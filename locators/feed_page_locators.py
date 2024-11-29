from selenium.webdriver.common.by import By


class FeedPageLocators:
    FEED_PAGE_HEADER = By.XPATH, ".//h1[text()='Лента заказов']"
    FIRST_ORDER_IN_LIST = By.XPATH, ".//div[contains(@class, 'OrderHistory_textBox')]//p[contains(@class, 'text_type_digits')]"
    ORDER_DETAIL_WINDOW = By.XPATH, ".//div[contains(@class, 'Modal_orderBox')]"
    FIRST_ORDER_ID = By.XPATH, ".//p[contains(@class, 'text_type_digits')][1]"
    ORDER_LIST = By.XPATH, ".//div[contains(@class, 'OrderHistory_textBox')]//p[contains(@class, 'text_type_digits')]"
    ALL_TIME_COMPLETED_ORDERS = By.XPATH, ".//*[text()='Выполнено за все время:']/parent::div/p[2]"
    TODAY_COMPLETED_ORDERS = By.XPATH, ".//*[text()='Выполнено за сегодня:']/parent::div/p[2]"
    ORDERS_AT_WORK = By.XPATH, ".//ul[contains(@class, 'orderListReady')]/li[contains(@class, 'default mb-2')]"
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    ORDER_FEED = By.XPATH, ".//p[text()='Лента Заказов']"
    ORDER_STATUS_LOADING_IMG = By.XPATH, ".//img[contains(@class, 'Modal_modal__loading')]"
    ORDER_ID = By.XPATH, ".//h2[contains(@class,'title_shadow')]"