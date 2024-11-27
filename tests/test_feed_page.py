import allure


class TestFeedPage:
    @allure.title('Successful order details window display')
    def test_order_detail_window_display(self, main_page, feed_page):
        main_page.press_order_feed_button()
        feed_page.click_on_order_in_order_list()
        result = feed_page.order_detail_window_check()
        assert result == True

    @allure.title('Users order displayed in order feed list test')
    def test_users_order_displayed_in_orders_list(self, authorization_by_new_user, main_page, personal_account_page,
                                                  feed_page):
        main_page.main_page_loading_wait()
        main_page.set_ingredient_and_make_order()
        main_page.close_order_detail_window()
        main_page.press_personal_account_button()
        main_page.click_on_order_history_button()
        order_id = feed_page.get_order_id()
        feed_page.click_order_feed_button()
        order_id_list = feed_page.get_order_numbers_list()
        assert order_id in order_id_list

    @allure.title('Increased counter of all time completed orders test')
    def test_increased_all_time_completed_orders_counter(self, main_page, personal_account_page,
                                                         authorization_by_new_user, feed_page):
        main_page.press_order_feed_button()
        feed_page.wait_page_loading()
        order_count_before = feed_page.get_count_all_time_completed_orders()
        main_page.set_ingredient_and_make_order()
        main_page.close_order_detail_window()
        main_page.press_order_feed_button()
        feed_page.wait_page_loading()
        order_count_after = feed_page.get_count_all_time_completed_orders()
        assert order_count_before < order_count_after

    @allure.title('Increased counter of today completed orders test')
    def test_increased_today_completed_orders_counter(self, main_page, personal_account_page,
                                                      authorization_by_new_user, feed_page):
        main_page.main_page_loading_wait()
        main_page.press_order_feed_button()
        feed_page.wait_page_loading()
        order_count_before = feed_page.get_count_today_completed_orders()
        main_page.set_ingredient_and_make_order()
        main_page.close_order_detail_window()
        main_page.press_order_feed_button()
        feed_page.wait_page_loading()
        order_count_after = feed_page.get_count_today_completed_orders()
        assert order_count_before < order_count_after

    @allure.title('Fresh order appears in orders progress list')
    def test_check_order_id_in_progress_list(self, main_page, personal_account_page,
                                             authorization_by_new_user, feed_page):
        main_page.main_page_loading_wait()
        main_page.press_order_feed_button()
        feed_page.wait_page_loading()
        main_page.set_ingredient_and_make_order()
        main_page.order_detail_window_loading()
        order_id = feed_page.get_fresh_order_id()
        main_page.close_order_detail_window()
        main_page.press_order_feed_button()
        feed_page.wait_page_loading()
        id_list = feed_page.get_order_id_in_progress_list()
        assert order_id == id_list