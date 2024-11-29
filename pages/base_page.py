import allure
import data
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop


class BasePage:

    @allure.step('Driver initialization')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Page loading')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('Getting current Url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Finding element on page with waiting')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, data.SetupData.WAIT_TIME).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Click on element')
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step('Click on element with waiting')
    def click_on_element_with_wait(self, locator):
        WebDriverWait(self.driver, data.SetupData.WAIT_TIME).until(EC.element_to_be_clickable(locator))
        self.click_on_element(locator)

    @allure.step('Set text to import field')
    def send_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @allure.step('Wait visibility of element')
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, data.SetupData.WAIT_TIME).until(EC.visibility_of_element_located(locator))

    @allure.step('Get attribute value of element')
    def get_attribute_value(self, locator, attribute):
        element = self.find_element_with_wait(locator)
        attribute_value = element.get_attribute(attribute)
        return attribute_value

    @allure.step('Try to find element')
    def try_to_find_element(self, locator):
        try:
            self.find_element_with_wait(locator)
            return True
        except TimeoutException:
            return False

    @allure.step('Wait until element become invisible')
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, data.SetupData.WAIT_TIME).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Drop ingredient into basket')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step('Get element text')
    def get_element_text(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step('Get elements list')
    def get_list_of_elements(self, locator):
        return WebDriverWait(self.driver, data.SetupData.WAIT_TIME).until(EC.presence_of_all_elements_located(locator))