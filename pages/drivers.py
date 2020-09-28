from selenium import webdriver

class Drivers:

    def __init__(self, argument):
        self.argument = argument


    def chrome(self):
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument(self.argument)
        driver = webdriver.Chrome(options=options)
        return driver

    def firefox(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        return driver


