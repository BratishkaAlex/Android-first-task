from appium import webdriver

from framework.browser.browser_factory import get_remote_driver
from framework.models.singleton import Singleton
from framework.utils.logger import debug


class Browser(metaclass=Singleton):
    def __init__(self):
        self.__driver = get_remote_driver()

    @property
    def driver(self) -> webdriver:
        return self.__driver

    def enter_url(self, url: str):
        debug(f"Entering {url}")
        self.driver.get(url)

    def switch_to_native_app_context(self):
        self.driver.switch_to.context('NATIVE_APP')

    def switch_to_default_context(self):
        self.driver.switch_to.context('WEB_VIEW')

    def quit(self):
        self.driver.quit()
