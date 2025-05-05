
from selenium import webdriver
import pyautogui
import time
import threading

import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from gologin import GoLogin
from gologin import getRandomPort
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pyautogui import typewrite,press,scroll
import random
from subprocess import CREATE_NO_WINDOW
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def scrldown(driver):
	html = driver.find_element(By.TAG_NAME,"html")
	html.send_keys(Keys.PAGE_DOWN)
def scrlup(driver):
	html = driver.find_element(By.TAG_NAME,"html")
	html.send_keys(Keys.PAGE_UP)
def darrow(driver):
	darrow=driver.find_element(By.TAG_NAME,"html")
	darrow.send_keys(Keys.ARROW_DOWN)
	time.sleep(random.randint(2,10))
def moregame(driver):
	moreg=driver.find_element(By.XPATH,'//img[@alt="more games"]')
	moreg.click()
	time.sleep(random.randint(2,10))
	randg=driver.find_elements(By.XPATH,'//img[@style="width: 26px;"]')
	r=random.choice(randg)
	r.click()
	time.sleep(random.randint(2,10))

def notmoreg(driver):
	showg=driver.find_elements(By.XPATH,'//span[@style="text-transform: capitalize;"]')
	r=random.choice(showg)
	r.click()
	time.sleep(random.randint(2,10))
def gamec(driver):
	darrow=driver.find_element(By.TAG_NAME,"html")
	for i in range(0,20):
		darrow.send_keys(Keys.ARROW_DOWN)
		
	gamec=driver.find_elements(By.XPATH,'//div[@class="game-card undefined"]')
	print(len(gamec))
	r=random.choice(gamec)
	r.click()
	time.sleep(random.randint(9,16))
	for i in range(0,14):
		darrow.send_keys(Keys.ARROW_DOWN)
	time.sleep(10)
	try:
		driver.implicitly_wait(3)
		btn=driver.find_element(By.XPATH,'//*[@id="gameframe"]')
		driver.switch_to.frame(btn)


		element = driver.find_element(By.XPATH,'//button[@id="pluto-splash-button"]')

		element.click()


		driver.switch_to.default_content()

	except:
		pass
	time.sleep(random.randint(10,25))
	




	

path=open("path.txt", 'r')
ids=(open("ids.txt", 'r').read()).split('\n')
links=(open("links.txt","r").read()).split("\n")
print(ids)
k=path.read()
print(k)


# Define a function to be called by each browser window
def do_task(browser_num, url):


    i=random.choice(ids)
    print(f'{i}')
    time.sleep(4)
    gl = GoLogin({
        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MzQ5NzVlZGNhZDI1NjM1MzM0N2VmYmEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NDM1NDc2NjMzZGZmZjBhOTRjMDA0NTQifQ.6xdaRZW4maqO1OZlHzu8-dfkSKIIcXStj9i2ESxB8no',
        'profile_id': i,
        'executable_path': k,
        # "port": random_port
        })

    debugger_address = gl.start()
    chrome_options = Options()
    chrome_options.add_argument('--disable-extensions') # Disable extensions
    chrome_options.add_argument('--incognito') # Open in incognito mode
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_experimental_option("debuggerAddress", debugger_address)
    chrome_service = Service('chromedriver')	
    chrome_service.creationflags = CREATE_NO_WINDOW
    driver = webdriver.Chrome(options=chrome_options,service=chrome_service)
    driver.get("https://www.youtube.com/")
    time.sleep(9)
    driver.get("https://www.youtube.com/")
    # create an ActionChains object
    typewrite("14a425b93e311")
    press('enter')
    time.sleep(4)
    actions = ActionChains(driver)
    # simulate typing without targeting a specific element

    time.sleep(3)
    typewrite("14a425b93e311")
    press('tab')
    typewrite("5787a861e6")
    press('tab')
    press('enter')
    time.sleep(3)
    for m in links:
        driver.get(m)
        time.sleep(random.randint(7,14))
        o=random.randint(15,34)
        time.sleep(8)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        fnlist=[scrldown,scrlup,moregame,notmoreg,gamec]
        for i in range(0,o):
            time.sleep(random.randint(5,7))
            try:
                random.choice(fnlist)(driver)
            except:
                time.sleep(random.randint(7,25))
                driver.get(m)
                typewrite("14a425b93e311")
                press('tab')
                typewrite("5787a861e6")
                press('tab')
                press('enter')

            
        time.sleep(3)


    time.sleep(random.randint(7,15))
    driver.close()

    time.sleep(3)
    gl.stop()

# Create a list of URLs to be used by each browser window
urls = ["https://stackoverflow.com","https://www.youtube.com"]

# Create a list of threads to be used for each browser window
threads = []

# Loop through each URL and create a separate thread for each browser window
for i, url in enumerate(urls):
    # Define a new thread for the current URL
    thread = threading.Thread(target=do_task, args=(i+1, url))
    time.sleep(2)
    thread.start()
    
    # Add the thread to the list of threads
    threads.append(thread)

# Wait for all threads to finish before continuing
for thread in threads:
    thread.join()



