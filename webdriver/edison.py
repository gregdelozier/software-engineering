from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.get("https://wikipedia.org")
search_input = browser.find_element(by=By.NAME, value="search")
search_button = browser.find_element(by=By.CSS_SELECTOR, value="button")

search_input.send_keys("light bulb")
search_button.click()

sleep(2)

text = browser.find_element(by=By.XPATH, value="/html/body").text
assert "Thomas Edison" in text

browser.quit()