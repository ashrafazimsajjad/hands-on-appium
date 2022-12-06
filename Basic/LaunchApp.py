from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Part 1 "Desired Capabilities"

desired_caps = {
                'platformName': 'Android',
                'automationName': 'UiAutomator2',
                'platformVersion': '11',
                'deviceName': 'samsung SM-M015G',
                'app': '/home/sajjad/Downloads/Android_Demo_App.apk',
                'appPackage': 'com.code2lead.kwad',
                'appActivity': 'com.code2lead.kwad.MainActivity'
                }
# Part 2 "WebDriver object"

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

#Part 3 "Action on the app"
# driver.find_element("").click()
ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()