from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, ".//p[text()='Личный Кабинет']"
    ORDER_FEED = By.XPATH, ".//p[text()='Лента Заказов']"
    CONSTRUCTOR_BUTTON = By.XPATH, ".//p[text()='Конструктор']"
    MAKE_ORDER_BUTTON = By.XPATH, ".//button[text()='Оформить заказ']"
    CONSTRUCTOR_HEADER = By.XPATH, "'.//*[text()='Соберите бургер']'"
    ORDER_FEED_HEADER = By.XPATH, ".//h1[text()='Лента заказов']"
    FIRST_INGREDIENT = By.XPATH, ".//a[contains(@href, '/ingredient/') and @draggable='true'][1]"
    INGREDIENT_DETAIL_WINDOW = By.XPATH, ".//*[contains(@class, 'Modal_modal_opened')]"
    CLOSE_INGREDIENT_DETAIL_WINDOW_BUTTON = By.XPATH, ".//button[contains(@class, 'Modal_modal__close__TnseK')]"
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    BASKET = By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket')]"
    INGREDIENT_COUNTER = By.XPATH, ".//p[contains(@class, 'counter_counter__num')]"
    ORDER_ID = By.XPATH, "//h2[contains(@class,'title_shadow')]"
    ORDER_STATUS_LOADING_IMG = By.XPATH, './/img[contains(@class, "Modal_modal__loading")]'
    CLOSE_ORDER_DETAIL_WINDOW_BUTTON = By.XPATH, ".//button[contains(@class, 'Modal_modal__close_modified')]"
    ORDER_HISTORY_BUTTON = By.XPATH, ".//a[text()='История заказов']"