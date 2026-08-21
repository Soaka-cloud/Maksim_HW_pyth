import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    driver_instance = webdriver.Chrome(options=options)
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()


def test_calc(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    wait = WebDriverWait(driver, 50)

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    for button_text in ["7", "+", "8", "="]:
        driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']"
        ).click()

    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    assert driver.find_element(By.CSS_SELECTOR, ".screen").text == "15"


if __name__ == "__main__":
    pytest.main(["-v", __file__])
