import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    @allure.step('Click on "Password recovery" button')
    def click_on_recovery_password_button(self):
        self.click_on_element_with_wait(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Wait of "Recovery Button" visibility')
    def wait_visibility_of_recovery_button(self):
        self.find_element_with_wait(LoginPageLocators.RECOVERY_BUTTON)

    @allure.step('Wait Login page loaded')
    def wait_till_login_page_loaded(self):
        self.wait_for_element_hide(LoginPageLocators.OVERLAY)
        self.wait_visibility_of_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Set email')
    def set_email(self, email):
        self.send_text_to_element(LoginPageLocators.EMAIL_INPUT_FIELD, email)

    @allure.step('Set password')
    def set_password(self, password):
        self.send_text_to_element(LoginPageLocators.PASSWORD_INPUT_FIELD, password)

    @allure.step('Fill authorization fields')
    def fill_authorization_fields_then_login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.wait_till_login_page_loaded()
        self.click_on_element_with_wait(LoginPageLocators.LOGIN_BUTTON)