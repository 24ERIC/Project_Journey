from selenium import webdriver
browser = webdriver.PhantomJS()
browser.get("https://www.python.org/")
print(browser.find_element_by_class_name("introduction").text)



browser.find_element_by_id("id")
browser.find_element_by_css_selector("#id")
browser.find_element_by_link_text("Click Here")
browser.find_element_by_name("Home")



browser.find_elements_by_id("id")
browser.find_elements_by_css_selector("#id")
browser.find_elements_by_link_text("Click Here")
browser.find_elements_by_name("Home")



browser.close()