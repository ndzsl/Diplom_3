import pytest
import data
import helpers
from api_shop import ApiShop
from selenium import webdriver
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.personal_account_page import PersonalAccountPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(data.Url.MAIN_URL)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(data.Url.MAIN_URL)
    yield driver
    driver.quit()


@pytest.fixture
def create_user():
    user_data = helpers.generate_user_data()
    user_creation = ApiShop.create_user(user_data)
    token = user_creation.json()['accessToken']
    yield [user_data, user_data["email"], user_data["password"], token]
    ApiShop.delete_user(token)


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.get_url(data.Url.MAIN_URL)

    return page


@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.get_url(f'{data.Url.MAIN_URL}{data.Url.LOGIN_PAGE}')
    return page


@pytest.fixture
def forgot_password_page(driver):
    return ForgotPasswordPage(driver)


@pytest.fixture
def reset_password_page(driver):
    return ResetPasswordPage(driver)


@pytest.fixture
def personal_account_page(driver):
    return PersonalAccountPage(driver)


@pytest.fixture
def feed_page(driver):
    return FeedPage(driver)


@pytest.fixture
def authorization_by_new_user(main_page, login_page, personal_account_page, create_user):
    main_page.main_page_loading_wait()
    main_page.press_personal_account_button()
    login_page.wait_till_login_page_loaded()
    login_page.fill_authorization_fields_then_login(create_user[1], create_user[2])
    main_page.press_personal_account_button()
    personal_account_page.wait_till_pa_page_loaded()