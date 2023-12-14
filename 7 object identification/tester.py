from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("https://support.smartbear.com/testcomplete/docs/reference/test-objects/controls/web/general/list-of-web-objects.html")

web_object_elements =['object','embed','img','a','textarea','audio','video','iframe','table','input']
web_page_elements = set()
wait = WebDriverWait(driver,1000)
wait.until(EC.presence_of_all_elements_located((By.XPATH,"//*")))
elements = driver.find_elements(By.XPATH,"//*")
for element in elements:
    if element.tag_name in web_object_elements:
        if element.tag_name == "input":
            web_page_elements.add(element.get_attribute('type'))
        web_page_elements.add(element.tag_name)
print(web_page_elements)
print("The count is:",len(web_page_elements))
driver.close()


"""OUTPUT:-
    {'img', 'a', 'text', 'textarea', 'checkbox', 'table', 'iframe', 'input'}
    The count is: 8 
"""
