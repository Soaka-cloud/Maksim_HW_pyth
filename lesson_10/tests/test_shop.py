import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.title("Покупка товаров в интернет-магазине")
@allure.description("Авторизация, добавление трёх товаров в корзину, "
                    "оформление заказа и проверка итоговой суммы $58.29")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.BLOCKER)
def test_shop(firefox_driver):
    login = LoginPage(firefox_driver)

    with allure.step("Авторизоваться под пользователем standard_user"):
        login.open()
        login.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        inventory = InventoryPage(firefox_driver)
        inventory.add_to_cart("sauce-labs-backpack")
        inventory.add_to_cart("sauce-labs-bolt-t-shirt")
        inventory.add_to_cart("sauce-labs-onesie")

    with allure.step("Перейти в корзину"):
        inventory.go_to_cart()

    with allure.step("Проверить, что в корзине 3 товара"):
        cart = CartPage(firefox_driver)
        assert cart.get_item_count() == "3"

    with allure.step("Нажать кнопку Checkout"):
        cart.checkout()

    with allure.step("Заполнить форму оформления заказа"):
        checkout = CheckoutPage(firefox_driver)
        checkout.fill_form("Иван", "Петров", "123456")

    with allure.step("Нажать кнопку Continue"):
        checkout.continue_checkout()

    with allure.step("Проверить, что итоговая сумма равна $58.29"):
        assert checkout.get_total() == "Total: $58.29"
