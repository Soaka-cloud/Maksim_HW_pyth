from selenium.webdriver.common.by import By


class InventoryPage:
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, item_id):
        self.driver.find_element(
            By.ID, f"add-to-cart-{item_id}"
        ).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
