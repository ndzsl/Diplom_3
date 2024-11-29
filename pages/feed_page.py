import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):

    @allure.step('Wait feed page loading')
    def wait_page_loading(self):
        self.wait_for_element_hide(FeedPageLocators.OVERLAY)
        self.wait_visibility_of_element(FeedPageLocators.FEED_PAGE_HEADER)

    @allure.step('Click on first order in orders list')
    def click_on_order_in_order_list(self):
        self.wait_page_loading()
        self.click_on_element_with_wait(FeedPageLocators.FIRST_ORDER_IN_LIST)

    @allure.step('Check visibility of order detail window')
    def order_detail_window_check(self):
        result = self.try_to_find_element(FeedPageLocators.ORDER_DETAIL_WINDOW)
        return result

    @allure.step('Get order id from history')
    def get_order_id(self):
        self.wait_for_element_hide(FeedPageLocators.OVERLAY)
        result = self.get_list_of_elements(FeedPageLocators.FIRST_ORDER_IN_LIST)[0].text
        return result

    @allure.step('Click "Order Feed" button')
    def click_order_feed_button(self):
        self.wait_for_element_hide(FeedPageLocators.OVERLAY)
        self.click_on_element_with_wait(FeedPageLocators.ORDER_FEED)

    @allure.step('Get Orders Numbers List')
    def get_order_numbers_list(self):
        self.wait_for_element_hide(FeedPageLocators.OVERLAY)
        element = self.get_list_of_elements(FeedPageLocators.ORDER_LIST)
        order_id = [element.text for element in element]
        return order_id

    @allure.step('Get count of all time completed orders')
    def get_count_all_time_completed_orders(self):
        result = self.get_element_text(FeedPageLocators.ALL_TIME_COMPLETED_ORDERS)
        return result

    @allure.step('Get count of today completed orders')
    def get_count_today_completed_orders(self):
        result = self.get_element_text(FeedPageLocators.TODAY_COMPLETED_ORDERS)
        return result

    @allure.step('Get order id in progress list')
    def get_order_id_in_progress_list(self):
        self.find_element_with_wait(FeedPageLocators.ORDERS_AT_WORK)
        result = self.get_element_text(FeedPageLocators.ORDERS_AT_WORK)
        return result

    @allure.step('Get fresh order id')
    def get_fresh_order_id(self):
        self.wait_for_element_hide(FeedPageLocators.ORDER_STATUS_LOADING_IMG)
        result = self.get_element_text(FeedPageLocators.ORDER_ID)
        return f'0{result}'