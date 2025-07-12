from playwright.sync_api import expect



class InventoryPage:
    def __init__(self, page):
        self.page = page

    def add_orders(self):
        labs = self.page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")
        labs.get_by_role("button").click()
        onesie = self.page.locator(".inventory_item").filter(has_text="Sauce Labs Onesie")
        onesie.get_by_role("button").click()
        self.page.locator(".shopping_cart_link").click()
        self.page.locator("button[name='checkout']").click()

    def grap_error_message(self):
        self.page.get_by_role("button", name="Continue").click()
        error_message = self.page.get_by_text("Error: First Name is required")
        expect(error_message).to_be_visible()
        print(f"When user do not give inputs displays {error_message.text_content()}")
