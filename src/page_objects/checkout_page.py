import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from src.page_objects.base_page import BasePage

from src.page_objects.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(CheckoutPage, self).__init__(driver, wait_driver)

    def login(self, email: str, password: str):
        logging.info(f"Login with email address {email} and password *****")
        self.element("email_input").wait_clickable().send_keys(email)
        self.element("password_input").wait_clickable().send_keys(password)
        self.element("login_btn").wait_clickable().click()

    def click_checkout(self):
        self.element("checkout_btn").wait_clickable().click()

    def new_address(self):
        self.element("new_address_btn").wait_clickable().click()

    def fill_items(self, first_name: str, lastname: str, company: str, address1: str, city: str, post_code: str,
                   country: str):
        self.element("firstname_input").wait_visible().send_keys(first_name)
        self.element("lastname_input").wait_visible().send_keys(lastname)
        self.element("company_input").wait_visible().send_keys(company)
        self.element("address_input").wait_visible().send_keys(address1)
        self.element("city_input").wait_visible().send_keys(city)
        self.element("post_code_input").wait_visible().send_keys(post_code)

    def continue_btn_payment(self):
        self.element("continue_payment_btn").wait_clickable().click()

    def continue_delivery_btn_method(self):
        self.element("continue_delivery_method_btn").wait_clickable().click()


