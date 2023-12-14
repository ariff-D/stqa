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
   url = 'https://www.facebook.com/'
   driver.get(url)
   time.sleep(1)
   email = driver.find_element(By.ID, 'email')
   email.send_keys("youremail@gmail.com")
   time.sleep(1)
   password =driver.find_element(By.ID, "pass")
   password.send_keys("yourpassword")
   time.sleep(1)
   btn =driver.find_element(By.XPATH , '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
   btn.click()
   time.sleep(4)
main()
