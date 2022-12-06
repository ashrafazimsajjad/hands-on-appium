from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_caps = {
                'platformName': 'Android',
                'automationName': 'UiAutomator2',
                'platformVersion': '11',
                'deviceName': 'samsung SM-M015G',
                'app': '/home/sajjad/Downloads/Android_Demo_App.apk',
                'appPackage': 'com.code2lead.kwad',
                'appActivity': 'com.code2lead.kwad.MainActivity'
                }

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

ele_xpath = driver.find_element(AppiumBy.XPATH,
                                '//android.widget.Button[@content-desc="Btn1"]')  # By using xpath and Con-des
# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]') #Xpath and Res-id
# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@text="ENTER SOME VALUE"]') #Xpath and text
# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[3]') #xpath and Index value
ele_xpath.click()

time.sleep(2)

ele_xpath2 = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText')
ele_xpath2.send_keys("Value Entered")

time.sleep(2)

driver.quit()
