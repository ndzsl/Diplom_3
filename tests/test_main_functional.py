import allure
import data


class TestMainFunctional:

    @allure.title('Successful switch to constructor section')
    def test_switch_to_constructor(self, main_page):
        main_page.press_constructor_button()
        assert main_page.get_current_url() == f'{data.Url.MAIN_URL}'

    @allure.title('Successful switch to order feed section')
    def test_switch_to_order_feed_section(self, main_page):
        main_page.press_order_feed_button()
        main_page.main_page_loading_wait()
        assert main_page.get_current_url() == f'{data.Url.MAIN_URL}{data.Url.ORDER_FEED_SECTION}'

    @allure.title('Successful open of ingredient detail window')
    def test_open_ingredient_detail_window(self, main_page):
        main_page.click_on_first_constructor_ingredient()
        result = main_page.ingredient_detail_window_check()
        assert result == True

    @allure.title('Successful close of ingredient detail window by click on "X" button')
    def test_close_ingredient_detail_window(self, main_page):
        main_page.click_on_first_constructor_ingredient()
        main_page.close_ingredient_detail_window()
        result = main_page.ingredient_detail_window_check()
        assert result == False

    @allure.title('Successful increased ingredient count after dragging')
    def test_ingredient_count_increasing_success(self, main_page):
        main_page.main_page_loading_wait()
        main_page.put_ingredient_into_basket()
        result = main_page.get_ingredient_count()
        assert result == data.StaticData.INGREDIENT_COUNT

    @allure.title('Successful order creation by authorized user')
    def test_order_creation_success(self, main_page, authorization_by_new_user):
        main_page.main_page_loading_wait()
        main_page.set_ingredient_and_make_order()
        result = main_page.get_order_id()
        assert result != data.StaticData.DEFAULT_ORDER_ID