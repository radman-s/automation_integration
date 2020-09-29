from selenium.webdriver.common.by import By
from .locator import Locator
from .base_page import BasePage
from .base_element import BaseElement

class AolMailPage(BasePage):
    # user_aol = 'test.integrate_30100'
    # pw_aol = '123852_pw'

    url = 'https://login.aol.com/'
    #
    # url = 'https://test.integrate_30100:123852_pw@www.aol.com/'

    @property
    def aol_user_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="login-username"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def user_next_button(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="login-signin"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def aol_pw_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="login-passwd"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def pw_next_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="login-signin"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def mail_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[title="email link"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def compose_button(self):
        locator = Locator(By.XPATH, '//div[text()="Compose"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def to_input(self):
        locator = Locator(By.CSS_SELECTOR, 'textarea[id="toInputField"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def subject_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="Subject"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def message_input(self):
        locator = Locator(By.CSS_SELECTOR, 'div[name="composeMessage_body_body"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def send_button(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="uniqName_4_4"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sent_button(self):
        locator = Locator(By.XPATH, '//span[text()="Sent"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def aol_select_email(self):
        locator = Locator(By.XPATH, '(//table[@class="dojoxGrid-row-table"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def aol_text_subject(self):
        locator = Locator(By.CSS_SELECTOR, 'span[class="subject"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def aol_text_to(self):
        locator = Locator(By.XPATH, '(//span[@class="address wsItem"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def aol_text_msg(self):
        locator = Locator(By.CSS_SELECTOR, 'div[style="font:10pt Helvetica Neue;"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def aol_date_time(self):
        locator = Locator(By.XPATH, '//div[@class="fullDateField"]/span')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def aol_delete(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="uniqName_4_45"]')
        return BaseElement(driver=self.driver, locator=locator)

