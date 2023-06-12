import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(RegisterPage, self).__init__(driver, wait_driver)

    def register_account(self, firstname: str, lastname: str, email: str, telephone: str, pswd: str, pswdConf: str):
        self.element("firstnm_input").wait_clickable().send_keys(firstname)
        self.element("lastnm_input").wait_clickable().send_keys(lastname)
        self.element("email_input").wait_visible().send_keys(email)
        self.element("telephone_input").wait_visible().send_keys(telephone)
        self.element("pswd_input").wait_visible().send_keys(pswd)
        self.element("pswdConf_input").wait_visible().send_keys(pswdConf)
        self.element("agree_box").wait_visible().click()
        self.element("continue_btn").wait_visible().click()

