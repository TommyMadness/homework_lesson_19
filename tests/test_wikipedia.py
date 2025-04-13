import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from locators import (
    search_button_locators,
    search_input_locators,
    search_result_locators,
)
from selene import browser, have, be


def test_check_search_functionality(mobile_management):
    with step("Type search"):
        platform = mobile_management
        if platform == "ios":
            pytest.skip("iOS app is not Wikipedia, skipping test.")
        browser.element(search_button_locators[platform]).click()
        browser.element(search_input_locators[platform]).type("Selenium")
        results = browser.all(search_result_locators[platform])

    with step("Verify content found"):
        results.should(have.size_greater_than(0))
        results.first.should(have.text("Selenium"))


def test_check_that_search_result_can_be_opened(mobile_management):
    with step("Type search"):
        platform = mobile_management
        if platform == "ios":
            pytest.skip("iOS app is not Wikipedia, skipping test.")
        browser.element(search_button_locators[platform]).click()
        browser.element(search_input_locators[platform]).type("BrowserStack")
        results = browser.all(search_result_locators[platform])

    with step("Open article"):
        results.first.click()

    with step("Verify article opened"):
        browser.element(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("BrowserStack")')
        ).should(be.visible)
