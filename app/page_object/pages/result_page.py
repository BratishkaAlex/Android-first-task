from selenium.webdriver.common.by import By

from app.page_object.forms.result_navigation_menu import ResultNavigationMenu
from app.page_object.forms.video_list_form import VideoListForm
from framework.base.base_page import BasePage


class ResultPage(BasePage):
    def __init__(self):
        super().__init__(By.XPATH, "//android.view.View[@resource-id='msd']")
        self.__result_navigation_menu = ResultNavigationMenu()
        self.__video_list_form = VideoListForm()

    @property
    def result_navigation_menu(self):
        return self.__result_navigation_menu

    @property
    def video_list_form(self):
        return self.__video_list_form
