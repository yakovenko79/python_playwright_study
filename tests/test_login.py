import allure
import pytest


@allure.feature('Авторизаци')
@allure.story('Авторизации недействительные учетные данные')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизаиця с недействительными учетными данными')
def test_login_failure(login_page):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page.login('invalid_user', 'invalid_password')
    with allure.step('Url не изменился'):
        assert login_page.page.url == 'https://zimaev.github.io/pom/'
    with allure.step('Отображается ошибка - Invalid credentials. Please try again.'):
        assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


@allure.feature('Login')
@allure.story('Авторизации существующие учетные данные')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Авторизаиця с валидными учетными данными')
@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin'),

])
def test_login_success(login_page, username, password, dashboard_page):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page.login(username, password)
    with allure.step('Отображается приветственное сообщение с именем пользователя'):
        dashboard_page.assert_welcome_messsage(f"Welcome {username}")
