import allure
import data


class TestPersonalAccountPage:

    @allure.title('Successful switch to Personal Account Page by click on Personal Account button on main page')
    def test_switch_to_personal_account_page(self, create_user, main_page, login_page, personal_account_page):
        main_page.press_personal_account_button()
        login_page.wait_till_login_page_loaded()
        login_page.fill_authorization_fields_then_login(create_user[1], create_user[2])
        main_page.press_personal_account_button()
        personal_account_page.wait_till_pa_page_loaded()
        assert personal_account_page.get_current_url() == f'{data.Url.MAIN_URL}{data.Url.PERSONAL_ACCOUNT_PAGE}'

    @allure.title('Successful switch to Order History section')
    def test_switch_to_order_history_section(self, authorization_by_new_user, personal_account_page):
        personal_account_page.wait_till_pa_page_loaded()
        personal_account_page.press_order_history_button()
        personal_account_page.wait_till_pa_page_loaded()
        assert personal_account_page.get_current_url() == f'{data.Url.MAIN_URL}{data.Url.ORDER_HISTORY_PAGE}'

    @allure.title('Successful exit from Personal Account')
    def test_exit_from_personal_account(self, authorization_by_new_user, personal_account_page, login_page):
        personal_account_page.wait_till_pa_page_loaded()
        personal_account_page.press_exit_button()
        login_page.wait_till_login_page_loaded()
        assert personal_account_page.get_current_url() == f'{data.Url.MAIN_URL}{data.Url.LOGIN_PAGE}'