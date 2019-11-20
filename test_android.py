from app.page_object.enums.result_menu_items import ResultMenuItems
from app.page_object.pages.main_page import MainPage
from app.page_object.pages.result_page import ResultPage
from framework.browser.browser import Browser
from framework.utils.logger import Step
from resources import config


def launch_script():
    with Step(f"Launch browser and go to {config.URL}"):
        Browser().enter_url(config.URL)
        Browser().switch_to_native_app_context()
    with Step("Enter request and submit"):
        main_page = MainPage()
        assert main_page.is_page_opened()
        main_page.enter_request("a1qa")
        main_page.submit()

    with Step("Go to the video tab"):
        result_page = ResultPage()
        assert result_page.is_page_opened()
        result_page.result_navigation_menu.navigate_to(ResultMenuItems.VIDEOS)

    with Step("Click on the first video"):
        result_page.video_list_form.click_on_video_by_index(0)

    with Step("Close browser"):
        Browser().quit()


launch_script()
