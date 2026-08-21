from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Страница корзины магазина."""

    CHECKOUT_BUTTON = (By.ID, "checkout")
    ITEM_COUNT = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def __init__(self, driver: WebDriver) -> None:
        """Конструктор страницы.

        Args:
            driver: драйвер браузера.

        Returns:
            None
        """
        self.driver = driver

    def get_item_count(self) -> str:
        """Получить количество товаров в корзине.

        Returns:
            Количество товаров в виде строки.
        """
        return self.driver.find_element(*self.ITEM_COUNT).text

    def checkout(self) -> None:
        """Нажать кнопку Checkout.

        Returns:
            None
        """
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
