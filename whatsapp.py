from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('/home/arshul/Downloads/chromedriver')
print("here")
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
target = "harshit"
msg = "Message sent using Python!!!"

x_arg = '//*[@id="side"]/div[2]/div/label/input'

group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.send_keys(target + Keys.ENTER)
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
print"hhere"
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

for i in range(10):
    input_box.send_keys(msg + Keys.ENTER)
    time.sleep(1)
