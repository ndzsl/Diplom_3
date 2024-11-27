import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Main page loading wait')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Order detail window loading wait')
    def order_detail_window_loading(self):
        self.wait_for_element_hide(MainPageLocators.ORDER_STATUS_LOADING_IMG)

    @allure.step('Press "Personal account" button')
    def press_personal_account_button(self):
        self.main_page_loading_wait()
        self.click_on_element_with_wait(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Press "Constructor" button')
    def press_constructor_button(self):
        self.main_page_loading_wait()
        self.click_on_element_with_wait(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Press "Order feed" button')
    def press_order_feed_button(self):
        self.main_page_loading_wait()
        self.click_on_element_with_wait(MainPageLocators.ORDER_FEED)

    @allure.step('Click on first ingredient in constructor')
    def click_on_first_constructor_ingredient(self):
        self.main_page_loading_wait()
        self.click_on_element_with_wait(MainPageLocators.FIRST_INGREDIENT)

    @allure.step('Check visibility of ingredient detail window')
    def ingredient_detail_window_check(self):
        self.main_page_loading_wait()
        return self.try_to_find_element(MainPageLocators.INGREDIENT_DETAIL_WINDOW)

    @allure.step('Close ingredient detail window')
    def close_ingredient_detail_window(self):
        self.main_page_loading_wait()
        self.click_on_element_with_wait(MainPageLocators.CLOSE_INGREDIENT_DETAIL_WINDOW_BUTTON)

    @allure.step('Put ingredient into basket')
    def put_ingredient_into_basket(self):
        self.main_page_loading_wait()
        ingredient = self.find_element_with_wait(locator=MainPageLocators.FIRST_INGREDIENT)
        basket = self.find_element_with_wait(locator=MainPageLocators.BASKET)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step('Get ingredient count')
    def get_ingredient_count(self):
        result = self.get_element_text(MainPageLocators.INGREDIENT_COUNTER)
        return result

    @allure.step('Press "Order Creation" button')
    def click_on_order_creation_button(self):
        self.main_page_loading_wait()
        self.click_on_element_with_wait(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Put ingredient into basket and make order')
    def set_ingredient_and_make_order(self):
        self.main_page_loading_wait()
        self.press_constructor_button()
        self.put_ingredient_into_basket()
        self.click_on_order_creation_button()

    @allure.step('Get created order ID')
    def get_order_id(self):
        self.main_page_loading_wait()
        self.wait_for_element_hide(MainPageLocators.ORDER_STATUS_LOADING_IMG)
        result = self.get_list_of_elements(MainPageLocators.ORDER_ID)
        return result

    @allure.step('Close Order Detail window')
    def close_order_detail_window(self):
        self.main_page_loading_wait()
        self.order_detail_window_loading()
        self.click_on_element_with_wait(MainPageLocators.CLOSE_ORDER_DETAIL_WINDOW_BUTTON)

    @allure.step('Click on "Order History" button')
    def click_on_order_history_button(self):
        self.main_page_loading_wait()
        self.click_on_element_with_wait(MainPageLocators.ORDER_HISTORY_BUTTON)