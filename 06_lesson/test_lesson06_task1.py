from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    try:
        # 1. Открыть страницу
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        # 2. Найти и нажать кнопку "Start"
        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()

        # 3. Дождаться появления текста "Hello World!"
        wait = WebDriverWait(driver, 10)
        hello_text = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )

        # 4. Сделать скриншот страницы
        driver.save_screenshot("06_lesson/dynamic_loading.png")

        # 5. Проверить, что текст равен "Hello World!"
        assert hello_text.text == "Hello World!"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_dynamic_loading()
