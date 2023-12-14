from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.by import By

def test():
   driver = webdriver.Edge()
   driver.get('http://127.0.0.1:8008/')
   s1H_marks = {'student':'', 'marks':0}
   s2H_marks = {'student':'', 'marks':0}
   s3H_marks = {'student':'', 'marks':0}

   table = driver.find_element(By.TAG_NAME, 'table')
   rows = driver.find_elements(By.TAG_NAME, 'tr')
   sleep(5)
   student_marks60 = []
   for row in rows[1:]:
      cell = row.find_elements(By.TAG_NAME, 'td')
      if int(cell[3].text) >= 60 or int(cell[4].text) >= 60 or int(cell[5].text) >= 60:
         student_marks60.append([int(cell[0].text),cell[1].text, cell[2].text, int(cell[3].text), int(cell[4].text), int(cell[5].text)])
         for student in student_marks60:
            if student[3] > s1H_marks['marks']:
               s1H_marks = {'student':student[1], 'marks':student[3]}

            if student[4] > s2H_marks['marks']:
               s2H_marks = {'student':student[1], 'marks':student[4]}

            if student[5] > s3H_marks['marks']:
               s3H_marks = {'student':student[1], 'marks':student[5]}
         print(f"Student: {student}")
   print("\n\nHighest marks mode than 60 of each subject.")
   print(f"subj1: {s1H_marks} \nsubj2: {s2H_marks} \nsubj3: {s3H_marks}")
   driver.quit()

if __name__ =="__main__":
   test()