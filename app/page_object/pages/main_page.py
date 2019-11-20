from selenium.webdriver.common.by import By

from framework.base.base_page import BasePage
from framework.elements.button import Button
from framework.elements.input_field import InputField


class MainPage(BasePage):
    def __init__(self):
        super().__init__(By.CLASS_NAME, "android.widget.Image")

    def enter_request(self, request: str):
        input_field = InputField(By.XPATH, "//android.view.View//android.widget.EditText", "Enter request")
        input_field.send_keys(request)

    def submit(self):
        Button(By.XPATH, "//android.widget.Button[@index='2']", "Submit request").click()
