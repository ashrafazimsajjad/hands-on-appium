from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

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

ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
print("Text on the Button ", ele_id.text)
print("Text on the Button ", ele_id.get_attribute("text"))
print("Content Des  of the Button ", ele_id.get_attribute("content-desc"))
print("Resource ID  of the Button ", ele_id.get_attribute("resource-id"))
ele_id.click()

time.sleep(2)
ele_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
ele_classname.send_keys("Value entered")
time.sleep(2)
ele_classname.clear()
time.sleep(2)
ele_classname.send_keys("Value entered")

time.sleep(2)
driver.quit()