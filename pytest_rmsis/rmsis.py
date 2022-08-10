import pytest
from _pytest.reports import TestReport
from _pytest.main import Session
from sgqlc.operation import Operation
from .rmsis_schema import rmsis_schema as schema
from .rmsis_schema import TestCase, TestCaseInput, TestRun, TestRunInput, Release, RelationshipEnum, \
                          TestCaseViewEnum, Project, Pagination, PlannedRequirement
from sgqlc.endpoint.http import HTTPEndpoint
from base64 import b64encode
import typing

class RMsis(object):

    def __init__(self, user: str, password: str, url: str, project: str, release: str, testrun: str):
        """_summary_

        _extended_summary_

        :param user: RMsis user name
        :type user: str
        :param password: Rmsis user password
        :type password: str
        :param url: RMsis URL
        :type url: str
        :param project: RMsis project name
        :type project: str
        :param release: RMsis release name
        :type release: str
        :param testrun: Rmsis testrun name
        :type testrun: str
        """
        self.user = user
        self.password = password
        self.url = url
        self.project_name = project
        self.release_name = release
        self.testrun_name = testrun
        self.project = None
        self.testrun = None
        self.release = None
        self._worker = False

    def _get_project(self, name: str) -> Project:
        """get project by name

        :param name: name of the RMsis project
        :type name: str
        :raises LookupError: raised if project does not exist in RMsis
        :return: project of Rmsis
        :rtype: Project
        """
        op = Operation(schema.query_type)
        op.get_projects()
        data = self.endpoint(op)
        projects = [Project(json) for json in data['data']['getProjects']]

        try:
            return next(filter(lambda p: p.name == name, projects))
        except StopIteration:
            raise LookupError("Project {} not found".format(name))

    def _get_requirements(self, project: Project) -> typing.Sequence[PlannedRequirement]:
        """get list of requirements corresponding to a project

        :param project: project of RMsis
        :type project: Project
        :return: list of requirements
        :rtype: typing.Sequence[PlannedRequirement]
        """
        op = Operation(schema.query_type)
        op.search_planned_requirements(project_id = project.id)
        data = self.endpoint(op)
        requirements = [PlannedRequirement(json) for json in data['data']["searchPlannedRequirements"]]
        return requirements

    def _get_testcases(self, project: Project) -> typing.Sequence[TestCase]:
        """get list of testcases corresponding to a rmsis project

        :param project: project of RMsis 
        :type project: Project
        :return: list of Testcases
        :rtype: Sequeunce(TestCase)
        """
        page_index = 0
        testcases = []
        while True:
            op = Operation(schema.query_type)
            page = Pagination(start_index = page_index, page_size = 50)
            op.search_test_cases(project_id = project.id, pagination=page, view=TestCaseViewEnum.LATEST)
            data = self.endpoint(op)
            page_testcases = [TestCase(json) for json in data['data']['searchTestCases']]
            testcases += page_testcases
            page_index += 50

            if len(page_testcases) < 50:
                break
        return testcases

    def _get_release(self, release_name: str, project: Project) -> Release:
        """get release by name corresponding to a rmsis project

        :param release_name: name of the reelase
        :type release_name: str
        :param project: RMsis project
        :type project: Project
        :raises LookupError: raised if release was not found 
        :return: release
        :rtype: Release
        """
        page_index = 0
        releases = []
        while True:
            op = Operation(schema.query_type)
            page = Pagination(start_index = page_index, page_size = 50)
            op.search_releases(project_id = project.id, pagination=page)
            data = self.endpoint(op)
            page_releases = [Release(json) for json in data['data']['searchReleases']]
            releases += page_releases
            page_index += 50

            try:
                return next(filter(lambda r: r.name == release_name, releases))
            except StopIteration:
                # the wanted release was not found yet
                pass
            # do not try to fetch more testcases when the last page has less than 50
            # testcases
            if len(page_releases) < 50:
                break
        raise LookupError("Release {} not found".format(release_name))

    def _get_test_run_by_name(self, testrun_name: str, project: Project) -> TestRun:
        """get testrun by name from a project

        :param testrun_name: name of the testrun
        :type testrun_name: str
        :param project: corresponding project 
        :type project: Project
        :raises LookupError: raised if testrun does not exist in RMsis
        :return: testrun
        :rtype: TestRun
        """
        op = Operation(schema.query_type)
        op.get_test_runs(project_id = project.id)
        data = self.endpoint(op)
        test_runs = [TestRun(json) for json in data['data']['getTestRuns']]
        try:
            return next(filter(lambda p: p.name == testrun_name, test_runs))
        except StopIteration:
            raise LookupError("Project {} not found".format(testrun_name))        

    def _lookup_status_map(self) -> typing.Mapping[str, str]:
        """mapper for supported statuses by RMsis

        :raises LookupError: raised if RMsis does not support Pass, Failed or ???
        :return: mapping from pytest status to Rmsis status
        :rtype: typing.Mapping[str, str]
        """
        op = Operation(schema.query_type)
        op.get_test_case_statuses()
        statuses = self.endpoint(op)['data']['getTestCaseStatuses']
        status_map = {}
        try:
            status_map["passed"] = next(status['id'] for status in statuses if status['name'] == "Pass")
            status_map["failed"] = next(status['id'] for status in statuses if status['name'] == "Fail")
            status_map["skipped"] = next(status['id'] for status in statuses if status['name'] == "???")
        except StopIteration:
            raise LookupError("RMsis does not support the test-case statuses Pass|Failed|???")
        return status_map

    def _create_testcase(self, report: TestReport) -> TestCase:
        """create a testcase in RMsis

        :param report: test report from pytest
        :type report: TestReport
        :return: new testcase
        :rtype: TestCase
        """
        user_properties = dict(report.user_properties)

        op = Operation(schema.mutation_type)
        test_case = TestCaseInput(name=report.nodeid, description=user_properties['description'])
        op.create_test_case(project_id=self.project.id, test_case=test_case)
        return TestCase(self.endpoint(op)['data']['createTestCase'])

    def _update_testcase(self, rmsis_testcase: TestCase, report: TestReport) -> TestCase:
        """update an existing testcase in Rmsis

        :param rmsis_testcase: testcase from RMsis
        :type rmsis_testcase: TestCase
        :param report: test report from pytest
        :type report: TestReport
        :return: updated testcase
        :rtype: TestCase
        """
        user_properties = dict(report.user_properties)

        #if user_properties['description'] != rmsis_testcase['description']:

        # testcase changed
        op = Operation(schema.mutation_type)
        test_case = TestCaseInput(name=report.nodeid, description=user_properties['description'])
        op.update_test_case(id=rmsis_testcase.id, test_case=test_case)
        
        return TestCase(self.endpoint(op)['data']['updateTestCase'])
    
    def _create_testrun(self, release: Release, project: Project) -> TestRun:
        """create a new testrun in RMsis

        :param release: corresponding release in RMsis
        :type release: Release
        :param project: corresponding project in RMsis
        :type project: Project
        :return: created test run
        :rtype: TestRun
        """
        op = Operation(schema.mutation_type)
        test_run_input = TestRunInput(name = self.testrun_name,
                                      release = release.id)
        op.create_test_run(project_id = project.id, test_run = test_run_input)
        return TestRun(self.endpoint(op)['data']['createTestRun'])

    def _is_worker(self, session: Session) -> bool:
        """helper function for pytest-xdist support

        :param session: Pytest session
        :type session: Session
        :return: true if current code is executed in a pytest-xdist worker
        :rtype: bool
        """
        return getattr(session.config, 'workerinput', None) is not None

    def pytest_sessionstart(self, session: Session) -> None:
        """pytest hook executed on session start

        This code is run once when pytest is started. If this plugin is used in 
        combination with pytest-xdist, this hook is executed in the controller
        and in each worker. In the second case, the function returns immediately.

        :param session: pytest session
        :type session: Session
        """
        # only run on the master (if pytest-xdist is used)
        self._worker = self._is_worker(session)
        if self._worker:
            return 

        # build the endpoint url
        auth = b64encode("{}:{}".format(self.user, self.password).encode("ascii")).decode("ascii")
        headers = {'Authorization': 'Basic {}'.format(auth)}
        self.endpoint = HTTPEndpoint("{}/rest/service/latest/rmsis/graphql".format(self.url), headers)

        # find project id by project name
        self.project = self._get_project(self.project_name)

        # find release id by release name
        rmsis_release = self._get_release(self.release_name, self.project)

        # lookup available test status in rmsis
        self.status_map = self._lookup_status_map()
        
        # lookup testcases based on project id
        self.rmsis_testcases = self._get_testcases(self.project)

        # create a testrun 
        try:
            self.rmsis_testrun = self._get_test_run_by_name(self.testrun_name, self.project)
        except LookupError:
            self.rmsis_testrun = self._create_testrun(rmsis_release, self.project)

        self.rmsis_requirements = self._get_requirements(self.project)

    @pytest.hookimpl(hookwrapper=True, tryfirst=True)
    def pytest_runtest_makereport(self, item, call):
        """pytest hook executed before pytest_runtest_logreport

        This hook prepares the `TestReport` object which is handed over later
        to `pytest_runtest_logreport`. In case of pytest-xdist, this function
        is only executed on each worker. As this is the only please where
        the `item` object is accessable for inspections, the information are
        gathered here and attached to the test report. This is serialized and 
        send to the controller automatically by pytest.
        """
        # Because this is a hookwrapper, calling `yield` lets the actual hooks run & returns a `_Result`
        result = yield

        # Get the actual `TestReport` which the hook(s) returned, having done the hard work for you
        report = result.get_result()                

        # gather information
        description = item.obj.__doc__
        skip_rmsis = any(item.iter_markers(name="skip_rmsis"))
        requirements = [mark.args[0] for mark in item.iter_markers(name="rmsis_requirement")]

        # append extra information to report
        report.user_properties.append(('description', description))
        report.user_properties.append(('skip_rmsis', skip_rmsis))
        report.user_properties.append(('rmsis_requirements', requirements))

    def pytest_runtest_logreport(self, report: TestReport) -> None:
        """pytest hook executed as part of the pytest protocol.

        This hook is executed on worker and controller if used with pytest-xdist. As it only
        needs to run on the controller, the hook returns immediately on workers.

        :param report: test report
        :type report: TestReport
        """
        if self._worker or report.when != "call":
            return 

        user_properties = dict(report.user_properties)

        # if a test is marked with @pytest.mark.ski_rmsis, no rmsis syncronisation is required.
        if user_properties["skip_rmsis"]:
            return

        # create or update testcase in rmsis
        rmsis_testcase = next(filter(lambda t: t.name == report.nodeid, self.rmsis_testcases), None)
        if not rmsis_testcase:
            rmsis_testcase = self._create_testcase(report)
        else:
            rmsis_testcase = self._update_testcase(rmsis_testcase, report)

        # sync requirements to rmsis
        for key in user_properties['rmsis_requirements']:
            # Rmsis format keys in two ways:
            # 1) "XXXX-1"
            # 2) "XXXX-1 {2}" for baselines
            # following filter matches both
            key_filter = lambda r: r.key == key or r.key.startswith("{} ".format(key))

            # search for an existing requirement which matches the filter
            rmsis_requirement = next(filter(key_filter, self.rmsis_requirements), None)
            if rmsis_requirement:
                op = Operation(schema.mutation_type)
                op.create_relationship(name = RelationshipEnum.REQUIREMENT_TEST_CASE,
                                       source_id = rmsis_requirement.id,
                                       target_id = rmsis_testcase.id)
                self.endpoint(op)
            else:
                raise LookupError("Requirement {} not found".format(key))

        # assign testcase to the testrun
        op = Operation(schema.mutation_type)
        op.create_relationship(name = RelationshipEnum.TEST_RUN_TEST_CASE,
                                source_id = self.rmsis_testrun.id,
                                target_id = rmsis_testcase.id)
        self.endpoint(op)

        # update result in rmsis
        rmsis_status = self.status_map[report.outcome]
        op = Operation(schema.mutation_type)
        op.update_test_case_by_test_run(test_run_id = self.rmsis_testrun.id,
                                        test_case_id = rmsis_testcase.id,
                                        test_case_status_id = rmsis_status)
        self.endpoint(op)