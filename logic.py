from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import variables
import time

browser  = webdriver.Chrome(ChromeDriverManager().install())

##Opens a user interface

browser.get(myWebPage)
driver.maximize_window()
driver.implicitly_wait(10)

## Select a specific time and date 
def dateTimeSelect() :
    dateTimeElement = driver.find_element_by_id("purchasetime").click()
    dateTimeElement.send_keys(myDate)
    dateTimeElement.send_keys(Keys.TAB)
    dateTimeElement.send_keys(myTime)
    driver.find_element_by_xpath(submitButton).click()
    ##bring up webpage containing submitted date and time.
    driver.find_element_by_xpath(startButton).click()
    return dateTimeElement


## Function utilizing while loop that sleeps (time.sleep) until specific time is reached. 
def sleepUntil(dateTimeReached, dateTimeSelect()) :
    sleep = True
    while sleep == True:
        if dateTimeReached == dateTimeElement:
            shopForProduct()
            sleep = False
        time.sleep()    

# Call to sleep function to begin purchase process.
#sleepUntil(myDate == "06022021" and myTime ==  "1200AM", shopForProduct())

##	Function to Launch Chrome, go to desired website, purchase desired item.
def shopForProduct() :
    browser.get(productWebpage) 
    desiredProduct = driver.find_element_by_xpath(searchBar)
    desiredProduct.send_keys(searchBarItem)
    driver.find_element_by_xpath(searchButton).click()
    driver.find_element_by_xpath(itemToBuy).click()
    driver.find_element_by_xpath(buyNowButton).click()

##4.	Function to return results of attempted shopping venture.
def results(infoPassedFromShoppingAttempt)