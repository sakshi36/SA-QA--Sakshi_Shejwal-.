from playwright.sync_api import expect

from .inventory import InventoryPage


class LoginPage:
    def __init__(self,page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login_cred(self, userName, userPassword):
        self.page.get_by_placeholder("Username").fill(userName)
        self.page.locator("#password").fill(userPassword)
        self.page.get_by_role("button", name="Login").click()



