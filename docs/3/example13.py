from selenium import webdriver
browser = webdriver.PhantomJS()
browser.get("https://likegeeks.com/")
print(browser.get_cookies())