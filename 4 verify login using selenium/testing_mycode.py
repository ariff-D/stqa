import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
def main():
   options =Options()
   options.add_experimental_option("excludeSwitches" , ["enable-automation"])
   service = Service(r"C:\selenium\chromedriver-win64\chromedriver.exe")
   driver = webdriver.Chrome(options=options ,service=service)
   url = 'http://127.0.0.1:5500/myLoginPage.html'
   driver.get(url)
   time.sleep(1)
   email = driver.find_element(By.ID, 'username')
   email.send_keys("youremail@gmail.com")
   time.sleep(1)
   password =driver.find_element(By.ID, "password")
   password.send_keys("yourpassword")
   time.sleep(1)
   btn =driver.find_element(By.XPATH , '/html/body/div/button')
   btn.click()
   time.sleep(40)
main()
