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
def check_user_phone(x):
    file_user_r=open("user.txt", "r")
    for line in file_user_r:
        if x in line:
            print("!! Already used phone number !!")
            phone_number()
        else:
            pass
        
        ##########################################################

def check_project_title(x):
    file_user_r=open("project.txt", "r")
    for line in file_user_r:
        if x in line:
            print("!! Already used title !!")
            project_create()
        else:
            
            

            ############################################# signup sub_page functions #########################################
def user_name():
    first_name=input("Please enter first name: ")
    last_name=input("Please enter last name: ")
    file_user=open("user.txt", "a")
    file_user.write("\n"+first_name+" "+last_name+":")
    