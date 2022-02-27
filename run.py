#!/usr/bin/env python3

#import ต่างๆ
import os 
import sys
import time
import webbrowser
# from playsound import playsound


# ฟังชั้้นต่างๆ
def lowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0/90)

#ตัวแปลง
cr=('''\033[0;32m
╦═╗ ╦╦ ╦╔═╗╔═╗╦╔═╦ ╦╔═╗╦ ╦
╠╦╝ ║╠═╣╠═╣║  ╠╩╗╚╦╝║ ║║ ║
╩╚═╚╝╩ ╩╩ ╩╚═╝╩ ╩ ╩ ╚═╝╚═╝ o
=================================
Project จัดทำโดย Sakol Thaneerat ได้ดัดเเปลง ทำเพื่อเป็น Tool ในการใช้ได้ง่ายขึ้น 
สนับสนุน ได้ที่
            เพจ 
                ๏ https://bit.ly/3ptgTVs
                ๏ https://bit.ly/3Ijx9Bi
การสนับสนุนนี้จะนำมาพัฒนาโปรเจคต่างๆต่อไป ถ้าหากหมดเงินจากการบริจาคทางเราจะไม่ให้ใช้สคริปฟรีต่อไปจนกว่าจะได้เงินสนับสนุนไหม่อีกครั้ง 
''')

xr=("______________________________________________________")
xxx = ("================================================================================================================")
top=('''
 ██████╗██╗   ██╗ ██████╗ ███████╗██████╗     ███████╗ █████╗  ███████╗███████╗    
██╔════╝╚██╗ ██╔╝ ██╔══██╗██╔════╝██╔══██╗    ██╔════╝██╔══██╗ ██╔════╝██╔════╝    
██║      ╚████╔╝  ██████╔╝█████╗  ██████╔╝    ███████╗███████║ █████╗  █████╗      
██║       ╚██╔╝   ██╔══██╗██╔══╝  ██╔══██╗    ╚════██║██╔══██║ ██╔══╝  ██╔══╝      
╚██████╗   ██║    ██████╔╝███████╗██║  ██║    ███████║██║  ██║ ██║     ███████╗    
 ╚═════╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝ ╚═╝     ╚══════╝    
                                                                                 
''')

memu = ('''
            \33[32mM\33[33mE\33[35mM\33[37mU\33[35mS\33[32mY\33[36mS\33[33mT\33[32mE\33[35mM
\33[32m [ 1 ] \33[33m INSTALL 
\33[32m [ 2 ] \33[33m CR
\33[32m [ 3 ] \33[33m UPDATE
\33[32m [99 ] \33[33m EXIT

''')
os.system("clear")
lowprint(memu)
# playsound('1.mp3')
x = int(input("ENTER NEMBER : "))
if x == 1:#cr rj
    os.system("clear")
    lowprint(top)
    os.system("pkg install wget -y;apt install wget -y;cd $HOME;cd ..;cd usr;cd etc;rm -rf bash.bashrc;wget https://raw.githubusercontent.com/sakol289/bashterumxv1/main/bash.bashrc;exit")#crrj
    os.system("mv bannere.txt $HOME")
if x == 2:
    os.system("clear")
    lowprint(cr)
    lowprint(xr)
    input("PLESS ENTER : ")
if x == "3":
    os.system("git pull https://github.com/sakol289/bstermux")
    os.system("python3 run.py")
if x == 99:
    os.system("exit")#crrj
