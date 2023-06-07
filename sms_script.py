# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 20:16:02 2023

@author: asadbek
"""

import pyautogui
import time

print("Ishlamoqda.....")

def sms_jonat():
    xabar = input("Xabar yozing\n>>")
    nechta = int(input("Nechta xabar jo'natilsin>>\n"))
    time.sleep(10)
    
    
    for i in range(nechta):
        pass
    while nechta > 0:
        nechta -=1
    
        pyautogui.typewrite(xabar.strip())
        pyautogui.press('enter')
        
sms_jonat()        
        