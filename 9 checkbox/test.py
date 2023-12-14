from selenium import webdriver 
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("http://localhost:5000/")
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
checked=0
unchecked = 0 
for checkbox in checkboxes:
    if checkbox.is_selected():
        checked+=1
    else:
        unchecked+=1
print("Total checkboxes:",len(checkboxes))
print("Checked:",checked)
print("Unchecked:",unchecked)

driver.quit()

"""OUTPUT:-
    Total checkboxes: 4
    Checked: 2
    Unchecked: 2
"""
