from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    PROFILE_BUTTON = By.XPATH, ".//a[text()='Профиль']"
    ORDER_HISTORY_BUTTON = By.XPATH, ".//a[text()='История заказов']"
    EXIT_BUTTON = By.XPATH, ".//button[text()='Выход']"
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"