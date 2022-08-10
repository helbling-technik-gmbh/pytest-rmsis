import sgqlc.types


rmsis_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class BaselineStatusEnum(sgqlc.types.Enum):
    __schema__ = rmsis_schema
    __choices__ = ('NOT_BASELINED', 'BASELINED', 'MARKED_FOR_BASELINE', 'MARKED_AND_MODIFIED')


class BigDecimal(sgqlc.types.Scalar):
    __schema__ = rmsis_schema


Boolean = sgqlc.types.Boolean

class CustomFieldTypeEnum(sgqlc.types.Enum):
    __schema__ = rmsis_schema
    __choices__ = ('TEXT', 'INTEGER', 'DATE', 'REAL', 'RICH_TEXT', 'SINGLE_SELECT', 'MULTI_SELECT', 'HIERARCHICAL_MULTI_SELECT')


class CustomObject(sgqlc.types.Scalar):
    __schema__ = rmsis_schema


class EntityTypes(sgqlc.types.Enum):
    __schema__ = rmsis_schema
    __choices__ = ('PROJECT', 'REQUIREMENT', 'ARTIFACT', 'TEST_CASE', 'TEST_RUN', 'RELEASE', 'BASELINE')


Int = sgqlc.types.Int

class Long(sgqlc.types.Scalar):
    __schema__ = rmsis_schema


class RelationshipEnum(sgqlc.types.Enum):
    __schema__ = rmsis_schema
    __choices__ = ('PROJECT_REQUIREMENT', 'PROJECT_TEST_CASE', 'PROJECT_TEST_RUN', 'PROJECT_ARTIFACT', 'PROJECT_RELEASE', 'PROJECT_BASELINE', 'RELEASE_REQUIREMENT', 'RELEASE_TEST_RUN', 'BASELINE_REQUIREMENT', 'REQUIREMENT_DEPENDENCY', 'REQUIREMENT_TEST_CASE', 'REQUIREMENT_ARTIFACT', 'TEST_CASE_DEPENDENCY', 'TEST_CASE_ARTIFACT', 'TEST_RUN_TEST_CASE')


String = sgqlc.types.String

class StringMin0Max255(sgqlc.types.Scalar):
    __schema__ = rmsis_schema


class TestCaseViewEnum(sgqlc.types.Enum):
    __schema__ = rmsis_schema
    __choices__ = ('LATEST', 'ALL')



########################################################################
# Input Objects
########################################################################
class CustomFieldFilterInput(sgqlc.types.Input):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'values')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Long)), graphql_name='values')


class MultiSelectInput(sgqlc.types.Input):
    __schema__ = rmsis_schema
    __field_names__ = ('add', 'remove')
    add = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='add')
    remove = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='remove')


class NameDescriptionInput(sgqlc.types.Input):
    __schema__ = rmsis_schema
    __field_names__ = ('name', 'description')
    name = sgqlc.types.Field(StringMin0Max255, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')


class Pagination(sgqlc.types.Input):
    __schema__ = rmsis_schema
    __field_names__ = ('start_index', 'page_size')
    start_index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='startIndex')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')


class PlannedRequirementInput(sgqlc.types.Input):
    __schema__ = rmsis_schema
    __field_names__ = ('summary', 'description', 'category_map', 'actual_effort', 'assignee', 'priority', 'criticality', 'feasibility', 'technical_risk', 'requirement_status', 'watcher_map', 'internal_source_map', 'external_source_map', 'size', 'effort')
    summary = sgqlc.types.Field(String, graphql_name='summary')
    description = sgqlc.types.Field(String, graphql_name='description')
    category_map = sgqlc.types.Field(MultiSelectInput, graphql_name='categoryMap')
    actual_effort = sgqlc.types.Field(BigDecimal, graphql_name='actualEffort')
    assignee = sgqlc.types.Field(Long, graphql_name='assignee')
    priority = sgqlc.types.Field(Long, graphql_name='priority')
    criticality = sgqlc.types.Field(Long, graphql_name='criticality')
    feasibility = sgqlc.types.Field(Long, graphql_name='feasibility')
    technical_risk = sgqlc.types.Field(Long, graphql_name='technicalRisk')
    requirement_status = sgqlc.types.Field(Long, graphql_name='requirementStatus')
    watcher_map = sgqlc.types.Field(MultiSelectInput, graphql_name='watcherMap')
    internal_source_map = sgqlc.types.Field(MultiSelectInput, graphql_name='internalSourceMap')
    external_source_map = sgqlc.types.Field(MultiSelectInput, graphql_name='externalSourceMap')
    size = sgqlc.types.Field(BigDecimal, graphql_name='size')
    effort = sgqlc.types.Field(BigDecimal, graphql_name='effort')


