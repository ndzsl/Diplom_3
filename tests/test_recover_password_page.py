import allure
import data


class TestRecoverPasswordPage:

    @allure.title('Successful switch to password recovery page by "Password Recovery Button"')
    def test_switch_to_password_recovery_page(self, login_page):
        login_page.wait_till_login_page_loaded()
        login_page.click_on_recovery_password_button()
        login_page.wait_visibility_of_recovery_button()
        assert login_page.get_current_url() == f'{data.Url.MAIN_URL}{data.Url.FORGOT_PASSWORD_PAGE}'

    @allure.title('Send email and press "Recover Button" then check switch to reset password page')
    def test_send_email_and_press_recover_button(self, login_page, forgot_password_page, reset_password_page,
                                                 create_user):
        login_page.click_on_recovery_password_button()
        forgot_password_page.fill_email_field(create_user[1])
        forgot_password_page.press_recover_button()
        reset_password_page.wait_reset_password_page_header_loading()
        assert reset_password_page.get_current_url() == f'{data.Url.MAIN_URL}{data.Url.RESET_PASSWORD_PAGE}'

    @allure.title('Email field becomes active test')
    def test_email_input_field_becomes_active(self, login_page, forgot_password_page, reset_password_page, create_user):
        login_page.click_on_recovery_password_button()
        forgot_password_page.fill_email_field(create_user[1])
        forgot_password_page.press_recover_button()
        reset_password_page.press_password_input_field()
        result = reset_password_page.get_password_field_attribute()
        assert data.AssertFlags.PASSWORD_FIELD_ACTIVE_STATUS in result