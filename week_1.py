from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

total_txt_field=driver.find_elements(By.CLASS_NAME,"text_field")
print("total_text_fields_in_webpages=",len(total_txt_field))

total_links=driver.find_elements(By.TAG_NAME,"a")
print("totel links present in webpage:",len(total_links))

element=driver.find_elements(By.CLASS_NAME,"drop_down")
print ("totel number of dropdowns:",len(element))

status=driver.find_element(By.ID,"RESULT_RadioButton-7_0").is_selected()
status_1=driver.find_element(By.ID,"RESULT_CheckBox-8_1").is_selected()
drp=Select(element)

print(drp.options)

driver.find_element(By.ID,"RESULT_TextField-1").send_keys("Naveen")
driver.find_element(By.ID,"RESULT_TextField-2").send_keys("kota")
driver.find_element(By.ID,"RESULT_TextField-3").send_keys("9012222222")
driver.find_element(By.ID,"RESULT_TextField-4").send_keys("Canada")
driver.find_element(By.ID,"RESULT_TextField-5").send_keys("Halifax")
driver.find_element(By.ID,"RESULT_TextField-6").send_keys("@dal.ca")

if status==False & status_1==False:
    driver.find_element(By.ID,"RESULT_CheckBox-8_1").click()
    driver.find_element(By.ID,"RESULT_RadioButton-7_0").click()


time.sleep(3)
driver.quit()