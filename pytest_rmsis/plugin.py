from .rmsis import RMsis
import os

def pytest_addoption(parser):
    group = parser.getgroup('terminal reporting')
    group.addoption(
        '--rmsis',
        dest='rmsis_enabled',
        action='store_true',
        help='Enable sycronisation with RMsis'
    )
    group.addoption(
        '--rmsis-user',
        dest='rmsis_user',
        action='store',
        type=str,
        default=None,
        help='user name of RMsis account'
    )
    group.addoption(
        '--rmsis-password',
        dest='rmsis_password',
        action='store',
        type=str,
        default=None,
        help='user password of RMsis account'
    )
    group.addoption(
        '--rmsis-url',
        dest='rmsis_url',
        action='store',
        type=str,
        default=None,
        help='URL of RMsis server'
    )
    group.addoption(
        '--rmsis-project',
        dest='rmsis_project',
        action='store',
        type=str,
        default=None,
        help='Project of RMsis'
    )
    group.addoption(
        '--rmsis-release',
        dest='rmsis_release',
        action='store',
        type=str,
        default=None,
        help='Project Release of RMsis'
    )
    group.addoption(
        '--rmsis-testrun',
        dest='rmsis_testrun',
        action='store',
        type=str,
        default=None,
        help='Name of the testrun'
    )

def pytest_configure(config):
    if config.option.rmsis_enabled:
        # load user and password from environment variables or program arguments
        config._rmsis = RMsis(user=config.option.rmsis_user or os.environ.get("RMSIS_USR"),
                              password=config.option.rmsis_password or os.environ.get("RMSIS_PSW"),
                              url=config.option.rmsis_url or os.environ.get("RMSIS_URL"),
                              project=config.option.rmsis_project or os.environ.get("RMSIS_PROJECT"),
                              release=config.option.rmsis_release or os.environ.get("RMSIS_RELEASE"),
                              testrun=config.option.rmsis_testrun or os.environ.get("RMSIS_TESTRUN"))
        config.pluginmanager.register(config._rmsis)


    # register an additional marker
    config.addinivalue_line(
        "markers", "skip_rmsis: mark test to skip rmsis syncronisation"
    )
    config.addinivalue_line(
        "markers", "rmsis_requirement(requirement): set requirement of this test"
    )

def pytest_unconfigure(config):
    rmsis = getattr(config, '_rmsis', None)
    if rmsis:
        del config._rmsis
        config.pluginmanager.unregister(rmsis)
