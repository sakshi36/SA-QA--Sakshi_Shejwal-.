from .inventory import InventoryPage


class UserDetails:
    def __init__(self, page):
        self.page = page

    def create_user_details(self):
        self.page.locator("#first-name").fill("John")
        self.page.get_by_placeholder("Last Name").fill("Sweety")
        self.page.locator("#postal-code").fill("412104")
        self.page.get_by_role("button", name="Continue").click()
