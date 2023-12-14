from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get("http://127.0.0.1:5000/")

select = driver.find_element(By.ID,'myComboBox')
options = select.find_elements(By.TAG_NAME,'option')
count=0
for option in options:
    print(option.text+" "+option.get_attribute('value'))
    count +=1 
print("Count:",count)
driver.quit()


"""OUTPUT:-
    Option 1-1
    Option 2-2
    Option 3-3
    Count: 3
"""
