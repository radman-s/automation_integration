from selenium.webdriver.common.by import By
from .locator import Locator
from .base_page import BasePage
from .base_element import BaseElement


class YahooPage(BasePage):

    url = 'https://uk.yahoo.com/'

    @property
    def egree(self):
        locator = Locator(By.CSS_SELECTOR, 'button[name="agree"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sign_in_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="header-signin-link"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def login_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="login-username"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def next_button1(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="login-signin"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def next_button2(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="login-signin"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def pw_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="login-passwd"]')
        return BaseElement(driver=self.driver, locator=locator)

