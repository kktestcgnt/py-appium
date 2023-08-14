import time
from appium import webdriver
from selenium.webdriver.common.by import By

desired_cap = dict(
    deviceName='Android',
    platformName='Android',
    browserName='Chrome'
)
# print(desired_cap)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)
# to open google.com in browser
driver.get('http://google.com')
# to get the opened url link
print(driver.title)
time.sleep(13)
driver.find_element(By.XPATH,"//*[@id='tsf']/div[1]/div[1]/div[1]/div[1]/div/input").send_keys("Hai i am Krishna !!!!")
time.sleep(15)
driver.quit()
