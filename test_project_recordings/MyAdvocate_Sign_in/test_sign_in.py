from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
from subtests import test_sign_in
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: MyAdvocate
    Package: TestProject.Generated.Tests.MyAdvocate
    Test: Sign in
    Generated by:   (vladislav@myadvocate.com)
    Generated on 04/24/2022, 15:41:53
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="XQV4YNVuSzEClPLRwOY0W-z9vrbmbnuRA1R84NW2RKQ1",
                              project_name="MyAdvocate",
                              job_name="Sign in")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Sign in full flow .

    au2425050.
    """
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://qat.d12dvpsxvwz2ny.amplifyapp.com/"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Login with existing user
    test_sign_in.test_main(driver)