class ReleaseInput(sgqlc.types.Input):
    __schema__ = rmsis_schema
    __field_names__ = ('name', 'description', 'planned_date', 'actual_date', 'release_status')
    name = sgqlc.types.Field(StringMin0Max255, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    planned_date = sgqlc.types.Field(String, graphql_name='plannedDate')
    actual_date = sgqlc.types.Field(String, graphql_name='actualDate')
    release_status = sgqlc.types.Field(Long, graphql_name='releaseStatus')


class TestCaseInput(sgqlc.types.Input):
    __schema__ = rmsis_schema
    __field_names__ = ('name', 'description', 'external_id', 'category_map')
    name = sgqlc.types.Field(StringMin0Max255, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    external_id = sgqlc.types.Field(String, graphql_name='externalId')
    category_map = sgqlc.types.Field(MultiSelectInput, graphql_name='categoryMap')


class TestRunInput(sgqlc.types.Input):
    __schema__ = rmsis_schema
    __field_names__ = ('name', 'description', 'version', 'environment', 'start_date', 'end_date', 'release')
    name = sgqlc.types.Field(StringMin0Max255, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    version = sgqlc.types.Field(StringMin0Max255, graphql_name='version')
    environment = sgqlc.types.Field(StringMin0Max255, graphql_name='environment')
    start_date = sgqlc.types.Field(String, graphql_name='startDate')
    end_date = sgqlc.types.Field(String, graphql_name='endDate')
    release = sgqlc.types.Field(Long, graphql_name='release')


class TestStepInput(sgqlc.types.Input):
    __schema__ = rmsis_schema
    __field_names__ = ('action', 'expected_result')
    action = sgqlc.types.Field(String, graphql_name='action')
    expected_result = sgqlc.types.Field(String, graphql_name='expectedResult')


class UnplannedRequirementInput(sgqlc.types.Input):
    __schema__ = rmsis_schema
    __field_names__ = ('summary', 'description', 'category_map', 'priority', 'criticality', 'feasibility', 'technical_risk', 'requirement_status', 'watcher_map', 'internal_source_map', 'external_source_map', 'size', 'effort')
    summary = sgqlc.types.Field(String, graphql_name='summary')
    description = sgqlc.types.Field(String, graphql_name='description')
    category_map = sgqlc.types.Field(MultiSelectInput, graphql_name='categoryMap')
    priority = sgqlc.types.Field(Long, graphql_name='priority')
    criticality = sgqlc.types.Field(Long, graphql_name='criticality')
    feasibility = sgqlc.types.Field(Long, graphql_name='feasibility')
    technical_risk = sgqlc.types.Field(Long, graphql_name='technicalRisk')
    requirement_status = sgqlc.types.Field(Long, graphql_name='requirementStatus')
    watcher_map = sgqlc.types.Field(MultiSelectInput, graphql_name='watcherMap')
    internal_source_map = sgqlc.types.Field(MultiSelectInput, graphql_name='internalSourceMap')
    external_source_map = sgqlc.types.Field(MultiSelectInput, graphql_name='externalSourceMap')
    size = sgqlc.types.Field(BigDecimal, graphql_name='size')
    effort = sgqlc.types.Field(BigDecimal, graphql_name='effort')



########################################################################
# Output Objects and Interfaces
########################################################################
class Artifact(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'external_id', 'summary')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    external_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='externalId')
    summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='summary')


class Attachment(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'name', 'url', 'document')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(String, graphql_name='url')
    document = sgqlc.types.Field('Document', graphql_name='document')


class Baseline(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'name', 'description', 'is_committed')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_committed = sgqlc.types.Field(String, graphql_name='isCommitted')


class CustomField(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'name', 'unit', 'type', 'is_editable_after_entity_commit', 'is_global', 'options')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    type = sgqlc.types.Field(sgqlc.types.non_null(CustomFieldTypeEnum), graphql_name='type')
    is_editable_after_entity_commit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEditableAfterEntityCommit')
    is_global = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isGlobal')
    options = sgqlc.types.Field(sgqlc.types.list_of('Option'), graphql_name='options')


class CustomFieldData(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'name', 'unit', 'type', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    type = sgqlc.types.Field(sgqlc.types.non_null(CustomFieldTypeEnum), graphql_name='type')
    value = sgqlc.types.Field(CustomObject, graphql_name='value')


class Document(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'data')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='data')


class Filter(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class MutationType(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('create_planned_requirement', 'delete_requirement', 'update_planned_requirement', 'create_unplanned_requirement', 'update_unplanned_requirement', 'create_release', 'update_release', 'delete_release', 'create_test_case', 'update_test_case', 'delete_test_case', 'create_test_run', 'update_test_run', 'delete_test_run', 'create_test_step', 'update_test_step', 'delete_test_step', 'create_relationship', 'delete_relationship', 'update_test_case_by_test_run', 'update_test_step_by_test_run', 'update_requirement_custom_field', 'update_test_case_custom_field', 'update_test_step_custom_field', 'create_requirement_category', 'update_requirement_category', 'delete_requirement_category', 'create_test_case_category', 'update_test_case_category', 'delete_test_case_category', 'create_external_source', 'update_external_source', 'delete_external_source')
    create_planned_requirement = sgqlc.types.Field('PlannedRequirement', graphql_name='createPlannedRequirement', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('summary', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='summary', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
))
    )
    delete_requirement = sgqlc.types.Field(Boolean, graphql_name='deleteRequirement', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    update_planned_requirement = sgqlc.types.Field('PlannedRequirement', graphql_name='updatePlannedRequirement', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
        ('requirement', sgqlc.types.Arg(sgqlc.types.non_null(PlannedRequirementInput), graphql_name='requirement', default=None)),
))
    )
    create_unplanned_requirement = sgqlc.types.Field('UnplannedRequirement', graphql_name='createUnplannedRequirement', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('summary', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='summary', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
))
    )
    update_unplanned_requirement = sgqlc.types.Field('UnplannedRequirement', graphql_name='updateUnplannedRequirement', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
        ('requirement', sgqlc.types.Arg(sgqlc.types.non_null(UnplannedRequirementInput), graphql_name='requirement', default=None)),
))
    )
    create_release = sgqlc.types.Field('Release', graphql_name='createRelease', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('release', sgqlc.types.Arg(sgqlc.types.non_null(ReleaseInput), graphql_name='release', default=None)),
))
    )
    update_release = sgqlc.types.Field('Release', graphql_name='updateRelease', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
        ('release', sgqlc.types.Arg(sgqlc.types.non_null(ReleaseInput), graphql_name='release', default=None)),
))
    )
    delete_release = sgqlc.types.Field(Boolean, graphql_name='deleteRelease', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    create_test_case = sgqlc.types.Field('TestCase', graphql_name='createTestCase', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('test_case', sgqlc.types.Arg(sgqlc.types.non_null(TestCaseInput), graphql_name='testCase', default=None)),
))
    )
    update_test_case = sgqlc.types.Field('TestCase', graphql_name='updateTestCase', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
        ('test_case', sgqlc.types.Arg(sgqlc.types.non_null(TestCaseInput), graphql_name='testCase', default=None)),
))
    )
    delete_test_case = sgqlc.types.Field(Boolean, graphql_name='deleteTestCase', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    create_test_run = sgqlc.types.Field('TestRun', graphql_name='createTestRun', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('test_run', sgqlc.types.Arg(sgqlc.types.non_null(TestRunInput), graphql_name='testRun', default=None)),
))
    )
    update_test_run = sgqlc.types.Field('TestRun', graphql_name='updateTestRun', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
        ('test_run', sgqlc.types.Arg(sgqlc.types.non_null(TestRunInput), graphql_name='testRun', default=None)),
))
    )
    delete_test_run = sgqlc.types.Field(Boolean, graphql_name='deleteTestRun', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    create_test_step = sgqlc.types.Field('TestStep', graphql_name='createTestStep', args=sgqlc.types.ArgDict((
        ('test_case_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='testCaseId', default=None)),
        ('test_step', sgqlc.types.Arg(sgqlc.types.non_null(TestStepInput), graphql_name='testStep', default=None)),
))
    )
    update_test_step = sgqlc.types.Field('TestStep', graphql_name='updateTestStep', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
        ('test_step', sgqlc.types.Arg(sgqlc.types.non_null(TestStepInput), graphql_name='testStep', default=None)),
))
    )
    delete_test_step = sgqlc.types.Field(Boolean, graphql_name='deleteTestStep', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    create_relationship = sgqlc.types.Field(Boolean, graphql_name='createRelationship', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(RelationshipEnum), graphql_name='name', default=None)),
        ('source_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='sourceId', default=None)),
        ('target_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='targetId', default=None)),
))
    )
    delete_relationship = sgqlc.types.Field(Boolean, graphql_name='deleteRelationship', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(RelationshipEnum), graphql_name='name', default=None)),
        ('source_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='sourceId', default=None)),
        ('target_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='targetId', default=None)),
))
    )
    update_test_case_by_test_run = sgqlc.types.Field('TestRunLinkedTestCase', graphql_name='updateTestCaseByTestRun', args=sgqlc.types.ArgDict((
        ('test_run_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='testRunId', default=None)),
        ('test_case_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='testCaseId', default=None)),
        ('test_case_status_id', sgqlc.types.Arg(Long, graphql_name='testCaseStatusId', default=None)),
        ('assignee_id', sgqlc.types.Arg(Long, graphql_name='assigneeId', default=None)),
))
    )
    update_test_step_by_test_run = sgqlc.types.Field('TestRunLinkedTestStep', graphql_name='updateTestStepByTestRun', args=sgqlc.types.ArgDict((
        ('test_run_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='testRunId', default=None)),
        ('test_step_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='testStepId', default=None)),
        ('test_step_status_id', sgqlc.types.Arg(Long, graphql_name='testStepStatusId', default=None)),
        ('actual_result', sgqlc.types.Arg(String, graphql_name='actualResult', default=None)),
))
    )
    update_requirement_custom_field = sgqlc.types.Field(Boolean, graphql_name='updateRequirementCustomField', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
        ('custom_field_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='customFieldId', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(CustomObject), graphql_name='value', default=None)),
))
    )
    update_test_case_custom_field = sgqlc.types.Field(Boolean, graphql_name='updateTestCaseCustomField', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
        ('custom_field_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='customFieldId', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(CustomObject), graphql_name='value', default=None)),
))
    )
    update_test_step_custom_field = sgqlc.types.Field(Boolean, graphql_name='updateTestStepCustomField', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
        ('custom_field_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='customFieldId', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(CustomObject), graphql_name='value', default=None)),
))
    )
    create_requirement_category = sgqlc.types.Field('Option', graphql_name='createRequirementCategory', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(StringMin0Max255), graphql_name='name', default=None)),
))
    )
    update_requirement_category = sgqlc.types.Field('Option', graphql_name='updateRequirementCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(StringMin0Max255), graphql_name='name', default=None)),
))
    )
    delete_requirement_category = sgqlc.types.Field(Boolean, graphql_name='deleteRequirementCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    create_test_case_category = sgqlc.types.Field('Option', graphql_name='createTestCaseCategory', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(StringMin0Max255), graphql_name='name', default=None)),
))
    )
    update_test_case_category = sgqlc.types.Field('Option', graphql_name='updateTestCaseCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(StringMin0Max255), graphql_name='name', default=None)),
))
    )
    delete_test_case_category = sgqlc.types.Field(Boolean, graphql_name='deleteTestCaseCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    create_external_source = sgqlc.types.Field('NameDescriptionEntity', graphql_name='createExternalSource', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('external_source', sgqlc.types.Arg(sgqlc.types.non_null(NameDescriptionInput), graphql_name='externalSource', default=None)),
))
    )
    update_external_source = sgqlc.types.Field('NameDescriptionEntity', graphql_name='updateExternalSource', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
        ('external_source', sgqlc.types.Arg(sgqlc.types.non_null(NameDescriptionInput), graphql_name='externalSource', default=None)),
))
    )
    delete_external_source = sgqlc.types.Field(Boolean, graphql_name='deleteExternalSource', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )


