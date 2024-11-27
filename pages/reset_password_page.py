import allure
from pages.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePage):

    @allure.step('Waiting page to be loaded')
    def wait_page_loading(self):
        self.wait_for_element_hide(ResetPasswordPageLocators.OVERLAY)

    @allure.step('Press on password input field')
    def press_password_input_field(self):
        self.wait_page_loading()
        self.click_on_element_with_wait(ResetPasswordPageLocators.PASSWORD_INPUT_FIELD)

    @allure.step('Get active password field attribute value')
    def get_password_field_attribute(self):
        att = self.find_element_with_wait(ResetPasswordPageLocators.PASSWORD_ACTIVE_INPUT_FIELD).get_attribute('class')
        return att

    @allure.step('Wait page header loading')
    def wait_reset_password_page_header_loading(self):
        self.wait_visibility_of_element(ResetPasswordPageLocators.PASSWORD_INPUT_FIELD)