import time 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# dummy account information 
USERNAME = "mephistophelesgrailtaker"
PASSWORD = "holygrail99"
SUBMISSION_LOGIN = "https://leetcode.com/submissions/detail/397441290/"

# initialize Chrome driver with Selenium
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# Sign in to Leetcode using dummy account 
driver.get(SUBMISSION_LOGIN)
username = driver.find_element_by_id("id_login")
username.clear()
username.send_keys(USERNAME)
password = driver.find_element_by_name("password")
password.clear()
password.send_keys(PASSWORD)
time.sleep(1)
driver.find_element_by_id("signin_btn").click()

# Get to the submission stats page 
