import os
import time
try:
    from pytube import Playlist
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
except ModuleNotFoundError:
    os.system('pip install pytube')
    os.system('pip install selenium')
    os.system('pip install  webdriver-manager[chromium]')

playlist=input('Enter the playlist URL : ')
playlist = Playlist(playlist)
urls=[]

for video in playlist:
    urls.append(video)

with open('urls.txt','w') as f:
    for url in urls:
        f.write(str(url+'\n'))

opt = Options()
opt.add_extension("5.18.0_0.crx")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
time.sleep(10)

driver.get("https://yt1s.com/en600/youtube-to-mp3")

url_input=driver.find_element(By.ID,"s_input")
with open('urls.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        cleaned_line = line.strip()
        url_input=driver.find_element(By.ID,"s_input")
        url_input.send_keys(cleaned_line+Keys.ENTER)

        WebDriverWait(driver, float('inf')).until(EC.element_to_be_clickable((By.ID, "btn-action"))).click()
        WebDriverWait(driver, float('inf')).until(EC.element_to_be_clickable((By.ID, "asuccess"))).click()
        WebDriverWait(driver, float('inf')).until(EC.element_to_be_clickable((By.ID, "cnext"))).click()

time.sleep(10)
driver.quit()