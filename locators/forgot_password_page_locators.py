from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    RECOVERY_BUTTON = By.XPATH, ".//button[text()='Восстановить']"
    PASSWORD_RECOVERY_HEADER = By.XPATH, ".//h2[text()='Восстановление пароля']"
    EMAIL_INPUT_FIELD = By.XPATH, ".//label[text() = 'Email']/following-sibling::input"
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"