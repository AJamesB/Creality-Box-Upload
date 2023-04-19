from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys


# Uncomment the following line for automator quick action on Mac
# file =  sys.argv[1:]


# Uncomment the following lines to use file browser
# def file_input():
#     import tkinter as tk
#     from tkinter import filedialog
#     root = tk.Tk()
#     root.withdraw()
#     return filedialog.askopenfilename()
#
#
# file = file_input()


# Change the email and password to your Creality cloud login details
email = "email"
password = "password"

# Using Chrome to access web. If using Firefox change "Chrome" to "Firefox"
driver = webdriver.Chrome()

# Open the website
driver.get('https://www.crealitycloud.com/upload-gcode')

driver.implicitly_wait(10)
login_button = driver.find_element(By.CLASS_NAME, 'login-btn')
login_button.click()

wait = WebDriverWait(driver, 2)
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'el-dialog__body')))
username_box = driver.find_element(By.CLASS_NAME, 'email')
username = username_box.find_element(By.CLASS_NAME, 'el-input__inner')

username.clear()
username.send_keys(email)
driver.implicitly_wait(2)  # seconds

password_box = driver.find_element(By.CLASS_NAME, 'password')
password = password_box.find_element(By.CLASS_NAME, 'el-input__inner')
password.clear()
password.send_keys(password)
driver.implicitly_wait(2)  # seconds

log_in = driver.find_element(By.CLASS_NAME, 'el-button--primary')
log_in.click()

time.sleep(2)
driver.back()

upload_input = driver.find_element(By.CLASS_NAME, 'el-upload__input')

upload_input.send_keys(file)

cookies = driver.find_element(By.CLASS_NAME, 'cookies')
cookies_okay = cookies.find_element(By.CLASS_NAME, 'btn')
cookies_okay.click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'icon-edit')))

upload_button = driver.find_element(By.CLASS_NAME, 'submit-btn')

upload_button.click()

time.sleep(2)

# Quits the driver
driver.close()
driver.quit()
