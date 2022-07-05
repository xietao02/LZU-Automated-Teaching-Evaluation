#-=-=-=-=-=-=-=-=-=-=-info-=-=-=-=-=-=-=-=-=-=-=-=
# coding: UTF-8
# by xietao from Lanzhou University(兰州大学)

#-=-=-=-=-=-=-=-=-=-Tutorials-=-=-=-=-=-=-=-=-=-=-
#

#-=-=-=-=-=-=-=-=-Preprocessing-=-=-=-=-=-=-=-=-=-
# Education Email Prefix
Account = "txie20"
# Password  
Password = ""
# Satisfaction with the course
Satisfaction = "课程很受用，老师的讲授很生动。"
# Areas for improvement of the course
Improvement = "无"
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://my.lzu.edu.cn:8080/login?service=http://my.lzu.edu.cn")
driver.implicitly_wait(0.5)

driver.find_element(By.ID, "username").send_keys(Account)
time.sleep(0.5)
driver.find_element(By.NAME, "password").send_keys(Password + Keys.ENTER)

def Evaluation_of_teaching(teachers):
    for i in range(1, teachers+1):
        time.sleep(3)
        js = '''return document.querySelector("#sample_2 > tbody > tr:nth-child(''' + \
            str(i) + ''') > td:nth-child(3) > div > a").click()'''
        driver.execute_script(js)
        time.sleep(2)
        print("Evaluation of teaching:", i, end="   ")
        Evaluation()
    js = '''document.querySelector("#kfxpjDlg > div.modal-header > button").click()'''
    driver.execute_script(js)

def Evaluation():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "zbxxid_1030")))
    js = '''return document.getElementsByClassName("controls").length'''
    Questions = driver.execute_script(js)
    print("Questions:", Questions)
    for i in range(3, Questions-3):
        js = '''document.getElementsByClassName("controls")['''+ \
            str(i) + '''].getElementsByTagName('label')[0].click()'''
        driver.execute_script(js)
    js = '''document.getElementsByClassName("controls")[''' + str(Questions-3) + '''].getElementsByTagName('label')[1].click()'''
    driver.execute_script(js)
    js = '''document.getElementsByClassName("controls")[''' + str(Questions-2) + '''].getElementsByTagName('textarea')[0].value = "''' + str(Satisfaction) + '''"'''
    driver.execute_script(js)
    js = '''document.getElementsByClassName("controls")[''' + str(Questions-1) + '''].getElementsByTagName('textarea')[0].value = "''' + str(Improvement) + '''"'''
    driver.execute_script(js)
    time.sleep(2)
    js = '''document.querySelector('#pjsubmit').click()'''
    driver.execute_script(js)
    js = '''document.querySelector("#finishDlg > div.modal-footer > button").click()'''
    driver.execute_script(js)
    time.sleep(3)

while True:
    if "http://my.lzu.edu.cn/main" in driver.current_url:
        print("Login: successful!")
        time.sleep(0.5)
        driver.get("http://qa.lzu.edu.cn:8081/loginSSO2")
        break
    else:
        print("Login: failed! Please login manually!")
        time.sleep(10)


js = '''return document.querySelector('#task-list').getElementsByTagName('li').length'''
taskList = 0
while taskList == 0:
    taskList = driver.execute_script(js)
    if(taskList != 0):
        print("taskNum:", taskList)
    

for i in range(1, taskList+1):
    js = '''return document.querySelector('#task-list>li:nth-child(''' + \
        str(i)+''')').className'''
    currentClass = driver.execute_script(js)
    if currentClass == "over":
        continue
    js = '''document.querySelector('#task-list>li:nth-child(''' + \
        str(i)+''')').click()'''
    driver.execute_script(js)
    time.sleep(1)

    js = '''return document.querySelector("#tipDlg > div.modal-footer > button").disabled'''
    while driver.execute_script(js):
        time.sleep(2)
    js = '''document.querySelector("#tipDlg > div.modal-footer > button").click()'''
    driver.execute_script(js)
    time.sleep(2)

    js = '''return document.querySelector('#pjkc').rows.length'''
    rows = 0
    while rows == 0:
        rows = driver.execute_script(js)
        if(rows != 0):
            print("Total number of courses:", rows)

    for j in range(1, rows+1):
        js = '''document.querySelector("#pjkc > tr:nth-child(''' + \
            str(j) + ''') > td:nth-child(3) > div > a").click()'''
        driver.execute_script(js)

        teachers = 0
        js = '''return document.querySelector("#sample_2 > tbody").rows.length'''
        while teachers == 0:
            teachers = driver.execute_script(js)
        print("class:", j, " teachers:", teachers)
        time.sleep(1)

        if teachers < 3:
            Evaluation_of_teaching(teachers)
        else:
            js = '''document.querySelector("#kfxpjDlg > div.modal-header > button").click()'''
            driver.execute_script(js)
            time.sleep(4)
            js = '''document.querySelector("#pjkc > tr:nth-child(''' + \
            str(j) + ''') > td:nth-child(6) > div > a").click()'''
            driver.execute_script(js)
            Evaluation()
            js = '''document.querySelector("#pjkc > tr:nth-child(''' + \
            str(j) + ''') > td:nth-child(3) > div > a").click()'''
            driver.execute_script(js)
            Evaluation_of_teaching(teachers)
        print("class " + str(j) + " finished!", end="\n\n")
    
    js = '''document.querySelector("#titlelist > div.actions > div > a").click()'''
    driver.execute_script(js)

print("Evaluation of teaching is complete!\nScript will close automatically after 5 seconds!")
time.sleep(5)
driver.quit()
