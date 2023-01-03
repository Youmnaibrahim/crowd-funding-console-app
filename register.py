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
    

    def  enter_mail():
        global email
        email = input ("enter Email :" )
        r_email = r'^([a-z]|[0-9]|\-|\_|\+|\.)+\@([a-z]|[0-9]){2,}\.[a-z]{2,}(\.[a-z]{2,})?$'
        if(re.fullmatch(r_email, email)):
            check_user_email(email)
            print("Valid Email")
            file_user=open("user.txt", "a")
            file_user.write(email+":")
        else:
            print("!! Invalid Email !!")
            enter_mail()


def password():
    passwd=input("Please enter password: ")
    passwd_check=input("Please confirm password: ")
    if passwd==passwd_check:
        print("Correct password")
        file_user=open("user.txt", "a")
        file_user.write(passwd+":")
    else:
        print("!! Incorect password !!")
        password()

def phone_number():
    ph_numb=input("Please enter Egyptian phone number: ")
    r_ph_numb = r'^01[0125][0-9]{8}$'
    if(re.fullmatch(r_ph_numb, ph_numb)):
        check_user_phone(ph_numb)
        print("Valid Egyptian phone number")
        file_user=open("user.txt", "a")
        file_user.write(ph_numb+":")
    else:
        print("!! Invalid Egyptian phone number !!")
        phone_number()



        ############################################# login sub_page functions #########################################
def project():
    try:
        print("\n$$ Welcome $$\n")
        first_input=input("1- Create \n2- View \n3- back \nEnter choice your: ")
        if int(first_input)==1:
            project_create()
            project()
        elif int(first_input)==2:
            project_view()
        elif int(first_input)==3:
            print("")
            first_page()
        else:
            project()
    except:
        project()
