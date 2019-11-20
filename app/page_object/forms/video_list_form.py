from selenium.webdriver.common.by import By

from framework.elements.button import Button


class VideoListForm:
    def click_on_video_by_index(self, index: int):
        self.get_video_by_index(index).wait_and_click()

    def get_video_by_index(self, index: int) -> Button:
        return Button(By.XPATH, f"//android.view.View[@resource-id='rso']/android.view.View[@index='{index}']",
                      "Video by index")
