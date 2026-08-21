from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Страница оформления заказа."""

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver: WebDriver) -> None:
        """Конструктор страницы.

        Args:
            driver: драйвер браузера.

        Returns:
            None
        """
        self.driver = driver

    def fill_form(self, first_name: str, last_name: str,
                  postal_code: str) -> None:
        """Заполнить форму данными покупателя.

        Args:
            first_name: имя покупателя.
            last_name: фамилия покупателя.
            postal_code: почтовый индекс.

        Returns:
            None
        """
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(
            first_name
        )
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(
            postal_code
        )

    def continue_checkout(self) -> None:
        """Нажать кнопку Continue.

        Returns:
            None
        """
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total(self) -> str:
        """Получить итоговую стоимость заказа.

        Returns:
            Текст с итоговой суммой.
        """
        return self.driver.find_element(*self.TOTAL_LABEL).text
