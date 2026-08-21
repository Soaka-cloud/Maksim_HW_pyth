from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button(self, button_text):
        self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']"
        ).click()

    def wait_for_result(self, expected_result):
        wait = WebDriverWait(self.driver, 50)
        wait.until(
            EC.text_to_be_present_in_element(self.RESULT, expected_result)
        )

    def get_result(self):
        return self.driver.find_element(*self.RESULT).text
