from selenium.webdriver.common.by import By

def downloads_latest_python_version(driver,new_version):
    downloads_latest_python_version_button = driver.find_element(By.XPATH, "//*[@id=\"touchnav-wrapper\"]/header/div/div[2]/div/div[4]/p/a")
    downloads_latest_python_version_text = str(downloads_latest_python_version_button.text)
    if downloads_latest_python_version_text != None :
        words = downloads_latest_python_version_text.split()
        #for word in words:
            #print(word)
            #print(new_version)
        if new_version == words[2] :
            print("correct version "+words[2])
        else:
            print("wrong version "+words[2])
    return driver