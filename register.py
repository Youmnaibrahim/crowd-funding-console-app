
def registeration():
    firstname = check()
    lastname = check()
    passwrd = password()
    email = input("Enter your email: ")
    num = checknumber()
    all = f"{firstname}:{lastname}:{passwrd}:{email}:{num}\n"
    append(all)

def login():
    email = input("Enter your email\n")
    password = input("Enter your password\n")
    try:
        fileobject = open("user.txt","r")
    except Exception as e:
        print(e)
    else:
        users = fileobject.readlines()
        for u in users:
            usrinfo = u.strip("\n")
            final = usrinfo.split(":")
            if final[3] == email and final[2] == password:
                print("Login successfully")
                break
            else:
                main()


def check():
    while True:
        x = input("Enter your name: ")
        if x.isalpha() and not x.isspace():
            return x
            break
        else:
            print("invalid")

def password():
    while True:
        p1 = input("Enter your password: ")
        p2 = input("Rewrite your password: ")
        if p1 == p2:
            return p1
            break
        else:
            print("unmatched")

def checknumber():
    while True:
        num = input("Enter your number: ")
        if num.isdigit():
            return num
            break
        else:
            print("Invalid try again")


def main():
    ask = input("1) login\n2)signup\n")
    ask = int(ask)
    if ask == 1:
        login()
    elif ask == 2:
        registeration()
    else:
        main()

def append(x):
    try:
        fileobject = open("user.txt","a")
    except Exception as e:
        print(e)
    else:
        fileobject.write(x)