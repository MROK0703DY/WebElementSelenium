"""Test for PageElement class."""

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from tutorial.page_element import PageElement


def test_click(driver: WebDriver) -> None:
    """Test for the click method"""
    # 1. Открыть страницу с тестом.
    # 2. Найти элемент.
    # 3. Кликнуть по нему.
    # 4. Проверить, что он был кликнут.
    button = PageElement(driver, (By.ID, "click"))
    span = PageElement(driver, (By.ID, "click_result"))
    button.click()

    # TODO: and assertion: something changed.
    assert span.get_text() == "Button clicked!"
    assert "Test click" in driver.page_source, "Element не найден"


def test_text(driver: WebDriver) -> None:
    """Test for the text method"""
    p_tag = PageElement(driver, (By.ID, "test_text"))

    assert (
        p_tag.get_text()
        == "Ты не должен даже слушать злоречия, не должен говорить худое о ком бы то ни было, не должен соблазняться ни на кого"
    )


def test_send_keys(driver: WebDriver) -> None:
    """Test for the send_keys method"""
    input_tag = PageElement(driver, (By.ID, "send_keys-input"))
    assert input_tag.value() == ""

    input_tag.send_keys("You are extraordinary!")
    assert input_tag.value() == "You are extraordinary!"


def test_value(driver: WebDriver) -> None:
    """Test for the value method"""
    assert PageElement(driver, (By.ID, "test_value")).value() == "Bai, you're a beauty!"


def test_clear(driver: WebDriver) -> None:
    """Test for the clear method"""
    assert PageElement(driver, (By.ID, "test_clear")).value() != ""
    assert PageElement(driver, (By.ID, "test_clear")).value() == "This must be cleared."
    PageElement(driver, (By.ID, "test_clear")).clear()
    assert PageElement(driver, (By.ID, "test_clear")).value() == ""


print(os.getcwd())
print("ok")
