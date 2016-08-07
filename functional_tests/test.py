from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_search_a_city(self):
        # Edith has heard about a cool new online travel site
        # She goes to check out its homepage
        self.browser.get('http://127.0.0.1:8080/')

        # She notices the page title and header mention the title
        assert 'Travel Share' in self.browser.title

        # She is invited to search or select a city

        # She types in "Berlin, Germany" into a text box
        # Edith would like to visit Berlin

        # When she hits enter, the page changes, and now
        # she can see all the tour plans for Berlin

        # Edith has a look at the first one on the list

if __name__ == '__main__':
    unittest.main(warnings='ignore')
