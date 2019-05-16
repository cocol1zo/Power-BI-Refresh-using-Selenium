import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


URL = "Enter URL"

chromedriver_PATH = "C:\\Users\\rshars\\Desktop\\Shared drive\\Dashboard Automation\\chromedriver"

username = "Enter Username"

password = "Enter Password"

driver = webdriver.Chrome(executable_path = chromedriver_PATH)

driver.wait = WebDriverWait(driver, 10)


driver.get(URL)
HTML = driver.page_source

time.sleep(5)

driver.find_element_by_xpath("/html/body/section[1]/div[3]/div/a").click()

time.sleep(5)

driver.find_element_by_name("loginfmt").send_keys(username)

driver.find_element_by_xpath('//*[@id="i0281"]/div[1]/div/div[1]/div[2]/div/div/div[3]/div[1]').click()

time.sleep(5)

driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)

driver.find_element_by_xpath('//*[@id="Login"]/div[2]//input[@type="submit"]').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/div/form/div[1]/div/div[1]/div[2]/div/div/div[4]/div[1]//input[@type="submit"]').click()

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="contentMain"]/navigation-pane-v2/div[1]/div[1]/group-switcher')))



driver.find_element_by_xpath('//*[@id="contentMain"]/navigation-pane-v2/div[1]/div[1]/group-switcher').click()


driver.find_element_by_xpath('//*[@id="contentMain"]/navigation-pane-v2/div[1]/div[1]/quick-access-pane/div/button').click()



driver.find_element_by_xpath('//*[@id="contentMain"]/navigation-pane-v2/div[1]/div[1]/quick-access-pane/section/ul[4]/li[1]/button').click()

#WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[9]/div/dropdown-list/dropdown-list-item[4]')))


driver.find_element_by_xpath('//*[@title="REFRESH NOW"]').click()

