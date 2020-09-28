from selenium.webdriver.common.by import By
from .locator import Locator
from .base_page import BasePage
from .base_element import BaseElement

class FacebookPage(BasePage):

    url = 'https://www.facebook.com/'

    @property
    def fb_user_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="email"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def fb_pw_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="pass"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def fb_login_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="u_0_d"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def profile_button(self):
        locator = Locator(By.XPATH, '(//span[@class="a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def img_name(self):
        locator = Locator(By.XPATH, '//div[@class="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q"]/div')
        return BaseElement(driver=self.driver, locator=locator)

