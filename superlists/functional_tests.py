# -*- coding: utf-8 -*- 
from selenium.webdriver import Chrome

browser = Chrome()
browser.get('http://localhost:8000')


assert 'Django' in browser.title
