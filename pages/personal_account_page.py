import allure
from pages.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLocators


class PersonalAccountPage(BasePage):

    @allure.step('Get page url')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('Wait page loading')
    def wait_till_pa_page_loaded(self):
        self.wait_visibility_of_element(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Wait till modal window hide')
    def wait_till_modal_window_hide(self):
        self.wait_for_element_hide(PersonalAccountPageLocators.OVERLAY)

    @allure.step('Press Order History button')
    def press_order_history_button(self):
        self.wait_till_modal_window_hide()
        self.wait_till_pa_page_loaded()
        self.click_on_element_with_wait(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Press Exit button')
    def press_exit_button(self):
        self.wait_till_pa_page_loaded()
        self.wait_till_modal_window_hide()
        self.click_on_element_with_wait(PersonalAccountPageLocators.EXIT_BUTTON)