from src.page_objects.checkout_page import CheckoutPage


def test_checkout(web_drivers):
    checkout_page = CheckoutPage(*web_drivers)
    checkout_page.open()
    checkout_page.login("ddvp0188@qamindslab.com","test1234")
    checkout_page.click_checkout()
    checkout_page.new_address()
    checkout_page.fill_items("Laura", "Gomez","Test", "Vallarta", "GDL", "44230")
    checkout_page.continue_btn_payment()
    checkout_page.radio_btn_address()
    checkout_page.continue_delivery_btn_method()


