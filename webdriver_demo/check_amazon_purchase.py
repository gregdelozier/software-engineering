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

    time.sleep(5)
    search_div = browser.find_element(By.ID,'search')
    # print(search_div.text)
    # assert "Hamilton Beach" in browser.page_source
    anchors = search_div.find_elements(By.TAG_NAME,"a")
    # for a in list(anchors):
    #     if "Hamilton Beach" in a.text and "Personal Blender Blender" in a.text:
    #         a.click()
    #         break
    for a in list(anchors):
        if "Hamilton Beach" in a.text and "Wave Crusher Blender" in a.text:
            a.click()
            break
    assert "Hamilton Beach" in browser.title
    add_to_cart_button = browser.find_element(By.ID, "add-to-cart-button")
    add_to_cart_button.click()
    time.sleep(5)
    no_thanks_spans = browser.find_elements(By.ID,"attachSiNoCoverage")
    if len(no_thanks_spans) > 0:
        no_thanks_input = no_thanks_span[0].find_element(By.TAG_NAME,"input")
        no_thanks_input.click()
        time.sleep(5)
    assert "Added to Cart" in browser.page_source
    assert "Proceed to checkout" in browser.page_source
    time.sleep(5)
    view_cart_form = browser.find_element(By.ID,"attach-view-cart-button-form")
    view_cart_input = view_cart_form.find_element(By.TAG_NAME,"input")
    view_cart_input.click()
    time.sleep(5)
    # can you find if in the cart we do in fact have the blender? 
    print("test passed")
finally:
    browser.close()




