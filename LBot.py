from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pag
import time

# -------------------------------------- INPUTS WHICH WILL BE IN GUI ---------------------------------

#username = input("Type your username : ")
#password = input("Type your password : ")
#word = input("What you would like to search : ")
#3con = []
#z = int(input("how many Connections ?"))
#for i in range(z):
	#temp = int(input("Connections Please"))
	#con.append(temp)

# ------------------------------------------- BROWSER DRIVER --------------------------------------------

driver = webdriver.Firefox(executable_path = r"Z:\SORTING VISUAL\LINKEDIN-Bot\drivers\geckodriver.exe")

# --------------------------------- URL FOR LINKEDIN SIGNIN PAGE ----------------------------------------

url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"

driver.get(url)

# -------------------------------------- LOGIN YOUR ACCOUNT ---------------------------------------------

time.sleep(4)
driver.find_element_by_id('username').send_keys("Parmeet757@gmail.com")
driver.find_element_by_id('password').send_keys("meonLINKEDIN7")
driver.find_element_by_id('password').send_keys(Keys.RETURN)

time.sleep(4)

# ---------------------------------------- SEARCH FOR KEYWORD -------------------------------------------

def search():
	time.sleep(8)
	driver.find_element_by_xpath("//input[@placeholder='Search']").click()
	driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys("Python")
	driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(Keys.RETURN)


# -------------------------------------------- FILTERS ---------------------------------------------------

# ------------------------------------------- CONNECTIONS ------------------------------------------------
def Con():
	
	time.sleep(4)
	driver.find_element_by_xpath("//span[text()='Connections']").click()
	if 1 in con:
		driver.find_element_by_xpath("//span[text()='1st']").click()

	if 2 in con:
		driver.find_element_by_xpath("//span[text()='2nd']").click()

	if 3 in con:
		driver.find_element_by_xpath("//span[text()='3rd+']").click()

	time.sleep(2)
	pag.click(730,610)

# ------------------------------------------ LOCATION -----------------------------------------------------

def Location():
	#USE LIST FOR MULTIPLE COUNTRY INPUTS AFTER GUI
	time.sleep(4)
	driver.find_element_by_xpath("//span[text()='Locations']").click()
	driver.find_element_by_xpath("//input[@placeholder='Add a country/region']").send_keys('India')
	pag.click(420,400)
	#Apply Button instead of pag


# -----------------------------------------

search()
#Con()
Location()
time.sleep(3)

