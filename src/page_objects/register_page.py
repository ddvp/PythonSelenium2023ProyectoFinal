import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(RegisterPage, self).__init__(driver, wait_driver)

    def register_account(self, first_name: str, last_name: str, email: str, telephone: str, pswd: str, pswdConf: str):
        self.element("first_name_input").wait_clickable().send_keys(first_name)
        self.element("last_name_input").wait_clickable().send_keys(last_name)
        self.element("email_input").wait_clickable().send_keys(email)
        self.element("telephone_input").wait_clickable().send_keys(telephone)
        self.element("pswd_input").wait_clickable().send_keys(pswd)
        self.element("pswdConf_input").wait_clickable().send_keys(pswdConf)
        self.element("agree_box").wait_clickable().click()
        self.element("continue_btn").wait_clickable().click()

