from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep as sl

"""
Harris Benedict

BMR = 66.5 + (13.75 * weight in kg) + (5.003 * height in cm) - (6.75 * age)
"""

BMR = 66.5 + (13.75 * 118) + (5.003 * 184) - (6.75 * 29)

print(BMR)