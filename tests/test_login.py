from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


def test_login_failure(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login('invalid_user', 'invalid_password')
    assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


def test_login_success(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.navigate()
    login_page.login('admin', 'admin')

    dashboard_page.assert_welcome_messsage("Welcome admin")
