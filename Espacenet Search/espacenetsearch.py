from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import pyautogui
# Moving mouse to upper LHS will break loop
pyautogui.FAILSAFE = True


browser = webdriver.Firefox()
# opens firefox
browser.get('https://worldwide.espacenet.com/advancedSearch?locale=en_EP')
# opens espacenet patent search webpage
searchElem = browser.find_element_by_css_selector('#abEditBox')
# creates elem based on title/abstract HTML element of webpage
searchElem.send_keys('pet devices')
# ' ' is the user entered search, current example will be pet device
searchElem.submit()
# selenium will find associated submit element to submit search

# checked the position of button to download results as a list
# position (696, 339)
# position is relative to screen used to compute
pyautogui.moveTo(696, 339, duration=3)
pyautogui.click(696, 339)

#clicking download file button
pyautogui.moveTo(740, 609, duration=3)
pyautogui.click(740, 609)

# closing webpage opened via selenium via geckodriver
browser.quit()




"""
This code requires Mozilla Firefox > vers60
This code requires geckodriver to run selenium module for Firefox

It uses an older version of espacenet which auto loads in search elements
--> unfortunately older vers only downloads 20 at a time therefore need to switch to new one;
    --> read total number by scraping info from webpage
    --> calc how many diff files that would require downloading
    --> max it out at 10,000 results say (20 files)
    --> merge data to master file
    --> extract data in meaningful way

Currently requires code specific input for search terms
--> need to be sys argv terms

Need a method to download csv of results
--> current method uses pyautogui to click download on opened espacenet website
--> better to use csv vs xls files as it allows easier/better data manipulation between file types (future-proofing)


Need to plot visuals of results in meaningful way
- number of patents
- pub date
- app date
- inventors
- applicants
- application number

"""
"""
THIS IS FOR XLS FILE OPERATIONS
# opening downloaded results file, how do I differentiate between one file and another
# using xlrd mod instead of openpyxl as it can handle older excel formats
workbook = xlrd.open_workbook('c:\\users\\jj\\downloads\\results.xls')

# test by checking cell values
# A13 = 'Dielectric ink composition' == (12, 0)
# xlrd reads cells by (row+1,column-1) both integer formats
value = worksheet.cell(12,0)
print(value)
"""
