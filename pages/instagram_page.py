from selenium.webdriver.common.by import By
from .locator import Locator
from .base_page import BasePage
from .base_element import BaseElement

class InstagramPage(BasePage):

    url = 'https://www.instagram.com/'

    @property
    def ig_user_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="username"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def ig_pw_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="password"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def ig_login_button(self):
        locator = Locator(By.XPATH, '//div[text()="Log In"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def ig_notnow_button(self):
        locator = Locator(By.XPATH, '//button[text()="Not Now"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def profile_link(self):
        locator = Locator(By.XPATH, '//div[@class="SKguc"]/a')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def image(self):
        locator = Locator(By.CSS_SELECTOR, 'div[class="eLAPa"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def menu_button(self):
        locator = Locator(By.XPATH, '//div[@class="MEAGs"]/button')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def share_button(self):
        locator = Locator(By.XPATH, '//button[text()="Share"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def share_fb_button(self):
        locator = Locator(By.XPATH, '//div[text()="Share to Facebook"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def email_fb_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="email"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def pw_fb_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="pass"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def login_fb_button(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="login"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def comment_img(self):
        locator = Locator(By.CSS_SELECTOR, 'textarea[name="xhpc_message_text"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def text_image(self):
        locator = Locator(By.CSS_SELECTOR, 'div[class="unclickableMask"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def post_fb_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="u_0_23"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def close_share(self):
        locator = Locator(By.XPATH, '//div[@class="WaOAr"]/button')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def close_image(self):
        locator = Locator(By.XPATH, '(//button[@class="wpO6b "])[7]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def setting_button(self):
        locator = Locator(By.XPATH, '//div[@class="AFWDX"]/button')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def logout_button(self):
        locator = Locator(By.XPATH, '//button[text()="Log Out"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def emails_ig_button(self):
        locator = Locator(By.XPATH, '//button[text()="Emails from Instagram"]')
        return BaseElement(driver=self.driver, locator=locator)


