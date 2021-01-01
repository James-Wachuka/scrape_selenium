from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
from selenium.common.exceptions import NoSuchElementException,TimeoutException
url = 'https://twitter.com/login'
driver_exe = 'C:/python_proj/chromedriver.exe'
driver = webdriver.Chrome(driver_exe)
driver.get(url)
# Function of waiting until the present of the element on the web page
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session[username_or_email]']"))).send_keys("")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session[password]']"))).send_keys("")
driver.find_element_by_xpath("//div[@data-testid='LoginForm_Login_Button']").click()

# Function of waiting until the present of the element on the web page
def waiting_func(by_variable, attribute):
    try:
        WebDriverWait(driver, 20).until(lambda x: x.find_element(by=by_variable,  value=attribute))
    except (NoSuchElementException, TimeoutException):
        print('{} {} not found'.format(by_variable, attribute))
        exit()

waiting_func('css selector', "[aria-label=Profile]")
profile = driver.find_element_by_css_selector("a[aria-label='Profile']")
profile.click()

# get tweet activity
path = []
while True:
    waiting_func('css selector', "a[aria-label='View Tweet activity']")
    last_height = driver.execute_script("return document.body.scrollHeight")
    traffic_path = driver.find_elements_by_css_selector("a[aria-label='View Tweet activity']")
    #driver.find_elements_by_css_selector("[aria-label=XXXX]")
    path.extend([traffic.get_attribute('href') for traffic in traffic_path])
    driver.execute_script("window.scrollTo(0, {})".format(last_height+500))
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if last_height == new_height:
        break

# capture traffic statistics

# 1. switch to iframe
waiting_func('tag name', 'iframe')
iframe = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(iframe)

# 2. capture the impression
detail = driver.find_element_by_tag_name('body')
impression = detail.find_element_by_class_name('ep-MetricTopContainer')
print(impression.text)

# capture engagement
try:
    WebDriverWait(driver, 5).until(
        lambda x: x.find_element(by='class name', value='ep-ViewAllEngagementsButton'))
except TimeoutException:
    pass
view_all = driver.find_element_by_class_name('ep-ViewAllEngagementsButton')
view_all.click()
waiting_func('class name', 'ep-EngagementsSection')
engagesection = driver.find_element_by_class_name('ep-EngagementsSection')
waiting_func('class name', 'ep-MetricTopContainer')
engagement = engagesection.find_element_by_class_name('ep-MetricTopContainer')
print(engagement.text)
waiting_func('class name', 'ep-DetailedEngagementsSection')
detail = engagesection.find_element_by_class_name('ep-DetailedEngagementsSection')
waiting_func('class name', 'ep-SubSection')
engagement_details = detail.find_elements_by_class_name('ep-SubSection')
for _ in engagement_details:
    print(_.text)

input('Press ENTER to close the automated browser')
driver.quit()
