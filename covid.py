from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
#browser = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options, executable_path=r'/usr/bin/chromedriver')
#driver.get("https://www.google.com/")

#browser = webdriver.Firefox()
driver.get('https://www.qfc.com/rx/guest/get-vaccinated')

# Search for stores
elem = driver.find_element(By.NAME, 'findAStore')
#elem.send_keys('98225' + Keys.RETURN)
elem.send_keys('98033' + Keys.RETURN)

# Wait for results
time.sleep(2)


def check_pharmacy(elem):
    # Scroll to the top of the page to ensure that the 'Choose Location' heading is clickable
    print('Scrolling up....')
    driver.execute_script('window.scrollTo(0,document.body.scrollTop)')
    time.sleep(1)

    print('Selecting store....')
    # Select this store
    elem.click()

    print('Getting store address....')
    elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[1]')
    store_address = elem.get_attribute('innerText')
    elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[2]')
    store_address += ', ' + elem.get_attribute('innerText')

    # Wait for the store to fully render
    time.sleep(1)

    print('Clicking continue for this store....')
    # Click 'Continue' for this store
    elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[3]/button')
    elem.click()

    # Wait for the vaccine page
    time.sleep(1)

    # Check the "Covid-19" checkbox
    elem = None
    try:
        elem = driver.find_element(By.NAME, 'COVID-19 Vaccine')
    except NoSuchElementException:
        print(store_address, ": covid-19 vaccine not distributed here")

    if elem:
        if not elem.is_selected():
            elem.click()

        # Click 'Continue' for the vaccine search
        elem = driver.find_element(By.XPATH, '//*[@id="step2"]/div/div/form/div/button')
        elem.click()

        # Wait on the vaccine results to load
        time.sleep(4)

        # See if there are any vaccines. Most likely we'll get:
        #  Sorry, there are no available time slots at this location. Please try another location or check back soon.
        try:
            elem = driver.find_element(By.XPATH, '//*[@id="step3"]/div/div/div/div/form/div/span')
            if "there are no available time slots" in elem.get_attribute('innerText'): 
                print(store_address, ": has no time slots available")
            else:
                print(store_address, ": likely has availability!")
        except:
            print(store_address, ": likely has availability!")

    # Scroll to the top of the page to ensure that the 'Choose Location' heading is clickable
    driver.execute_script('window.scrollTo(0,document.body.scrollTop)')
    time.sleep(1)

    # Click 'Choose Location' header
    elem = driver.find_element(By.XPATH, '//*[@id="step1"]/button/div/div[1]/h2')
    elem.click()

    time.sleep(2)

    # Click 'Choose Another Pharmacy' button
    elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/button')
    elem.click()

    time.sleep(2)

check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result0"]/div/button'))
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result1"]/div/button'))
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result2"]/div/button'))
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result3"]/div/button'))

elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/div[2]/div[2]/div/nav/a[2]')
elem.click()
time.sleep(2)
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result0"]/div/button'))
elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/div[2]/div[2]/div/nav/a[2]')
elem.click()
time.sleep(2)
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result1"]/div/button'))
elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/div[2]/div[2]/div/nav/a[2]')
elem.click()
time.sleep(2)
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result2"]/div/button'))
elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/div[2]/div[2]/div/nav/a[2]')
elem.click()
time.sleep(2)
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result3"]/div/button'))

elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/div[2]/div[2]/div/nav/a[3]')
elem.click()
time.sleep(2)
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result0"]/div/button'))
elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/div[2]/div[2]/div/nav/a[3]')
elem.click()
time.sleep(2)
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result1"]/div/button'))
elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/div[2]/div[2]/div/nav/a[3]')
elem.click()
time.sleep(2)
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result2"]/div/button'))
elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/div[2]/div[2]/div/nav/a[3]')
elem.click()
time.sleep(2)
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result3"]/div/button'))


elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/div[2]/div[2]/div/nav/a[4]')
elem.click()
time.sleep(2)
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result0"]/div/button'))
elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/div[2]/div[2]/div/nav/a[4]')
elem.click()
time.sleep(2)
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result1"]/div/button'))
elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/div[2]/div[2]/div/nav/a[4]')
elem.click()
time.sleep(2)
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result2"]/div/button'))
elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/div[2]/div[2]/div/nav/a[4]')
elem.click()
time.sleep(2)
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result3"]/div/button'))


elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/div[2]/div[2]/div/nav/a[5]')
elem.click()
time.sleep(2)
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result0"]/div/button'))
elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/div[2]/div[2]/div/nav/a[5]')
elem.click()
time.sleep(2)
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result1"]/div/button'))
elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/div[2]/div[2]/div/nav/a[5]')
elem.click()
time.sleep(2)
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result2"]/div/button'))
elem = driver.find_element(By.XPATH, '//*[@id="step1"]/div/div/form/div[2]/div[2]/div[2]/div/nav/a[5]')
elem.click()
time.sleep(2)
check_pharmacy(driver.find_element(By.XPATH, '//*[@id="SearchResults-store-result3"]/div/button'))

driver.quit()
