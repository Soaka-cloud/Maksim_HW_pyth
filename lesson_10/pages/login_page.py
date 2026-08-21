from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Страница авторизации магазина Saucedemo."""

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver: WebDriver) -> None:
        """Конструктор страницы.

        Args:
            driver: драйвер браузера.

        Returns:
            None
        """
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self) -> None:
        """Открыть страницу авторизации.

        Returns:
            None
        """
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        """Авторизоваться под указанным пользователем.

        Args:
            username: логин пользователя.
            password: пароль пользователя.

        Returns:
            None
        """
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
