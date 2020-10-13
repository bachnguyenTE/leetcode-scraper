import time, re, os, io
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, MoveTargetOutOfBoundsException, TimeoutException, JavascriptException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


# dummy account information 
USERNAME = "mephistophelesgrailtaker"
PASSWORD = "holygrail99"
SUBMISSION_LOGIN = "https://leetcode.com/submissions/detail/402756293/"
PROBLEM_SET = 'isPalindrome'

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

# Create directory to store current scraped datasets
parent_dir = os.getcwd()
directory = '{}_dataset'.format(PROBLEM_SET)
path = os.path.join(parent_dir, directory)
os.mkdir(path)
os.chdir(path)

# Plot scraping function
def plotScrape(plotType: str, data_path, yoffset: int):

    # Search for the plot 
    time.sleep(6)
    plot_holder = driver.find_element_by_id('{}_detail_plot_placeholder'.format(plotType))
    print(plot_holder.location)
    print(plot_holder.size)

    # Create a directory to store the scraped code 
    dataset_dir = os.path.join(data_path, plotType)
    os.mkdir(dataset_dir)
    os.chdir(dataset_dir)

    # Create a dict to check for duplicate data points during loop-checking
    prevData = ''

    # Perform mouseover the memory plot
    for xoffset in range(80, plot_holder.size['width'] - 200, 3):

        # Search for clickable bars in the plot 
        try:
            hover = ActionChains(driver).move_to_element_with_offset(plot_holder, xoffset, plot_holder.size['height']-yoffset)
            hover.perform()

        except MoveTargetOutOfBoundsException:
            break

        # Parse the plot data and the sample code each time a bar is found and clicked
        try:
            infoBox = driver.find_element_by_id('jquery-flot-comments-tooltip')

            # Check if bar is a dupe to skip 
            if infoBox.text == prevData:
                continue
            else:
                prevData = infoBox.text
                label = re.search('\((.+?),', prevData).group(1)
                print(label)

            # try:
            #     hover.click().perform()
            #     time.sleep(5)
            #     WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div[2]/div/div/div/div[1]/button')))

            #     # Scrape and write sample code to file
            #     outputFile = open('{}_{}_{}.txt'.format(PROBLEM_SET, plotType, label), 'w')
            #     sampleCode = driver.find_element_by_id('sample-submission-code')
            #     outputFile.write(sampleCode.text)
            #     outputFile.close()
            #     ActionChains(driver).move_to_element(driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div/div/div[1]/button')).click().perform()
            # except TimeoutException:
            #     print('Timeout occured at {} {}.'.format(plotType, label))
            #     ActionChains(driver).move_to_element(driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div/div/div[1]/button')).click().perform()
            #     continue

            hover.click().perform()
            time.sleep(5)

            # Scrape and write sample code to file
            filename = '{}_{}_{}.txt'.format(PROBLEM_SET, plotType, label)
            outputFile = io.open(filename, 'w', encoding='utf-8')
            sampleCode = driver.find_element_by_id('sample-submission-code')
            outputFile.write(sampleCode.text)
            outputFile.close()

            if os.path.getsize(filename) < 50:
                print('Empty file deleted at {} {}.'.format(plotType, label))
                os.remove(filename)

            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        
        except (NoSuchElementException, AttributeError):
            continue

    # Go back to the original directory for all datasets
    os.chdir(data_path)


# Scrape and generate files for runtime plot
plotScrape('runtime', path, 37)

# Scrape and generate files for memory plot
plotScrape('memory', path, 45)


# yoffset for runtime (atoi): 37
# yoffset for memory (atoi): 45