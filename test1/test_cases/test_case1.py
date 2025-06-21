import time
from selenium import webdriver
from pages.home_page import click_downloads_button
from pages.download_page import downloads_latest_python_version

driver = webdriver.Chrome()
time.sleep(2)
driver.get("https://www.python.org")

driver = click_downloads_button(driver)

driver = downloads_latest_python_version(driver,"3.13.1")


