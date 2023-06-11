from src.page_objects.register_page import RegisterPage


def test_valid_register(web_drivers):
    register_page = RegisterPage(*web_drivers)
    register_page.open()
    register_page.register_account("Juan", "Martinez", "juan@test.com", "3311098733", "test1234", "test1234")
