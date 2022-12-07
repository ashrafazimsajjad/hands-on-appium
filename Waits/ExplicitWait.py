from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
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

# list of Selenium Exceptions
# https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html
wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

ele = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue"))
ele.click()

ele = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText"))
ele.send_keys("Value Entered")

time.sleep(4)
driver.quit()
