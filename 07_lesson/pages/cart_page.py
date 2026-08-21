from selenium.webdriver.common.by import By


class CartPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")
    ITEM_COUNT = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def get_item_count(self):
        return self.driver.find_element(*self.ITEM_COUNT).text

    def checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
