import pytest
from appium.webdriver.appium_service import AppiumService


@pytest.fixture
def start_appium_server():
    appium_service = AppiumService()
    appium_service.start()
    yield
    appium_service.stop()