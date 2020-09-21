from tkinter import *
from PIL import Image,ImageTk
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
from datetime import datetime, timedelta
import random



def wasd():
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")

    driver.implicitly_wait(5)

    serchbox = driver.find_element_by_name("username")
    serchbox.send_keys(Uname)

    password = driver.find_element_by_name("password")
    password.send_keys(Pword) 

    login = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]').click()

    driver.implicitly_wait(10)

    insta = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div/div').click()

    not_now = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

    send_message = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()

    sleep(5)


    driver.implicitly_wait(5)

    c = 0
    while 1:
        name_list = []
        for i in range(1, 6):
            name_list.append(driver.find_element_by_xpath(f'//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[{i}]/a'))
            action = ActionChains(driver)
            action.move_to_element(name_list[i-1])        
            nam = name_list[i-1].text.split()[0]
            action.click()
            action.perform()

            last_message = driver.find_elements_by_class_name('ZyFrc')
            if "hi" in last_message[-1].text.lower() and "(bot)" not in last_message[-1].text.lower():
                send_message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                send_message_box.send_keys(f"HI {nam} THIS IS SHADOW(BOT)")
                send_message_box.send_keys(Keys.RETURN)
            
            if "happy" in last_message[-1].text.lower() or "birth" in last_message[-1].text.lower() or "day" in last_message[-1].text.lower():
                send_message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                send_message_box.send_keys(f"THANK YOU SO MUCH {nam}, THIS IS SHADOW(BOT)")
                send_message_box.send_keys(Keys.RETURN)            

            if "hey shadow" in last_message[-1].text.lower() or "help" in last_message[-1].text.lower() and last_message[-1].text != "THIS WILL HEPL YOU":
                send_message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                send_message_box.send_keys("HOW CAN I HELP YOU :)")
                send_message_box.send_keys(Keys.RETURN)
                sleep(3)
                sec = 0
                while 1:
                    if sec >120:
                        break
                    lm = driver.find_elements_by_class_name('ZyFrc')[-1].text
                    print(lm)
                    if lm != "HOW CAN I HELP YOU :)":
                        break
                    sleep(1)
                    sec += 1

                if "HOW CAN I HELP YOU :)" in lm:
                    send_message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                    send_message_box.send_keys("HAVE A GOOD DAY  :)")
                    send_message_box.send_keys(Keys.RETURN)

                elif "what" in lm.lower() and "dowing" in lm.lower():
                    send_message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                    send_message_box.send_keys("TIME PASS")
                    send_message_box.send_keys(Keys.RETURN)

                elif "how are you" in lm.lower():
                    qw = random.randint(0, 100)
                    send_message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                    send_message_box.send_keys(F"I AM {qw}% FINE")
                    send_message_box.send_keys(Keys.RETURN)


                elif "what" in lm.lower() and "name" in lm.lower():
                    send_message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                    send_message_box.send_keys("THIS IS SHADOW(BOT)")
                    send_message_box.send_keys(Keys.RETURN)

                elif "what" in lm.lower() and "age" in lm.lower():
                    send_message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                    send_message_box.send_keys("19")
                    send_message_box.send_keys(Keys.RETURN)

                elif "where" in lm.lower() and "live" in lm.lower():
                    send_message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                    send_message_box.send_keys("MEHSANA")
                    send_message_box.send_keys(Keys.RETURN)

                elif "where" in lm.lower() and "study" in lm.lower():
                    send_message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                    send_message_box.send_keys("G.E.C. PATAN")
                    send_message_box.send_keys(Keys.RETURN)

                elif "what" in lm.lower() and "study" in lm.lower():
                    send_message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                    send_message_box.send_keys("COMPUTER SCIENCE")
                    send_message_box.send_keys(Keys.RETURN)

                elif "what" in lm.lower() and "real name" in lm.lower():
                    send_message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                    send_message_box.send_keys("MIHIR")
                    send_message_box.send_keys(Keys.RETURN)

                elif "what" in lm.lower() and "birth day" in lm.lower():
                    send_message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                    send_message_box.send_keys("29/05/2001")
                    send_message_box.send_keys(Keys.RETURN)

                elif "what" in lm.lower() and "hoby" in lm.lower():
                    send_message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                    send_message_box.send_keys("GAMING AND DROWING")
                    send_message_box.send_keys(Keys.RETURN)

                elif "favorite" in lm.lower() and "color" in lm.lower():
                    send_message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                    send_message_box.send_keys("BLACK")
                    send_message_box.send_keys(Keys.RETURN)

                else:
                    driver1 = webdriver.Chrome()
                    driver1.get('https://www.google.com/')
                    se_ba = driver1.find_element_by_name("q")
                    se_ba.send_keys(lm)
                    se_ba.send_keys(Keys.RETURN)
                    driver.implicitly_wait(5)
                    ans_text = driver1.find_element_by_class_name('s')
                    send_message_box.send_keys(ans_text.text)
                    send_message_box.send_keys(Keys.RETURN)
                    send_message_box.send_keys("TO READ MORE. --" + driver1.current_url)
                    send_message_box.send_keys(Keys.RETURN)
                    driver1.quit()
                    send_message_box.send_keys("THIS WILL HEPL YOU ")
                    send_message_box.send_keys(Keys.RETURN)
            
            driver.back()
            print(nam)
            print(c)
            c += 1

root = Tk()
root.title("AUTO REPLY BOT")
# root.iconbitmap('C:/Users/mihir/OneDrive/Desktop/python/SELENIUM/GUI/logo.ico')

def clicked():
    global Uname
    Uname = e1.get()
    global Pword
    Pword = e2.get()
    print(Uname, Pword)
    wasd()

lable1 = Label(root, text = "UserName ")
lable2 = Label(root, text = "Password: ")
e1 = Entry(root)
e2 = Entry(root)

lable1.grid(row = 0, column = 0)
lable2.grid(row = 1, column = 0)
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

enterButton = Button(root, text = "Log In", command = clicked, padx = 40)
enterButton.grid(row = 2, column = 0, columnspan = 2)



root.mainloop()