from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://www.python.org")

    assert "Python" in browser.title

    search_box = browser.find_element(By.NAME,"q")
    search_box.clear()
    search_box.send_keys("pycon")
    search_box.send_keys(Keys.RETURN)

    assert "Results" in browser.page_source
    assert "No results found." not in browser.page_source
    time.sleep(15)
finally:
    browser.close()




