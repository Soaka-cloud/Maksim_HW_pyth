from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()

    try:
        driver.get("https://httpbin.qa-territory.online/forms/post")

        name_field = driver.find_element(By.NAME, "custname")
        name_field.clear()
        name_field.send_keys("Maksim")

        submit_button = driver.find_element(
            By.XPATH, "//button[text()='Submit order']"
        )
        submit_button.click()

        assert "/post" in driver.current_url

    finally:
        driver.quit()


if __name__ == "__main__":
    test_form_submission()
