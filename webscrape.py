import time, re 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, MoveTargetOutOfBoundsException

# dummy account information 
USERNAME = "mephistophelesgrailtaker"
PASSWORD = "holygrail99"
SUBMISSION_LOGIN = "https://leetcode.com/submissions/detail/400104611/"
PROBLEM_SET = 'atoi'

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

# Search for the memory plot 
time.sleep(10)
memory_plot = driver.find_element_by_id("memory_detail_plot_placeholder")
print(memory_plot.location)
print(memory_plot.size)

# Create a dict to check for duplicate data points during loop-checking
prevData = ''

# Perform mouseover the memory plot
for xoffset in range(0, memory_plot.size['width']):

    try:
        hover = ActionChains(driver).move_to_element_with_offset(memory_plot, xoffset, memory_plot.size['height']-50)
        hover.perform()

    except MoveTargetOutOfBoundsException:
        break

    try:
        infoBox = driver.find_element_by_id('jquery-flot-comments-tooltip')

        if infoBox.text == prevData:
            continue
        else:
            prevData = infoBox.text
            label = re.search('\((.+?),', prevData).group(1)
            print(label)

        hover.click().perform()
        time.sleep(3)

        outputFile = open('{}_runtime_{}.txt'.format(PROBLEM_SET, label), 'w')
        sampleCode = driver.find_element_by_id('sample-submission-code')
        outputFile.write(sampleCode.text)
        outputFile.close()

        ActionChains(driver).move_to_element(driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div/div/div[1]/button')).click().perform()
    
    except NoSuchElementException:
        continue