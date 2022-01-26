#!/usr/bin/env python3
import webbrowser
import schedule
import time
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

# gets zoom links from dotenv file
C1 = os.environ.get('C1') 
C2 = os.environ.get('C2')
C3 = os.environ.get('C3')
C4 = os.environ.get('C4')
C5 = os.environ.get('C5')


# opens zoom links
def open_link(link):
    webbrowser.open(link, new=1)    # opens link


def course_1():
    open_link(C1)


def course_2():
    open_link(C2)


def course_3():
    open_link(C3)


def course_4():
    open_link(C4)


def course_5():
    open_link(C5)


# CHANGE DATES AND TIMES FOR ZOOM MEETINGS
schedule.every().monday.at("10:00").do(C1)
schedule.every().wednesday.at("10:00").do(C1)

schedule.every().monday.at("11:00").do(C2)
schedule.every().wednesday.at("11:00").do(C2)

schedule.every().monday.at("12:00").do(C3)
schedule.every().wednesday.at("12:00").do(C3)

schedule.every().monday.at("13:00").do(C4)
schedule.every().wednesday.at("13:00").do(C4)

schedule.every().tuesday.at("14:00").do(C5)
schedule.every().thursday.at("14:00").do(C5)


while True:
    schedule.run_pending()
    time.sleep(1)

