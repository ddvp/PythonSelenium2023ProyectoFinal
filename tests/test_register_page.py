import time

from src.page_objects.register_page import RegisterPage
from src.page_objects.login_page import LoginPage


def test_valid_register(web_drivers):
    register_page = RegisterPage(*web_drivers)
    register_page.open()
    register_page.loggin("Juana", "Martinez","test@test.com","3311098733","test1234","test1234")
