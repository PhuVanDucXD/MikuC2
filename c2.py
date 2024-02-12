#VIETNAM SỜ CU RI TY#
import socket
import os
import requests
import random
import getpass
import time
import sys
name=input("UserName:")
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ascii_vro():
    clear()
    print(f'''
   ''')
    clear()
def banners():
    clear()    
    print(f"""
METHODS
CLEAR 
""")


    
def meth():        
    print(f'''
\x1b[38;5;55mHTTP-\x1b[1;37mBROWSER    \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mPORT\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTIME\x1b[38;5;55m]
\x1b[38;5;55mHTTP-\x1b[1;37mSPAM       \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mPORT\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTIME\x1b[38;5;55m]
\x1b[38;5;55mHTTP-\x1b[1;37mKILLER     \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mPORT\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTIME\x1b[38;5;55m]
\x1b[38;5;55mHTTP-\x1b[1;37mGET        \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mPORT\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTIME\x1b[38;5;55m]
\x1b[38;5;55mHTTP-\x1b[1;37mMERIS      \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mPORT\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTIME\x1b[38;5;55m]
\x1b[38;5;55mCLOUD\x1b[1;37mFLARE      \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mPORT\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTIME\x1b[38;5;55m]
\x1b[38;5;55mHTTP-\x1b[1;37mBYPASS     \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mPORT\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTIME\x1b[38;5;55m]
\x1b[38;5;55mHTTP-\x1b[1;37mFLOOD      \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mPORT\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTIME\x1b[38;5;55m]
''')

def menu():
    os.system("clear")
    print("""          
                        \x1b[1;37m╔╦╗ ╦ \x1b[38;5;55m╦╔═ ╦ ╦
                        \x1b[1;37m║║║ ║ \x1b[38;5;55m╠╩╗ ║ ║
                        \x1b[1;37m╩ ╩ ╩ \x1b[38;5;55m╩ ╚═╚═╝
                  \x1b[1;37m-Best C2 In\x1b[38;5;55m the Year 2024-
             \x1b[1;37m╚═╦══════════════\x1b[38;5;55m═══════════════╦═╝       
          \x1b[1;37m╚╦═══╩══════════════\x1b[38;5;55m═══════════════╩═══╦╝
    \x1b[1;37m╚╦═════╩══════════════════\x1b[38;5;55m═══════════════════╩══════╦╝
     \x1b[1;37m║        -Welcome To Miku\x1b[38;5;55mC2 Made By VanDuc-        ║
     \x1b[1;37m║             -Powerful L\x1b[38;5;55mayer7 Bypasser-           ║        
    \x1b[1;37m╔╩═╦══════════════════════\x1b[38;5;55m════════════════════════╦═╩╗
       \x1b[1;37m║            -PhuVanDuc\x1b[38;5;55m X Miku C2-             ║
      \x1b[1;37m╔╩══════════════════════\x1b[38;5;55m════════════════════════╩╗
      \x1b[1;37m║  _Copyright © 2024 Mik\x1b[38;5;55mu C2 All Right Reserved_ ║
     \x1b[1;37m╔╩═══════════════════════\x1b[38;5;55m═════════════════════════╩╗
      
    """)


def main():
    menu()
    while(True):
        cnc = input(f"\x1b[1;37m{name}@\x1b[38;5;55mAdmin\x1b[1;37m:~# ")
        if cnc == "methods" or cnc == "METHODS" or cnc == "METHOD" or cnc == "method":
            meth()                
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "help" or cnc == "HELP":
            help()



