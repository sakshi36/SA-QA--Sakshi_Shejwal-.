import json

import pytest
from playwright.sync_api import Playwright, expect

from pageObjectModel.inventory import InventoryPage
from pageObjectModel.login import LoginPage
from pageObjectModel.orderHistorypage import OrderHistory
from pageObjectModel.userDetailPage import UserDetails

with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_list = test_data['user_credentials']


@pytest.mark.order(1)
@pytest.mark.parametrize('user_cred',[
    cred for cred in user_list if cred['username'] != 'locked_out_user'])
def test_UI(playwright: Playwright, user_cred):
    print("\n Starting Happy Path Test")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir="videos1/")
    page = context.new_page()
    userName = user_cred['username']
    userPassword = user_cred['password']
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_cred(userName, userPassword)
    # inventory
    inventoryPage = InventoryPage(page)
    inventoryPage.add_orders()
    # grap the error message
    inventoryPage.grap_error_message()
    user_page = UserDetails(page)
    user_page.create_user_details()

    # order history page
    order_page = OrderHistory(page)
    order_page.order_track()
    context.close()
    browser.close()
    # ================================================================



@pytest.mark.order(2)
@pytest.mark.parametrize('user_cred',[
    cred for cred in user_list if cred['username'] == 'locked_out_user'])
def test_locked_out_user(playwright: Playwright, user_cred):
    print("\n Starting Negative Path Test")

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir="videos2/")
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    userName = user_cred['username']
    userPassword = user_cred['password']
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_cred(userName, userPassword)

    # Verify locked out error
    error = page.locator("//div[@class='error-message-container error']")
    expect(error).to_be_visible()
    print(error.text_content())
    context.close()
    browser.close()
    pytest.exit("Negative test run completed — exiting test suite.")