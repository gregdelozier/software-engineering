from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.get("https://www.selenium.dev/selenium/web/web-form.html")

title = browser.title

assert title > ""

browser.implicitly_wait(0.5)

text_box = browser.find_element(by=By.NAME, value="my-text")
submit_button = browser.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = browser.find_element(by=By.ID, value="message")
text = message.text
print(text)

sleep(100)

browser.quit()