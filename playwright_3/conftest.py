import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="selection browser"
    )


@pytest.fixture(scope='function')
def user_cred(request):
    return request.param



@pytest.fixture(scope="function")
def playwright():
    with sync_playwright() as p:
        yield p