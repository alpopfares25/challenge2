
from selenium import webdriver


mobile= "01001234455"
password="111111"
url="https://dashboard.staging.fatura-app.com/#/login"

driver=webdriver.Chrome("chromedriver.exe")
driver.get(url)
mobile=driver.find_element_by_xpath("//*[@id='fatura-dashboard']/section/div/div/div/form/div[1]/div/div/input").send_keys(mobile)
password=driver.find_element_by_xpath("//*[@id='fatura-dashboard']/section/div/div/div/form/div[2]/div/div/input").send_keys(password)
driver.find_element_by_xpath("//*[@id='fatura-dashboard']/section/div/div/div/form/div[3]/div/button").click()

##cdriver.find_element_css_selector()



