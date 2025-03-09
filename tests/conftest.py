from typing import Any, Generator

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver


@pytest.fixture
def driver() -> Generator[WebDriver, Any, None]:
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def close_cookies(driver):
    cookie_button_xpath = "//button[contains(@class, 'App_CookieButton')]"
    try:
        driver.find_element(By.XPATH, cookie_button_xpath).click()
    except Exception:
        pass
