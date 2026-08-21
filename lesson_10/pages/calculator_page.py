from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Страница калькулятора с задержкой вычисления."""

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver: WebDriver) -> None:
        """Конструктор страницы.

        Args:
            driver: драйвер браузера.

        Returns:
            None
        """
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def open(self) -> None:
        """Открыть страницу калькулятора.

        Returns:
            None
        """
        self.driver.get(self.url)

    def set_delay(self, seconds: str) -> None:
        """Установить задержку вычисления результата.

        Args:
            seconds: значение задержки в секундах.

        Returns:
            None
        """
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button(self, button_text: str) -> None:
        """Нажать кнопку калькулятора.

        Args:
            button_text: текст кнопки (цифра или оператор).

        Returns:
            None
        """
        self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']"
        ).click()

    def wait_for_result(self, expected_result: str) -> None:
        """Дождаться появления результата на экране.

        Args:
            expected_result: ожидаемый результат.

        Returns:
            None
        """
        wait = WebDriverWait(self.driver, 50)
        wait.until(
            EC.text_to_be_present_in_element(self.RESULT, expected_result)
        )

    def get_result(self) -> str:
        """Получить текст результата с экрана калькулятора.

        Returns:
            Текст результата.
        """
        return self.driver.find_element(*self.RESULT).text
