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

element = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")

for x in element:
    print(x.text)

for x in element:
    button = x.text
    if button == "ScrollView":
        x.click()
        break

time.sleep(2)
driver.quit()