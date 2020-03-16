# -*- coding: utf-8 -*- 
#  from selenium.webdriver import Chrome
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Story Begains

        # Edith has heard about a cool new online to-do app
        # She goes to check out its homepage
        self.browser.get(self.live_server_url)
        self.browser.implicitly_wait(10)


        #  assert 'Django' in browser.title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types " Buy peacock feathers" into a text box
        input_box.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the apge lists
        # "1: By peacock feathers" as an item in a to-do list
        input_box.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        #  self.assertTrue(
            #  any(row.text == '1: Buy peacock feathers' for row in rows),
            #  f"New to-do item did not appear in table. Contents were:\n{table.text}"
        #  )
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # There is still a text box inviting her to add another item.
        input_box = self.browser.find_element_by_id('id_new_item')

        # She enters "Use peacock feathers to make a fly"
        input_box.send_keys('Use peacock feathers to make a fly')
        input_box.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(1)

        # The page updates again, and now shows both items on her list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])

        # Edith wonders whether the site will remember her list.
        # Then she sees that the site has generated a unique URL for her
        # there is some explanatory text to that effect.

        # She vistis that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
