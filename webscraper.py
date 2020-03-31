import sys
import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#Your Repository Name passed as Commandline argument to this python script
repo_name = sys.argv[1]

#Set the executable_path as path of chromedriver.exe
#Example executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver = webdriver.Chrome(executable_path=r"")
driver.get('https://github.com/login')

def login():
    login_to_github = driver.find_elements_by_xpath("//*[@id='login_field']")[0]
    #Github username
    login_to_github.send_keys('')
    login_to_github = driver.find_elements_by_xpath("//*[@id='password']")[0]
    #Github Password
    login_to_github.send_keys('')
    login_to_github = driver.find_elements_by_xpath("//*[@id='login']/form/div[4]/input[9]")[0]
    login_to_github.click()
    driver.get('https://github.com/new')
    create_new_repo = driver.find_elements_by_xpath("//*[@id='repository_name']")[0]
    create_new_repo.send_keys(repo_name)
    #Sleep to make Create Repository Button active
    time.sleep(1)
    create_new_repo = driver.find_elements_by_xpath("//*[@id='new_repository']/div[3]/button")[0]
    create_new_repo.click()


if __name__ == "__main__":
    login()
