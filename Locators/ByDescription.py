from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
                'platformName': 'Android',
                'automationName': 'UiAutomator2',
                'platformVersion': '11',
                'deviceName': 'samsung SM-M015G',
                'app': '/home/sajjad/Downloads/Android_Demo_App.apk',
                'appPackage': 'com.code2lead.kwad',
                'appActivity': 'com.code2lead.kwad.MainActivity'
                }

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

ele_index = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().description("Btn3")')
ele_index.click()