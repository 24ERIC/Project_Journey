from selenium import webdriver
browser = webdriver.PhantomJS()
browser.get("https://likegeeks.com/")
browser.delete_all_cookies()