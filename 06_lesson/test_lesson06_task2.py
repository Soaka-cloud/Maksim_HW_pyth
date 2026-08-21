from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()

    try:
        driver.get("https://gitflic.ru/")

        sessionid_user1 = (
            "3:1787293435.5.0.1708266561009:dD6lLg:ce.1.2:1|1008284233.-1.2.3:"
            "1708266561.6:2162771413.7:1784312624|3:12128128.475976."
            "0q2EAD3YBB2x6qrGX-H9gXy1gWA"
        )
        driver.add_cookie({
            "name": "sessionid",
            "value": sessionid_user1
        })
        driver.add_cookie({
            "name": "csrftoken",
            "value": "a1105099-9980-4572-bc4c-d1334eb9bc18"
        })

        driver.refresh()
        driver.get("https://gitflic.ru/user/soaka01")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        url_user_1 = driver.current_url
        print(f"URL пользователя 1: {url_user_1}")

        driver.delete_all_cookies()
        driver.refresh()

        sessionid_user2 = (
            "3:1787293435.5.0.1708266561009:dD6lLg:ce.1.2:1|1008284233.-1.2.3:"
            "1708266561.6:2162771413.7:1784312624|3:12128128.475976."
            "0q2EAD3YBB2x6qrGX-H9gXy1gWA"
        )
        driver.add_cookie({
            "name": "sessionid",
            "value": sessionid_user2
        })
        driver.add_cookie({
            "name": "csrftoken",
            "value": "e98a0059-90a8-4c48-9fc5-8fd19be4f138"
        })

        driver.refresh()
        driver.get("https://gitflic.ru/user/soaka02")
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        url_user_2 = driver.current_url
        print(f"URL пользователя 2: {url_user_2}")

        assert url_user_1 != url_user_2, "URL профилей одинаковые"

        print("✅ Тест 2 пройден")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_session_storage_auth()
