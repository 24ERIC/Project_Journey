from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.python.org/")
nav = browser.find_element_by_id("mainnav")
print(nav.text)