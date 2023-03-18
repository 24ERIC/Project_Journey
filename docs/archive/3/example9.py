from selenium import webdriver
browser = webdriver.PhantomJS()
browser.get("https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe")
iframe = browser.find_element_by_tag_name("iframe")
browser.switch_to.default_content()
browser.switch_to.frame(iframe)
iframe_source = browser.page_source
print(iframe_source) #returns iframe source
print(browser.current_url) #returns iframe URL