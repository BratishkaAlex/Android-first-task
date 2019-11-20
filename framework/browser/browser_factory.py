import sys

from appium import webdriver

from resources import config


def get_remote_driver() -> webdriver:
    return webdriver.Remote(
        command_executor=f"http://{config.REMOTE_DRIVER_HUB}:{config.REMOTE_DRIVER_PORT}/wd/hub",
        desired_capabilities=get_base_capabilities())


def get_base_capabilities() -> dict:
    return {
        "platformName": config.PLATFORM,
        "deviceName": sys.argv[-1],
        "browserName": config.BROWSER_NAME
    }
