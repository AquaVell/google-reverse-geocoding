from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_autoinstaller
from excel_func import *


# Need this to crawl the website
def expandShadowElement(element):
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root

# Inserts the coordinates in the Google Playground and then passes it to another function which puts them inside the Output excel
def searchCoordinates(lastRow, coordsArray):
    number = [0]
    for i in range(0, len(coordsArray)):
        coordInput.clear()
        coordInput.send_keys(coordsArray[i])
        enterButton.click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="map"]/div/div[3]/div[1]/div[2]/div/div[4]/div/div/div/div[1]/div[2]/div')))
        address = driver.find_element(By.XPATH, '//*[@id="map"]/div/div[3]/div[1]/div[2]/div/div[4]/div/div/div/div[1]/div[2]/div').text
        print(address)
        lastRow += 1
        number[0] = number[0] + 1
        print(lastRow)
        coordsExcel(lastRow, address, number)


chromedriver_autoinstaller.install()

# The script runs inside an loop until it finishes geocoding all the coordinates given
# I had to do this because sometimes the program will crash when using too many coordinates (No problem, I made it so it can save the progress)
while(True):
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://geo-devrel-javascript-samples.web.app/samples/playground.html?showToolbar=true&previewHeight=400px&sample=geocoding-reverse")

        #Scraping the website
        root1 = driver.find_element(By.CSS_SELECTOR, 'google-maps-sample')
        shadow_root1 = expandShadowElement(root1)
        root2 = shadow_root1.find_element(By.CSS_SELECTOR, '.grow')
        shadow_root2 = expandShadowElement(root2)
        root3 = shadow_root2.find_element(By.CSS_SELECTOR, "iframe[title='Project preview']")
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(root3))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "latlng")))    # I don t get why this works sometimes and other times it makes the script crash
        coordInput = driver.find_element(By.ID, "latlng")
        enterButton = driver.find_element(By.ID, "submit")

        # Checks if there is previous progress
        lastRow = lastDone()

        # In case you try to restart it but it's already finished
        if lastRow is None:
            break
        
        # Loads the coordinates left to do
        coordsArray = loadCoordinates(lastRow)

        # Start the actual thing
        searchCoordinates(lastRow, coordsArray)

        print("Reverse Geocoding Completed, exiting loop...")
        driver.quit()
        break
    except:
        print("I Crashed...")
        saveExcel()
        driver.quit()