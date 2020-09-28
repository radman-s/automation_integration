from selenium.webdriver.common.by import By
from .locator import Locator
from .base_page import BasePage
from .base_element import BaseElement

class GmailPage(BasePage):

    url = 'https://www.google.com/'

    @property
    def g_login_button(self):
        locator = Locator(By.XPATH,'//div[text()="Přihlaste se"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def g_user_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="identifierId"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def g_next(self):
        locator = Locator(By.XPATH, '//span[text()="Další"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def g_pw_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="password"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def g_confirm_button(self):
        locator = Locator(By.XPATH, '(//span[@class="CwaK9"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def gmail_button(self):
        locator = Locator(By.XPATH, '(//div[@class="gb_h gb_i"])[1]')
        return BaseElement(driver=self.driver, locator=locator)


