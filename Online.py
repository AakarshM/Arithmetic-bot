import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/Aakarsh/Downloads/chromedriver')
driver.get('http://arithmetic.zetamac.com/game?key=96823302')
element = driver.find_element_by_class_name('answer')
a = True;
while(a == True):
    element.send_keys(4)