# LAYER 7 METHODS
 
        elif "HTTP-BROWSER" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3] 
                os.system("clear")
                print(f""" 
                 \x1b[1;37m╔═╗╔╦╗╔╦╗╔═╗╔═╗\x1b[38;5;55m╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
                 \x1b[1;37m╠═╣ ║  ║ ╠═╣║  \x1b[38;5;55m╠╩╗  ╚═╗║┤ ║║║ ║
                 \x1b[1;37m╩ ╩ ╩  ╩ ╩ ╩╚═╝\x1b[38;5;55m╩ ╩  ╚═╝╚═╝╝╚╝ ╩      
         \x1b[1;37m╚═══════╦══════════════\x1b[38;5;55m════════════════╦════════╝
       \x1b[1;37m╔═════════╩══════════════\x1b[38;5;55m════════════════╩══════════╗  
                 \x1b[1;37mTarget      × \x1b[38;5;55m[\x1b[1;37m{url}\x1b[38;5;55m]
                 \x1b[1;37mPort        × \x1b[38;5;55m[\x1b[1;37m{port}\x1b[38;5;55m]
                 \x1b[1;37mDuration    × \x1b[38;5;55m[\x1b[1;37m{time}\x1b[38;5;55m]
                 \x1b[1;37mMethod      × \x1b[38;5;55m[\x1b[1;37mHTTP-BROWSER\x1b[38;5;55m]
                 \x1b[1;37mUser        × \x1b[38;5;55m[\x1b[1;37m{name}\x1b[38;5;55m]
                 \x1b[1;37mVip         × \x1b[38;5;55m[\x1b[1;37mTRUE\x1b[38;5;55m]
       \x1b[1;37m╚═════════╦══════════════\x1b[38;5;55m═════════════════╦═════════╝
         \x1b[1;37m╔═══════╩══════════════\x1b[38;5;55m═════════════════╩═══════╗
                 \x1b[1;37mADMIN       × \x1b[38;5;55m[\x1b[1;37mPhuVanDuc\x1b[38;5;55m]
                 \x1b[1;37mPlan        × \x1b[38;5;55m[\x1b[1;37mSLIVER X VIP\x1b[38;5;55m]
         \x1b[1;37m╚══════════════════════\x1b[38;5;55m═════════════════════════╝  
               """)
               
                
            except IndexError:
                os.system("clear")
                menu()
        elif "HTTP-KILLER" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                clear()
                print(f"""
                 \x1b[1;37m╔═╗╔╦╗╔╦╗╔═╗╔═╗\x1b[38;5;55m╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
                 \x1b[1;37m╠═╣ ║  ║ ╠═╣║  \x1b[38;5;55m╠╩╗  ╚═╗║┤ ║║║ ║
                 \x1b[1;37m╩ ╩ ╩  ╩ ╩ ╩╚═╝\x1b[38;5;55m╩ ╩  ╚═╝╚═╝╝╚╝ ╩      
         \x1b[1;37m╚═══════╦══════════════\x1b[38;5;55m════════════════╦════════╝
       \x1b[1;37m╔═════════╩══════════════\x1b[38;5;55m════════════════╩══════════╗  
                 \x1b[1;37mTarget      × \x1b[38;5;55m[\x1b[1;37m{url}\x1b[38;5;55m]
                 \x1b[1;37mPort        × \x1b[38;5;55m[\x1b[1;37m{port}\x1b[38;5;55m]
                 \x1b[1;37mDuration    × \x1b[38;5;55m[\x1b[1;37m{time}\x1b[38;5;55m]
                 \x1b[1;37mMethod      × \x1b[38;5;55m[\x1b[1;37mHTTP-KILLER\x1b[38;5;55m]
                 \x1b[1;37mUser        × \x1b[38;5;55m[\x1b[1;37m{name}\x1b[38;5;55m]
                 \x1b[1;37mVip         × \x1b[38;5;55m[\x1b[1;37mTRUE\x1b[38;5;55m]
       \x1b[1;37m╚═════════╦══════════════\x1b[38;5;55m═════════════════╦═════════╝
         \x1b[1;37m╔═══════╩══════════════\x1b[38;5;55m═════════════════╩═══════╗
                 \x1b[1;37mADMIN       × \x1b[38;5;55m[\x1b[1;37mPhuVanDuc\x1b[38;5;55m]
                 \x1b[1;37mPlan        × \x1b[38;5;55m[\x1b[1;37mSLIVER X VIP\x1b[38;5;55m]
         \x1b[1;37m╚══════════════════════\x1b[38;5;55m═════════════════════════╝""")
               
                
            except IndexError:
                os.system("clear")
                menu()
        elif "HTTP-SPAM" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                clear()
                print(f"""
                 \x1b[1;37m╔═╗╔╦╗╔╦╗╔═╗╔═╗\x1b[38;5;55m╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
                 \x1b[1;37m╠═╣ ║  ║ ╠═╣║  \x1b[38;5;55m╠╩╗  ╚═╗║┤ ║║║ ║
                 \x1b[1;37m╩ ╩ ╩  ╩ ╩ ╩╚═╝\x1b[38;5;55m╩ ╩  ╚═╝╚═╝╝╚╝ ╩      
         \x1b[1;37m╚═══════╦══════════════\x1b[38;5;55m════════════════╦════════╝
       \x1b[1;37m╔═════════╩══════════════\x1b[38;5;55m════════════════╩══════════╗  
                 \x1b[1;37mTarget      × \x1b[38;5;55m[\x1b[1;37m{url}\x1b[38;5;55m]
                 \x1b[1;37mPort        × \x1b[38;5;55m[\x1b[1;37m{port}\x1b[38;5;55m]
                 \x1b[1;37mDuration    × \x1b[38;5;55m[\x1b[1;37m{time}\x1b[38;5;55m]
                 \x1b[1;37mMethod      × \x1b[38;5;55m[\x1b[1;37mHTTP-SPAM\x1b[38;5;55m]
                 \x1b[1;37mUser        × \x1b[38;5;55m[\x1b[1;37m{name}\x1b[38;5;55m]
                 \x1b[1;37mVip         × \x1b[38;5;55m[\x1b[1;37mTRUE\x1b[38;5;55m]
       \x1b[1;37m╚═════════╦══════════════\x1b[38;5;55m═════════════════╦═════════╝
         \x1b[1;37m╔═══════╩══════════════\x1b[38;5;55m═════════════════╩═══════╗
                 \x1b[1;37mADMIN       × \x1b[38;5;55m[\x1b[1;37mPhuVanDuc\x1b[38;5;55m]
                 \x1b[1;37mPlan        × \x1b[38;5;55m[\x1b[1;37mSLIVER X VIP\x1b[38;5;55m]
         \x1b[1;37m╚══════════════════════\x1b[38;5;55m═════════════════════════╝""")
               
                
            except IndexError:
                os.system("clear")
                menu()
        elif "HTTP-GET" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                clear()
                print(f"""
                 \x1b[1;37m╔═╗╔╦╗╔╦╗╔═╗╔═╗\x1b[38;5;55m╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
                 \x1b[1;37m╠═╣ ║  ║ ╠═╣║  \x1b[38;5;55m╠╩╗  ╚═╗║┤ ║║║ ║
                 \x1b[1;37m╩ ╩ ╩  ╩ ╩ ╩╚═╝\x1b[38;5;55m╩ ╩  ╚═╝╚═╝╝╚╝ ╩      
         \x1b[1;37m╚═══════╦══════════════\x1b[38;5;55m════════════════╦════════╝
       \x1b[1;37m╔═════════╩══════════════\x1b[38;5;55m════════════════╩══════════╗  
                 \x1b[1;37mTarget      × \x1b[38;5;55m[\x1b[1;37m{url}\x1b[38;5;55m]
                 \x1b[1;37mPort        × \x1b[38;5;55m[\x1b[1;37m{port}\x1b[38;5;55m]
                 \x1b[1;37mDuration    × \x1b[38;5;55m[\x1b[1;37m{time}\x1b[38;5;55m]
                 \x1b[1;37mMethod      × \x1b[38;5;55m[\x1b[1;37mHTTP-GET\x1b[38;5;55m]
                 \x1b[1;37mUser        × \x1b[38;5;55m[\x1b[1;37m{name}\x1b[38;5;55m]
                 \x1b[1;37mVip         × \x1b[38;5;55m[\x1b[1;37mTRUE\x1b[38;5;55m]
       \x1b[1;37m╚═════════╦══════════════\x1b[38;5;55m═════════════════╦═════════╝
         \x1b[1;37m╔═══════╩══════════════\x1b[38;5;55m═════════════════╩═══════╗
                 \x1b[1;37mADMIN       × \x1b[38;5;55m[\x1b[1;37mPhuVanDuc\x1b[38;5;55m]
                 \x1b[1;37mPlan        × \x1b[38;5;55m[\x1b[1;37mSLIVER X VIP\x1b[38;5;55m]
         \x1b[1;37m╚══════════════════════\x1b[38;5;55m═════════════════════════╝ 
               """)
               
                
            except IndexError:
                os.system("clear")
                menu()
                
       
    
        elif "CLOUDFLARE" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                print(f"""
                 \x1b[1;37m╔═╗╔╦╗╔╦╗╔═╗╔═╗\x1b[38;5;55m╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
                 \x1b[1;37m╠═╣ ║  ║ ╠═╣║  \x1b[38;5;55m╠╩╗  ╚═╗║┤ ║║║ ║
                 \x1b[1;37m╩ ╩ ╩  ╩ ╩ ╩╚═╝\x1b[38;5;55m╩ ╩  ╚═╝╚═╝╝╚╝ ╩      
         \x1b[1;37m╚═══════╦══════════════\x1b[38;5;55m════════════════╦════════╝
       \x1b[1;37m╔═════════╩══════════════\x1b[38;5;55m════════════════╩══════════╗  
                 \x1b[1;37mTarget      × \x1b[38;5;55m[\x1b[1;37m{url}\x1b[38;5;55m]
                 \x1b[1;37mPort        × \x1b[38;5;55m[\x1b[1;37m{port}\x1b[38;5;55m]
                 \x1b[1;37mDuration    × \x1b[38;5;55m[\x1b[1;37m{time}\x1b[38;5;55m]
                 \x1b[1;37mMethod      × \x1b[38;5;55m[\x1b[1;37mCLOUDFLARE\x1b[38;5;55m]
                 \x1b[1;37mUser        × \x1b[38;5;55m[\x1b[1;37m{name}\x1b[38;5;55m]
                 \x1b[1;37mVip         × \x1b[38;5;55m[\x1b[1;37mTRUE\x1b[38;5;55m]
       \x1b[1;37m╚═════════╦══════════════\x1b[38;5;55m═════════════════╦═════════╝
         \x1b[1;37m╔═══════╩══════════════\x1b[38;5;55m═════════════════╩═══════╗
                 \x1b[1;37mADMIN       × \x1b[38;5;55m[\x1b[1;37mPhuVanDuc\x1b[38;5;55m]
                 \x1b[1;37mPlan        × \x1b[38;5;55m[\x1b[1;37mSLIVER X VIP\x1b[38;5;55m]
         \x1b[1;37m╚══════════════════════\x1b[38;5;55m═════════════════════════╝
               """)
               
                
            except IndexError:
                os.system("clear")
                menu()
        elif "HTTP-MERIS" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                clear()
                print(f"""
                 \x1b[1;37m╔═╗╔╦╗╔╦╗╔═╗╔═╗\x1b[38;5;55m╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
                 \x1b[1;37m╠═╣ ║  ║ ╠═╣║  \x1b[38;5;55m╠╩╗  ╚═╗║┤ ║║║ ║
                 \x1b[1;37m╩ ╩ ╩  ╩ ╩ ╩╚═╝\x1b[38;5;55m╩ ╩  ╚═╝╚═╝╝╚╝ ╩      
         \x1b[1;37m╚═══════╦══════════════\x1b[38;5;55m════════════════╦════════╝
       \x1b[1;37m╔═════════╩══════════════\x1b[38;5;55m════════════════╩══════════╗  
                 \x1b[1;37mTarget      × \x1b[38;5;55m[\x1b[1;37m{url}\x1b[38;5;55m]
                 \x1b[1;37mPort        × \x1b[38;5;55m[\x1b[1;37m{port}\x1b[38;5;55m]
                 \x1b[1;37mDuration    × \x1b[38;5;55m[\x1b[1;37m{time}\x1b[38;5;55m]
                 \x1b[1;37mMethod      × \x1b[38;5;55m[\x1b[1;37mHTTP-MERIS\x1b[38;5;55m]
                 \x1b[1;37mUser        × \x1b[38;5;55m[\x1b[1;37m{name}\x1b[38;5;55m]
                 \x1b[1;37mVip         × \x1b[38;5;55m[\x1b[1;37mTRUE\x1b[38;5;55m]
       \x1b[1;37m╚═════════╦══════════════\x1b[38;5;55m═════════════════╦═════════╝
         \x1b[1;37m╔═══════╩══════════════\x1b[38;5;55m═════════════════╩═══════╗
                 \x1b[1;37mADMIN       × \x1b[38;5;55m[\x1b[1;37mPhuVanDuc\x1b[38;5;55m]
                 \x1b[1;37mPlan        × \x1b[38;5;55m[\x1b[1;37mSLIVER X VIP\x1b[38;5;55m]
         \x1b[1;37m╚══════════════════════\x1b[38;5;55m═════════════════════════╝
               """)
               
                
            except IndexError:
                os.system("clear")
                menu()
        elif "HTTP-FLOOD" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                clear()
                print(f"""
                 \x1b[1;37m╔═╗╔╦╗╔╦╗╔═╗╔═╗\x1b[38;5;55m╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
                 \x1b[1;37m╠═╣ ║  ║ ╠═╣║  \x1b[38;5;55m╠╩╗  ╚═╗║┤ ║║║ ║
                 \x1b[1;37m╩ ╩ ╩  ╩ ╩ ╩╚═╝\x1b[38;5;55m╩ ╩  ╚═╝╚═╝╝╚╝ ╩      
         \x1b[1;37m╚═══════╦══════════════\x1b[38;5;55m════════════════╦════════╝
       \x1b[1;37m╔═════════╩══════════════\x1b[38;5;55m════════════════╩══════════╗  
                 \x1b[1;37mTarget      × \x1b[38;5;55m[\x1b[1;37m{url}\x1b[38;5;55m]
                 \x1b[1;37mPort        × \x1b[38;5;55m[\x1b[1;37m{port}\x1b[38;5;55m]
                 \x1b[1;37mDuration    × \x1b[38;5;55m[\x1b[1;37m{time}\x1b[38;5;55m]
                 \x1b[1;37mMethod      × \x1b[38;5;55m[\x1b[1;37mHTTP-FLOOD\x1b[38;5;55m]
                 \x1b[1;37mUser        × \x1b[38;5;55m[\x1b[1;37m{name}\x1b[38;5;55m]
                 \x1b[1;37mVip         × \x1b[38;5;55m[\x1b[1;37mTRUE\x1b[38;5;55m]
       \x1b[1;37m╚═════════╦══════════════\x1b[38;5;55m═════════════════╦═════════╝
         \x1b[1;37m╔═══════╩══════════════\x1b[38;5;55m═════════════════╩═══════╗
                 \x1b[1;37mADMIN       × \x1b[38;5;55m[\x1b[1;37mPhuVanDuc\x1b[38;5;55m]
                 \x1b[1;37mPlan        × \x1b[38;5;55m[\x1b[1;37mSLIVER X VIP\x1b[38;5;55m]
         \x1b[1;37m╚══════════════════════\x1b[38;5;55m═════════════════════════╝
               """)
               
                
            except IndexError:
                os.system("clear")
                menu()
        
        elif "HTTP-BYPASS" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                clear()
                print(f"""
                 \x1b[1;37m╔═╗╔╦╗╔╦╗╔═╗╔═╗\x1b[38;5;55m╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
                 \x1b[1;37m╠═╣ ║  ║ ╠═╣║  \x1b[38;5;55m╠╩╗  ╚═╗║┤ ║║║ ║
                 \x1b[1;37m╩ ╩ ╩  ╩ ╩ ╩╚═╝\x1b[38;5;55m╩ ╩  ╚═╝╚═╝╝╚╝ ╩      
         \x1b[1;37m╚═══════╦══════════════\x1b[38;5;55m════════════════╦════════╝
       \x1b[1;37m╔═════════╩══════════════\x1b[38;5;55m════════════════╩══════════╗  
                 \x1b[1;37mTarget      × \x1b[38;5;55m[\x1b[1;37m{url}\x1b[38;5;55m]
                 \x1b[1;37mPort        × \x1b[38;5;55m[\x1b[1;37m{port}\x1b[38;5;55m]
                 \x1b[1;37mDuration    × \x1b[38;5;55m[\x1b[1;37m{time}\x1b[38;5;55m]
                 \x1b[1;37mMethod      × \x1b[38;5;55m[\x1b[1;37mHTTP-BYPASS\x1b[38;5;55m]
                 \x1b[1;37mUser        × \x1b[38;5;55m[\x1b[1;37m{name}\x1b[38;5;55m]
                 \x1b[1;37mVip         × \x1b[38;5;55m[\x1b[1;37mTRUE\x1b[38;5;55m]
       \x1b[1;37m╚═════════╦══════════════\x1b[38;5;55m═════════════════╦═════════╝
         \x1b[1;37m╔═══════╩══════════════\x1b[38;5;55m═════════════════╩═══════╗
                 \x1b[1;37mADMIN       × \x1b[38;5;55m[\x1b[1;37mPhuVanDuc\x1b[38;5;55m]
                 \x1b[1;37mPlan        × \x1b[38;5;55m[\x1b[1;37mSLIVER X VIP\x1b[38;5;55m]
         \x1b[1;37m╚══════════════════════\x1b[38;5;55m═════════════════════════╝ 
               """)
               
                
            except IndexError:
                os.system("clear")
                menu()
                                         
        

        else:
            try:
                cmmnd = cnc.split()[0]
                print(os.system("clear"))
                menu()
            except IndexError:
                pass


def login():
    clear()
    user = "PhuVanDuc"
    passwd = "MikuC2"
    username = input("Username: ")
    password = getpass.getpass(prompt='Password: ')
    if username != user or password != passwd:
        print("")
        print("Fail")
        sys.exit(1)
    elif username == user and password == passwd:
        print("Welcome To MikuC2")
        time.sleep(0.3)
        ascii_vro()
        main()

login()
