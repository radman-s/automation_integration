from selenium.webdriver.common.by import By
from .locator import Locator
from .base_page import BasePage
from .base_element import BaseElement

class SeznamPage(BasePage):

    url = 'https://www.seznam.cz/'

    @property
    def s_user_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="username"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def s_pw_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="password"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def s_toemail_button(self):
        locator = Locator(By.XPATH, '//button[text()="Přejít do Emailu"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def s_select_email(self):
        locator = Locator(By.CSS_SELECTOR, 'a[title="test.integrate_30100@aol.com"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def s_text_from(self):
        locator = Locator(By.CSS_SELECTOR, 'button[class="popup vcard plain compact"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def s_text_to(self):
        locator = Locator(By.XPATH, '//dd/div')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def s_text_subject(self):
        locator = Locator(By.XPATH, '//h2[@lang="un"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def s_text_msg(self):
        locator = Locator(By.XPATH, '//div[@class="body apply-styles"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def s_date_time(self):
        locator = Locator(By.CSS_SELECTOR, 'span[class="date noprint"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def s_delete_mail(self):
        locator = Locator(By.XPATH, '(//button[@data-command="misc:trash"])[1]')
        return BaseElement(driver=self.driver, locator=locator)