from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@given(u'we have gone to the wikipedia search page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://wikipedia.org")
    sleep(3)


@when(u'we search for "{invention}"')
def step_impl(context, invention):
    search_input = context.browser.find_element(by=By.NAME, value="search")
    search_button = context.browser.find_element(by=By.CSS_SELECTOR, value="button")
    search_input.send_keys(invention)
    search_button.click()
    sleep(2)    


@then(u'the resulting page should contain "{inventor}"')
def step_impl(context, inventor):
    text = context.browser.find_element(by=By.XPATH, value="/html/body").text
    assert inventor in text
