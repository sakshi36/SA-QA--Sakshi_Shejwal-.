import json

import pytest
from playwright.sync_api import Playwright, expect

from playwright_3.pageObjectModel.login import LoginPage

with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_list = test_data['user_credentials']


@pytest.mark.parametrize('user_cred',user_list)
def test_UI(playwright: Playwright, user_cred):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    userName = user_cred['username']
    userPassword = user_cred['password']
    login_page = LoginPage(page)
    login_page.navigate()
    inventoryPage = login_page.login_cred(userName, userPassword)
    # inventory
    inventoryPage.add_orders()

    # grap the error message


    page.locator("#first-name").fill("John")
    page.get_by_placeholder("Last Name").fill("Sweety")
    page.locator("#postal-code").fill("412104")
    page.get_by_role("button", name="Continue").click()

    # order history page
    card_items = page.locator(".cart_item")
    assert card_items.count() == 2
    print(f"Checkout contains {card_items.text_content()} items")
    page.click('[data-test="finish"]')
    # verify order confirmation
    order_placed = page.get_by_text("Thank you for your order!")
    expect(order_placed).to_contain_text("Thank you")
    print(f"Displays message {order_placed}")
    page.wait_for_timeout(3000)
    # ================================================================
    print("\n🔹 Starting Negative Path Test")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("locked_out_user")
    page.locator("#password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    # Verify locked out error
    error = page.locator("h3[data-test='error']")
    expect(error).to_be_visible()
    assert "locked out" in error.text_content().lower()
    print("❌ Error shown for locked_out_user:", error.text_content())

    context.close()
    browser.close()