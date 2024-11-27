import allure
from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):

    @allure.step('Wait Recover button loading')
    def wait_recover_button_loading(self):
        self.find_element_with_wait(ForgotPasswordPageLocators.RECOVERY_BUTTON)

    @allure.step('Wait till Page load')
    def wait_till_forgot_password_page_load(self):
        self.wait_for_element_hide(ForgotPasswordPageLocators.OVERLAY)

    @allure.step('Fill email input field')
    def fill_email_field(self, email):
        self.wait_visibility_of_element(ForgotPasswordPageLocators.EMAIL_INPUT_FIELD)
        self.send_text_to_element(ForgotPasswordPageLocators.EMAIL_INPUT_FIELD, email)

    @allure.step('Press on "Recover button')
    def press_recover_button(self):
        self.click_on_element_with_wait(ForgotPasswordPageLocators.RECOVERY_BUTTON)