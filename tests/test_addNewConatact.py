import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

mobile_data=dict(
    deviceName="Android",
    platformName='Android',
    appPackage="com.samsung.android.app.contacts",
    appActivity='com.samsung.android.contacts.contactslist.PeopleActivity'
)

def test_add_contact():
    driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',mobile_data)
    driver.implicitly_wait(5)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Create contact").click()
    driver.find_element(By.ID,"com.samsung.android.app.contacts:id/container").click()
    driver.hide_keyboard()
    driver.find_element(By.XPATH,"//android.widget.EditText[@text='Name']").send_keys("Appium testing")
    driver.find_element(By.ID,"com.samsung.android.app.contacts:id/titleText").click()
    driver.find_element(By.ID,"com.samsung.android.app.contacts:id/flow").send_keys("1234567890")
    # driver.find_element(By.XPATH,"//android.view.View").send_keys("1234567890")
    time.sleep(10)
    driver.quit()