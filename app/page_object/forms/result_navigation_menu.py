from selenium.webdriver.common.by import By

from app.page_object.enums.result_menu_items import ResultMenuItems
from framework.elements.button import Button


class ResultNavigationMenu:
    def navigate_to(self, item: ResultMenuItems):
        self.get_menu_item(item).wait_and_click()

    def get_menu_item(self, item: ResultMenuItems) -> Button:
        return Button(By.XPATH, f"//android.view.View[@text='{item.value}']", f"Navigate to {item.value}")
