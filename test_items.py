import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_visibility_of_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket").is_displayed()
    assert button, "should be visible"
