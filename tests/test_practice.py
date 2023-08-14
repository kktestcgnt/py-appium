import pytest
import time
from appium import webdriver
from appium.webdriver.appium_service import AppiumService

mobile_device = dict(
    deviceName='Android',
    platformName='Android',
    browserName='Chrome'
)


def test_one():
    appium_service = AppiumService()
    appium_service.start()
    print(appium_service.is_running)
    print(appium_service.is_listening)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', mobile_device)
    driver.get("http://google.com")
    time.sleep(25)
