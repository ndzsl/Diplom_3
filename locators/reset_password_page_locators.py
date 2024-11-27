from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    SAVE_BUTTON = By.XPATH, ".//button[text()='Сохранить']"
    PASSWORD_INPUT_FIELD = By.XPATH, ".//label[text()='Пароль']"
    PASSWORD_ACTIVE_INPUT_FIELD = By.XPATH, ".//fieldset[1]/div/div"
    RESET_PASSWORD_PAGE_HEADER = By.XPATH, ".//h2[text()='Восстановление пароля']"
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"