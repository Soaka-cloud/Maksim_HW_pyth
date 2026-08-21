from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """Главная страница магазина со списком товаров."""

    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver: WebDriver) -> None:
        """Конструктор страницы.

        Args:
            driver: драйвер браузера.

        Returns:
            None
        """
        self.driver = driver

    def add_to_cart(self, item_id: str) -> None:
        """Добавить товар в корзину.

        Args:
            item_id: идентификатор товара.

        Returns:
            None
        """
        self.driver.find_element(
            By.ID, f"add-to-cart-{item_id}"
        ).click()

    def go_to_cart(self) -> None:
        """Перейти в корзину.

        Returns:
            None
        """
        self.driver.find_element(*self.CART_LINK).click()
