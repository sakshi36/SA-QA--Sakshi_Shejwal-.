from playwright.sync_api import expect

from .userDetailPage import UserDetails


class OrderHistory:
    def __init__(self, page):
        self.page = page

    def order_track(self):
        card_items = self.page.locator(".cart_item")
        item_count = card_items.count()
        assert item_count == 2
        print(f"Checkout contains {item_count} items")
        self.page.click('[data-test="finish"]')
        # verify order confirmation
        order_placed = self.page.get_by_text("Thank you for your order!")
        expect(order_placed).to_contain_text("Thank you")
        print(f"Displays message {order_placed.text_content()}")
        self.page.wait_for_timeout(3000)

