import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

mobile_data = dict(
    deviceName='Android',
    platformName='Android',
    appPackage='com.samsung.android.dialer',
    appActivity='.DialtactsActivity'
)


def test_dialer_application():
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', mobile_data)
    time.sleep(10)
    driver.find_element(By.ID,"com.samsung.android.dialer:id/one").click()
    time.sleep(1)
    driver.find_element(By.ID,"com.samsung.android.dialer:id/two").click()
    time.sleep(1)
    driver.find_element(By.ID, "com.samsung.android.dialer:id/three").click()
    time.sleep(1)
    driver.find_element(By.ID, "com.samsung.android.dialer:id/four").click()
    time.sleep(1)
    driver.find_element(By.ID, "com.samsung.android.dialer:id/five").click()
    time.sleep(1)
    driver.find_element(By.ID, "com.samsung.android.dialer:id/callButtonContainer").click()
    time.sleep(1)
    driver.quit()
