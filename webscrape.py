import time 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# dummy account information 
USERNAME = "mephistophelesgrailtaker"
PASSWORD = "holygrail99"
SUBMISSION_LOGIN = "https://leetcode.com/submissions/detail/400104611/"

# initialize Chrome driver with Selenium
DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.maximize_window()

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

# Search for the runtime plot 
time.sleep(10)
runtime_plot = driver.find_element_by_id("runtime_detail_plot_placeholder")
print(runtime_plot.location)
print(runtime_plot.size)
