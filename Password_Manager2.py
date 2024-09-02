#Password Manager

import mysql.connector,time,sys

mydb = mysql.connector.connect(host = 'localhost',user='root',password="Apc@2007#CS", database = 'password_manager2')

 
mycursor = mydb.cursor()

#Fetching Values from my cursor:
mycursor.execute("SELECT * FROM manager")
values = mycursor.fetchall()


def login():
    user,pas = "kami ","1234"
    while True:
        username = input("Enter Login Username > ")
        password = input("Enter Login Password > ")

        # Validation
        if username == user and password == pas:
            print("Login Successful !!!\n")

            print("Redirecting to homepage in (3)"),time.sleep(1)
            print("Redirecting to homepage in (2)"),time.sleep(1)
            print("Redirecting to homepage in (1)\n"),time.sleep(1)
            display_all()
            break

        else:
            print("Wrong Username/Password !!! ")
            time.sleep(2)

def home_page():
    print("In home page !!!!")

def display_all():
    global mycursor
    #Getting maximum column values

    mycursor.execute("SELECT MAX(CHAR_LENGTH(website)) FROM manager")
    max_web = int(mycursor.fetchone()[0]) + 5

    mycursor.execute("SELECT MAX(CHAR_LENGTH(username)) FROM manager")
    max_user = int(mycursor.fetchone()[0]) + 5 

    mycursor.execute("SELECT MAX(CHAR_LENGTH(password)) FROM manager")
    max_pass = int(mycursor.fetchone()[0]) + 5


    # Table
    web,user,pas = "Website","Username","Password"


    #Checking if maximum value in the column is less than the header and if so then setting column width 
    # *2 because while printing values the max_x will be subracted by the len(x) and in case x = max_x the re
    if (max_web) <  len(web): 
        max_web = len(web) + 5

    if (max_user) <  len(user):
        max_user = len(user) + 5

    if (max_pass) <  len(pas):
        max_pass = len(pas) + 5


    # Table Header Start Outline

    print("+"+("-"*(max_web+1)),end='')
    print("+"+("-"*(max_user+1)),end='')
    print("+"+("-"*(max_pass))+"-+")


    #Resetting cursor
    mycursor.close()
    mycursor = mydb.cursor()

    #TABLE CONTENTS
    mycursor.execute("SELECT * FROM manager")
    values = mycursor.fetchall() 

    # Table Header
    print("| " + (web+" "*(max_web-len(web))),end='')
    print("| " + (user+" "*(max_user-len(user))),end='')
    print("| " + (pas+" "*(max_pass-len(pas))) + "|")

    #Table Header End Outline
    print("+"+("-"*(max_web+1)),end='')
    print("+"+("-"*(max_user+1)),end='')
    print("+"+("-"*(max_pass))+"-+")


    for value in values:
        
        website = value[0]
        username = value[1]
        password = value[2]

        print("| " + (website+" "*(max_web-len(website))),end='')
        print("| " + (username+" "*(max_user-len(username))),end='')
        print("| " + (password+" "*(max_pass-len(password))) + "|")

    #Table End outline
    print("+"+("-"*(max_web+1)),end='')
    print("+"+("-"*(max_user+1)),end='')
    print("+"+("-"*(max_pass))+"-+")

login()