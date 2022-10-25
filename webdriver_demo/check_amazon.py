from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://www.amazon.com")

    assert "Amazon" in browser.title

    search_box = browser.find_element(By.ID,"twotabsearchtextbox")
    search_box.clear()
    search_box.send_keys("blender")
    submit_button = browser.find_element(By.ID,"nav-search-submit-button")
    submit_button.click()

    assert "Hamilton Beach" in browser.page_source

    time.sleep(10)
finally:
    browser.close()




