from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

@given(u'we are browsing wikipedia home page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("http://wikipedia.org")


@when(u'we search for "{language}"')
def step_impl(context, language):
    search_input = context.browser.find_element(By.ID,"searchInput")
    search_input.clear()
    search_input.send_keys(language)  
    search_input.send_keys(Keys.RETURN)  


@then(u'we will see a reference to "{author}"')
def step_impl(context, author):
    assert author in context.browser.page_source
