import re
from datetime import datetime

def first_page():
    try:
        print("\n$$ Welcome To Charity Projects $$")
        first_input=input("1- Login\n2- Sign up\nEnter choice your: ")
        if int(first_input)==1:
            print("\n##Login page##\n")
            login()
        elif int(first_input)==2:
            print("\n##Sign up page##\n")
            signup()
        else:
            first_page()
    except:
        first_page()
        ################################# helpful check functions #####################
def check_user_email(x):
    file_user_r=open("user.txt", "r")
    for line in file_user_r:
        if x in line:
            print("!! Already used E-mail !!")
            enter_mail()
        else:
            pass
