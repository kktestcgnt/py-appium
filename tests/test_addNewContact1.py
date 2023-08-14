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


def test_add_contact1():
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', mobile_data)
    driver.implicitly_wait(5)
    el1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Create contact")
    el1.click()
    el2 = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[2]")
    el2.click()
    el3 = driver.find_element(By.ID,"com.samsung.android.app.contacts:id/nameEdit")
    el3.send_keys("asdf1234567890")
    el5 = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.TextView")
    el5.click()
    el8 = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.EditText");
    el8.send_keys("1122334455")
    el9 = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc=\"Save\"]/android.view.ViewGroup")
    el9.click()
