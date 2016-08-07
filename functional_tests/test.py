from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8080/')

print(browser.find_elements_by_tag_name('p')[0].text)
assert 'Hello, World!' == browser.find_elements_by_tag_name('p')[0].text