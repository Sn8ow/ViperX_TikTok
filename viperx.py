from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
from os import system
import time
from colorama import Fore, Back, Style

# if you have any issues with this contact me on discord
# MIMI#5103 discord.gg/zhCRERFRh7
# for educational purposes only C:


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options) # chrome driver more info on github
driver.set_window_size(1260, 720) # windows size changeable up to you


z = 0 # times
mode = 1 # mode 1 i will be adding more modes for likes and follows soon

def tool1():
    global z
    time.sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click() # views method button
    except:
        print(Fore.RED + 'Solve the Captcha!') # captcha alert
        driver.refresh() # site refresh
        tool1()
    try:
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/input").send_keys(vid) #site input text button
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/div/button").click() #site views button
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        driver.refresh() # site refresh
        z += 1
        total = z * 1000 # "z" is how many times you used the tool and basically 1000 views per 1z
        print(Fore.GREEN + 'Done! Total Views:', total,'views') # done views
        time.sleep(5)
        time.sleep(330) # 5min30sec timesleep because of 5min30sec cooldown
        tool1() # repeating
    except:
        print(Fore.RED + 'Timer isn´t finished yet! Trying again in 5 minutes.') # low chance that this will happen unless they changed time on site
        time.sleep(180)
        driver.refresh() # site refresh
        tool1() # starting loop




os.system('cls||clear') # clearing command prompt
print('''\r\n
██    ██ ██ ██████  ███████ ██████  ██   ██
██    ██ ██ ██   ██ ██      ██   ██  ██ ██
██    ██ ██ ██████  █████   ██████    ███ 
 ██  ██  ██ ██      ██      ██   ██  ██ ██ 
  ████   ██ ██      ███████ ██   ██ ██   ██
                  
┌─────────────────────────────────────────────────────┐
│                                                     │
│                                                     │
│                ViperX - Tik Tok Bot                 │
│                                                     │
│                                                     │
├─────────────────────────────────────────────────────┤
│               Credit: Sn8ow                         │
│     viewbot, comment liker, followbot, video liker  │
└─────────────────────────────────────────────────────┘\r\n''')

video = input('Video Link: ') # video link input
print("Solve the Captcha!") # captcha alert
time.sleep(6) # just time sleep for people to read the captcha alert
vid  = video # video link
os.system('cls||clear') # clearing command prompt

if mode == 1:
    driver.get("https://zefoy.com/") # driver getting the site
    tool1() # starting the loop
