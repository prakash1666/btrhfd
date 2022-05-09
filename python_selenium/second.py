from selenium import webdriver
import time
driver = webdriver.Chromexe")(r"C:\Users\praka\OneDrive\Desktop\chromedriver_win32\chromedriver.e
driver.get("http://google.com")


anchor = driver.find_element_by_id('h1Id')
print(anchor.text)
time.sleep(3)


id = driver.find_element_by_xpath('//p[@id="pId"]')
print(id.text)
time.sleep(3)


input1 =driver.find_element_by_id("inputId1")
print(input1.get_attribute('value'))
time.sleep(3)

input2 = driver.find_element_by_id("inputId2")
print(input2.get_attribute("placeholder"))
time.sleep(3)

driver.find_element_by_link_text('Google.com').click()
time.sleep(3)

driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

driver.find_element_by_link_text('Google.com').click()
time.sleep(3)

driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

driver.quit()