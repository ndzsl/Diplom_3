from selenium.webdriver.common.by import By


class LoginPageLocators:
    PASSWORD_RECOVERY_BUTTON = By.XPATH, ".//a[contains(text(), 'Восстановить пароль')]"
    LOGIN_PAGE_HEADER = By.XPATH, ".//h2[text()='Вход']"
    EMAIL_INPUT_FIELD = By.XPATH, ".//label[text() = 'Email']/following-sibling::input"
    PASSWORD_INPUT_FIELD = By.XPATH, ".//input[@name = 'Пароль']"
    LOGIN_BUTTON = By.XPATH, ".//button[text() = 'Войти']"
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    RECOVERY_BUTTON = By.XPATH, ".//button[text()='Восстановить']"