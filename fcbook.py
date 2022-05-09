import time

from selenium import webdriver
driver=webdriver.Chrome(r"C:\Users\praka\OneDrive\Desktop\chromedriver_win32\chromedriver.exe")
driver.get("https://www.facebook.com/")
#${vir}=    prakashkollati16@gmail.com
#$driver.maximize_window() varible assining###########
driver.find_element_by_xpath('//input[@id="email"]').send_keys
driver.find_element_by_xpath('//input[@type="password"]').send_keys('prakash1995')
driver.find_element_by_xpath('//button[@name="login"]').click()
time.sleep(4)
driver.close()






