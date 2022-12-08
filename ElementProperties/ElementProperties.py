from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '11',
                'automationName': 'UiAutomator2',
                'deviceName': 'samsung SM-M015G',
                'app': '/home/sajjad/Downloads/Android_Demo_App.apk',
                'appPackage': 'com.code2lead.kwad',
                'appActivity': 'com.code2lead.kwad.MainActivity'
                }

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

element = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")

print("Is Displayed : ", element.is_displayed())
print("Is Enabled : ", element.is_enabled())
print("Is selected : ", element.is_selected())
print("Size : ", element.size)
print("Location : ", element.location)