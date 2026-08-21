from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop(firefox_driver):
    login = LoginPage(firefox_driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(firefox_driver)
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.add_to_cart("sauce-labs-bolt-t-shirt")
    inventory.add_to_cart("sauce-labs-onesie")
    inventory.go_to_cart()

    cart = CartPage(firefox_driver)
    assert cart.get_item_count() == "3"
    cart.checkout()

    checkout = CheckoutPage(firefox_driver)
    checkout.fill_form("Иван", "Петров", "123456")
    checkout.continue_checkout()

    assert checkout.get_total() == "Total: $58.29"
