from selenium.webdriver.common.by import By

def click_downloads_button(driver):
    download_button = driver.find_element(By.XPATH, "//*[@id=\"downloads\"]/a")
    download_button.click()
    return driver