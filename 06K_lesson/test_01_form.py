import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    options = webdriver.EdgeOptions()
    driver_instance = webdriver.Edge(options=options)
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()


def test_form(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    wait = WebDriverWait(driver, 10)

    values = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for name, value in values.items():
        field = wait.until(EC.presence_of_element_located((By.NAME, name)))
        field.send_keys(value)

    submit_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()

    wait.until(EC.url_contains("data-types-submitted.html"))

    zip_class = wait.until(
        lambda d: d.find_element(By.ID, "zip-code").get_attribute("class")
    )
    assert "alert-danger" in zip_class

    for field_id, expected_value in values.items():
        field_class = wait.until(
            lambda d, fid=field_id: d.find_element(By.ID, fid)
            .get_attribute("class")
        )
        assert "alert-success" in field_class
        assert driver.find_element(By.ID, field_id).text == expected_value


if __name__ == "__main__":
    pytest.main(["-v", __file__])
