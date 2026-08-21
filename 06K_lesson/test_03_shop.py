import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    options = webdriver.FirefoxOptions()
    driver_instance = webdriver.Firefox(options=options)
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()


def test_shop(driver):
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    for item in ["backpack", "bolt-t-shirt", "onesie"]:
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, f"add-to-cart-sauce-labs-{item}")
            )
        ).click()

    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    total_text = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".summary_total_label")
        )
    ).text

    assert total_text == "Total: $58.29"


if __name__ == "__main__":
    pytest.main(["-v", __file__])