class NameDescriptionEntity(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'name', 'description')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')


class Option(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class PlannedRequirement(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'key', 'summary', 'description', 'categories', 'baselines', 'external_id', 'actual_effort', 'assignee', 'parent_id', 'is_committed', 'is_parent', 'priority', 'criticality', 'feasibility', 'technical_risk', 'requirement_status', 'reporter', 'watchers', 'internal_sources', 'external_sources', 'custom_fields', 'size', 'effort', 'attachments', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='summary')
    description = sgqlc.types.Field(String, graphql_name='description')
    categories = sgqlc.types.Field(sgqlc.types.list_of(Option), graphql_name='categories')
    baselines = sgqlc.types.Field(sgqlc.types.list_of(Baseline), graphql_name='baselines')
    external_id = sgqlc.types.Field(String, graphql_name='externalId')
    actual_effort = sgqlc.types.Field(BigDecimal, graphql_name='actualEffort')
    assignee = sgqlc.types.Field('User', graphql_name='assignee')
    parent_id = sgqlc.types.Field(Long, graphql_name='parentId')
    is_committed = sgqlc.types.Field(Boolean, graphql_name='isCommitted')
    is_parent = sgqlc.types.Field(Boolean, graphql_name='isParent')
    priority = sgqlc.types.Field(Option, graphql_name='priority')
    criticality = sgqlc.types.Field(Option, graphql_name='criticality')
    feasibility = sgqlc.types.Field(Option, graphql_name='feasibility')
    technical_risk = sgqlc.types.Field(Option, graphql_name='technicalRisk')
    requirement_status = sgqlc.types.Field(Option, graphql_name='requirementStatus')
    reporter = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='reporter')
    watchers = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='watchers')
    internal_sources = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='internalSources')
    external_sources = sgqlc.types.Field(sgqlc.types.list_of(NameDescriptionEntity), graphql_name='externalSources')
    custom_fields = sgqlc.types.Field(sgqlc.types.list_of(CustomFieldData), graphql_name='customFields')
    size = sgqlc.types.Field(BigDecimal, graphql_name='size')
    effort = sgqlc.types.Field(BigDecimal, graphql_name='effort')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(Attachment), graphql_name='attachments')
    created_at = sgqlc.types.Field(String, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(String, graphql_name='updatedAt')


class Project(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'external_id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    external_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='externalId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class QueryType(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('get_projects', 'get_project_by_id', 'get_project_by_external_id', 'get_users', 'get_user_by_id', 'get_user_by_external_id', 'get_priorities', 'get_criticalities', 'get_feasibilities', 'get_technical_risks', 'get_planned_requirement_statuses', 'get_unplanned_requirement_statuses', 'get_release_statuses', 'get_test_case_statuses', 'get_test_step_statuses', 'get_requirement_custom_fields', 'get_test_case_custom_fields', 'get_test_step_custom_fields', 'get_planned_requirement_filters', 'get_unplanned_requirement_filters', 'get_release_filters', 'get_artifact_filters', 'get_test_case_filters', 'get_test_run_filters', 'get_planned_requirements_by_filter', 'get_requirement_by_id', 'search_planned_requirements', 'get_unplanned_requirements_by_filter', 'search_unplanned_requirements', 'get_test_cases_by_filter', 'get_test_case_by_id', 'search_test_cases', 'get_test_cases_by_test_run_filter', 'get_test_cases_by_test_run', 'get_test_run_test_case_by_id', 'search_test_cases_by_test_run', 'get_artifacts_by_filter', 'get_artifact_by_id', 'get_artifact_by_external_id', 'get_releases_by_filter', 'get_release_by_id', 'search_releases', 'get_test_runs', 'get_test_run_by_id', 'get_relationships', 'get_target_relationship_entities', 'get_source_relationship_entities', 'get_baselines', 'get_baseline_by_id', 'get_external_sources', 'get_external_source_by_id', 'get_requirement_categories', 'get_requirement_category_by_id', 'get_test_case_categories', 'get_test_case_category_by_id', 'get_attachment_by_id')
    get_projects = sgqlc.types.Field(sgqlc.types.list_of(Project), graphql_name='getProjects')
    get_project_by_id = sgqlc.types.Field(Project, graphql_name='getProjectById', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    get_project_by_external_id = sgqlc.types.Field(Project, graphql_name='getProjectByExternalId', args=sgqlc.types.ArgDict((
        ('external_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='externalId', default=None)),
))
    )
    get_users = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='getUsers')
    get_user_by_id = sgqlc.types.Field('User', graphql_name='getUserById', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    get_user_by_external_id = sgqlc.types.Field('User', graphql_name='getUserByExternalId', args=sgqlc.types.ArgDict((
        ('external_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='externalId', default=None)),
))
    )
    get_priorities = sgqlc.types.Field(sgqlc.types.list_of(Option), graphql_name='getPriorities')
    get_criticalities = sgqlc.types.Field(sgqlc.types.list_of(Option), graphql_name='getCriticalities')
    get_feasibilities = sgqlc.types.Field(sgqlc.types.list_of(Option), graphql_name='getFeasibilities')
    get_technical_risks = sgqlc.types.Field(sgqlc.types.list_of(Option), graphql_name='getTechnicalRisks')
    get_planned_requirement_statuses = sgqlc.types.Field(sgqlc.types.list_of(Option), graphql_name='getPlannedRequirementStatuses')
    get_unplanned_requirement_statuses = sgqlc.types.Field(sgqlc.types.list_of(Option), graphql_name='getUnplannedRequirementStatuses')
    get_release_statuses = sgqlc.types.Field(sgqlc.types.list_of(Option), graphql_name='getReleaseStatuses')
    get_test_case_statuses = sgqlc.types.Field(sgqlc.types.list_of(Option), graphql_name='getTestCaseStatuses')
    get_test_step_statuses = sgqlc.types.Field(sgqlc.types.list_of(Option), graphql_name='getTestStepStatuses')
    get_requirement_custom_fields = sgqlc.types.Field(sgqlc.types.list_of(CustomField), graphql_name='getRequirementCustomFields', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
))
    )
    get_test_case_custom_fields = sgqlc.types.Field(sgqlc.types.list_of(CustomField), graphql_name='getTestCaseCustomFields', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
))
    )
    get_test_step_custom_fields = sgqlc.types.Field(sgqlc.types.list_of(CustomField), graphql_name='getTestStepCustomFields', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
))
    )
    get_planned_requirement_filters = sgqlc.types.Field(sgqlc.types.list_of(Filter), graphql_name='getPlannedRequirementFilters', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
))
    )
    get_unplanned_requirement_filters = sgqlc.types.Field(sgqlc.types.list_of(Filter), graphql_name='getUnplannedRequirementFilters', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
))
    )
    get_release_filters = sgqlc.types.Field(sgqlc.types.list_of(Filter), graphql_name='getReleaseFilters', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
))
    )
    get_artifact_filters = sgqlc.types.Field(sgqlc.types.list_of(Filter), graphql_name='getArtifactFilters', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
))
    )
    get_test_case_filters = sgqlc.types.Field(sgqlc.types.list_of(Filter), graphql_name='getTestCaseFilters', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
))
    )
    get_test_run_filters = sgqlc.types.Field(sgqlc.types.list_of(Filter), graphql_name='getTestRunFilters', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
))
    )
    get_planned_requirements_by_filter = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='getPlannedRequirementsByFilter', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('filter_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='filterId', default=None)),
))
    )
    get_requirement_by_id = sgqlc.types.Field(PlannedRequirement, graphql_name='getRequirementById', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    search_planned_requirements = sgqlc.types.Field(sgqlc.types.list_of(PlannedRequirement), graphql_name='searchPlannedRequirements', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('categories', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='categories', default=None)),
        ('priorities', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='priorities', default=None)),
        ('criticalities', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='criticalities', default=None)),
        ('feasibilities', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='feasibilities', default=None)),
        ('technical_risks', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='technicalRisks', default=None)),
        ('requirement_statuses', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='requirementStatuses', default=None)),
        ('baseline_statuses', sgqlc.types.Arg(sgqlc.types.list_of(BaselineStatusEnum), graphql_name='baselineStatuses', default=None)),
        ('releases', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='releases', default=None)),
        ('watchers', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='watchers', default=None)),
        ('reporters', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='reporters', default=None)),
        ('assignees', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='assignees', default=None)),
        ('external_sources', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='externalSources', default=None)),
        ('internal_sources', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='internalSources', default=None)),
        ('baseline', sgqlc.types.Arg(Long, graphql_name='baseline', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='ids', default=None)),
        ('custom_fields', sgqlc.types.Arg(sgqlc.types.list_of(CustomFieldFilterInput), graphql_name='customFields', default=None)),
))
    )
    get_unplanned_requirements_by_filter = sgqlc.types.Field(sgqlc.types.list_of('UnplannedRequirement'), graphql_name='getUnplannedRequirementsByFilter', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('filter_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='filterId', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(Pagination), graphql_name='pagination', default=None)),
))
    )
    search_unplanned_requirements = sgqlc.types.Field(sgqlc.types.list_of('UnplannedRequirement'), graphql_name='searchUnplannedRequirements', args=sgqlc.types.ArgDict((
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(Pagination), graphql_name='pagination', default=None)),
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('categories', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='categories', default=None)),
        ('priorities', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='priorities', default=None)),
        ('criticalities', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='criticalities', default=None)),
        ('feasibilities', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='feasibilities', default=None)),
        ('technical_risks', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='technicalRisks', default=None)),
        ('requirement_statuses', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='requirementStatuses', default=None)),
        ('releases', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='releases', default=None)),
        ('watchers', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='watchers', default=None)),
        ('reporters', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='reporters', default=None)),
        ('external_sources', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='externalSources', default=None)),
        ('internal_sources', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='internalSources', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='ids', default=None)),
        ('custom_fields', sgqlc.types.Arg(sgqlc.types.list_of(CustomFieldFilterInput), graphql_name='customFields', default=None)),
))
    )
    get_test_cases_by_filter = sgqlc.types.Field(sgqlc.types.list_of('TestCase'), graphql_name='getTestCasesByFilter', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('filter_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='filterId', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(Pagination), graphql_name='pagination', default=None)),
))
    )
    get_test_case_by_id = sgqlc.types.Field('TestCase', graphql_name='getTestCaseById', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    search_test_cases = sgqlc.types.Field(sgqlc.types.list_of('TestCase'), graphql_name='searchTestCases', args=sgqlc.types.ArgDict((
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(Pagination), graphql_name='pagination', default=None)),
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('categories', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='categories', default=None)),
        ('view', sgqlc.types.Arg(sgqlc.types.non_null(TestCaseViewEnum), graphql_name='view', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='ids', default=None)),
        ('custom_fields', sgqlc.types.Arg(sgqlc.types.list_of(CustomFieldFilterInput), graphql_name='customFields', default=None)),
))
    )
    get_test_cases_by_test_run_filter = sgqlc.types.Field(sgqlc.types.list_of('TestRunLinkedTestCase'), graphql_name='getTestCasesByTestRunFilter', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('filter_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='filterId', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(Pagination), graphql_name='pagination', default=None)),
))
    )
    get_test_cases_by_test_run = sgqlc.types.Field(sgqlc.types.list_of('TestRunLinkedTestCase'), graphql_name='getTestCasesByTestRun', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('test_run_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='testRunId', default=None)),
))
    )
    get_test_run_test_case_by_id = sgqlc.types.Field('TestRunLinkedTestCase', graphql_name='getTestRunTestCaseById', args=sgqlc.types.ArgDict((
        ('test_run_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='testRunId', default=None)),
        ('test_case_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='testCaseId', default=None)),
))
    )
    search_test_cases_by_test_run = sgqlc.types.Field(sgqlc.types.list_of('TestRunLinkedTestCase'), graphql_name='searchTestCasesByTestRun', args=sgqlc.types.ArgDict((
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(Pagination), graphql_name='pagination', default=None)),
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('test_run_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='testRunId', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('categories', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='categories', default=None)),
        ('statuses', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='statuses', default=None)),
        ('assignees', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='assignees', default=None)),
        ('view', sgqlc.types.Arg(sgqlc.types.non_null(TestCaseViewEnum), graphql_name='view', default=None)),
        ('custom_fields', sgqlc.types.Arg(sgqlc.types.list_of(CustomFieldFilterInput), graphql_name='customFields', default=None)),
))
    )
    get_artifacts_by_filter = sgqlc.types.Field(sgqlc.types.list_of(Artifact), graphql_name='getArtifactsByFilter', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('filter_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='filterId', default=None)),
))
    )
    get_artifact_by_id = sgqlc.types.Field(Artifact, graphql_name='getArtifactById', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    get_artifact_by_external_id = sgqlc.types.Field(Artifact, graphql_name='getArtifactByExternalId', args=sgqlc.types.ArgDict((
        ('external_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='externalId', default=None)),
))
    )
    get_releases_by_filter = sgqlc.types.Field(sgqlc.types.list_of('Release'), graphql_name='getReleasesByFilter', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('filter_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='filterId', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(Pagination), graphql_name='pagination', default=None)),
))
    )
    get_release_by_id = sgqlc.types.Field('Release', graphql_name='getReleaseById', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    search_releases = sgqlc.types.Field(sgqlc.types.list_of('Release'), graphql_name='searchReleases', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
        ('pagination', sgqlc.types.Arg(sgqlc.types.non_null(Pagination), graphql_name='pagination', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('statuses', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='statuses', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Long), graphql_name='ids', default=None)),
))
    )
    get_test_runs = sgqlc.types.Field(sgqlc.types.list_of('TestRun'), graphql_name='getTestRuns', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
))
    )
    get_test_run_by_id = sgqlc.types.Field('TestRun', graphql_name='getTestRunById', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    get_relationships = sgqlc.types.Field(sgqlc.types.list_of('RelationType'), graphql_name='getRelationships')
    get_target_relationship_entities = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='getTargetRelationshipEntities', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(RelationshipEnum), graphql_name='name', default=None)),
        ('source_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='sourceId', default=None)),
))
    )
    get_source_relationship_entities = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='getSourceRelationshipEntities', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(RelationshipEnum), graphql_name='name', default=None)),
        ('target_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='targetId', default=None)),
))
    )
    get_baselines = sgqlc.types.Field(sgqlc.types.list_of(Baseline), graphql_name='getBaselines', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
))
    )
    get_baseline_by_id = sgqlc.types.Field(sgqlc.types.non_null(Baseline), graphql_name='getBaselineById', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    get_external_sources = sgqlc.types.Field(sgqlc.types.list_of(NameDescriptionEntity), graphql_name='getExternalSources', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
))
    )
    get_external_source_by_id = sgqlc.types.Field(sgqlc.types.non_null(NameDescriptionEntity), graphql_name='getExternalSourceById', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    get_requirement_categories = sgqlc.types.Field(sgqlc.types.list_of(Option), graphql_name='getRequirementCategories', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
))
    )
    get_requirement_category_by_id = sgqlc.types.Field(Option, graphql_name='getRequirementCategoryById', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    get_test_case_categories = sgqlc.types.Field(sgqlc.types.list_of(Option), graphql_name='getTestCaseCategories', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='projectId', default=None)),
))
    )
    get_test_case_category_by_id = sgqlc.types.Field(Option, graphql_name='getTestCaseCategoryById', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    get_attachment_by_id = sgqlc.types.Field(Attachment, graphql_name='getAttachmentById', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )


class RelationType(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('name', 'description', 'source', 'target')
    name = sgqlc.types.Field(sgqlc.types.non_null(RelationshipEnum), graphql_name='name')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    source = sgqlc.types.Field(sgqlc.types.non_null(EntityTypes), graphql_name='source')
    target = sgqlc.types.Field(sgqlc.types.non_null(EntityTypes), graphql_name='target')


class Release(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'name', 'description', 'planned_date', 'actual_date', 'release_status', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    planned_date = sgqlc.types.Field(String, graphql_name='plannedDate')
    actual_date = sgqlc.types.Field(String, graphql_name='actualDate')
    release_status = sgqlc.types.Field(Option, graphql_name='releaseStatus')
    created_at = sgqlc.types.Field(String, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(String, graphql_name='updatedAt')


class TestCase(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'key', 'name', 'description', 'external_id', 'categories', 'is_committed', 'test_steps', 'custom_fields', 'attachments', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    external_id = sgqlc.types.Field(String, graphql_name='externalId')
    categories = sgqlc.types.Field(sgqlc.types.list_of(Option), graphql_name='categories')
    is_committed = sgqlc.types.Field(Boolean, graphql_name='isCommitted')
    test_steps = sgqlc.types.Field(sgqlc.types.list_of('TestStep'), graphql_name='testSteps')
    custom_fields = sgqlc.types.Field(sgqlc.types.list_of(CustomFieldData), graphql_name='customFields')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(Attachment), graphql_name='attachments')
    created_at = sgqlc.types.Field(String, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(String, graphql_name='updatedAt')


class TestRun(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'name', 'description', 'version', 'environment', 'start_date', 'end_date', 'release', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    version = sgqlc.types.Field(String, graphql_name='version')
    environment = sgqlc.types.Field(String, graphql_name='environment')
    start_date = sgqlc.types.Field(String, graphql_name='startDate')
    end_date = sgqlc.types.Field(String, graphql_name='endDate')
    release = sgqlc.types.Field(sgqlc.types.non_null(Release), graphql_name='release')
    created_at = sgqlc.types.Field(String, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(String, graphql_name='updatedAt')


class TestRunLinkedTestCase(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'key', 'name', 'description', 'external_id', 'categories', 'is_committed', 'test_case_status', 'assignee', 'test_steps', 'custom_fields', 'attachments', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    external_id = sgqlc.types.Field(String, graphql_name='externalId')
    categories = sgqlc.types.Field(sgqlc.types.list_of(Option), graphql_name='categories')
    is_committed = sgqlc.types.Field(Boolean, graphql_name='isCommitted')
    test_case_status = sgqlc.types.Field(Option, graphql_name='testCaseStatus')
    assignee = sgqlc.types.Field('User', graphql_name='assignee')
    test_steps = sgqlc.types.Field(sgqlc.types.list_of('TestRunLinkedTestStep'), graphql_name='testSteps')
    custom_fields = sgqlc.types.Field(sgqlc.types.list_of(CustomFieldData), graphql_name='customFields')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(Attachment), graphql_name='attachments')
    created_at = sgqlc.types.Field(String, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(String, graphql_name='updatedAt')


class TestRunLinkedTestStep(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'action', 'expected_result', 'actual_result', 'test_step_status', 'execution_attachments', 'custom_fields', 'attachments')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    expected_result = sgqlc.types.Field(String, graphql_name='expectedResult')
    actual_result = sgqlc.types.Field(String, graphql_name='actualResult')
    test_step_status = sgqlc.types.Field(Option, graphql_name='testStepStatus')
    execution_attachments = sgqlc.types.Field(sgqlc.types.list_of(Attachment), graphql_name='executionAttachments')
    custom_fields = sgqlc.types.Field(sgqlc.types.list_of(CustomFieldData), graphql_name='customFields')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(Attachment), graphql_name='attachments')


class TestStep(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'action', 'expected_result', 'custom_fields', 'attachments')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    expected_result = sgqlc.types.Field(String, graphql_name='expectedResult')
    custom_fields = sgqlc.types.Field(sgqlc.types.list_of(CustomFieldData), graphql_name='customFields')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(Attachment), graphql_name='attachments')


class UnplannedRequirement(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'key', 'summary', 'description', 'categories', 'priority', 'criticality', 'feasibility', 'technical_risk', 'requirement_status', 'reporter', 'watchers', 'internal_sources', 'external_sources', 'custom_fields', 'size', 'effort', 'attachments', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='summary')
    description = sgqlc.types.Field(String, graphql_name='description')
    categories = sgqlc.types.Field(sgqlc.types.list_of(Option), graphql_name='categories')
    priority = sgqlc.types.Field(Option, graphql_name='priority')
    criticality = sgqlc.types.Field(Option, graphql_name='criticality')
    feasibility = sgqlc.types.Field(Option, graphql_name='feasibility')
    technical_risk = sgqlc.types.Field(Option, graphql_name='technicalRisk')
    requirement_status = sgqlc.types.Field(Option, graphql_name='requirementStatus')
    reporter = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='reporter')
    watchers = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='watchers')
    internal_sources = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='internalSources')
    external_sources = sgqlc.types.Field(sgqlc.types.list_of(NameDescriptionEntity), graphql_name='externalSources')
    custom_fields = sgqlc.types.Field(sgqlc.types.list_of(CustomFieldData), graphql_name='customFields')
    size = sgqlc.types.Field(BigDecimal, graphql_name='size')
    effort = sgqlc.types.Field(BigDecimal, graphql_name='effort')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(Attachment), graphql_name='attachments')
    created_at = sgqlc.types.Field(String, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(String, graphql_name='updatedAt')


class User(sgqlc.types.Type):
    __schema__ = rmsis_schema
    __field_names__ = ('id', 'external_id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    external_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='externalId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
rmsis_schema.query_type = QueryType
rmsis_schema.mutation_type = MutationType
rmsis_schema.subscription_type = None

