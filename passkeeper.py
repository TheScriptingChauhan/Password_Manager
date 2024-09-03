#Password Manager

import mysql.connector,time 

global mycursor, mydb

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
            print("\nLogin Successful !!!\n")

            main()
            return

        else:
            print("\nWrong Username/Password !!! \n")


def display_all():
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

    time.sleep(2)

def specific(web = False,user = False):  # To delete / display a specific record 

    while True:
        if not web or not user:
            web = input("Enter Website Name >>> ").strip()
            user = input("Enter The Website Username / Email >>> ").strip()

            if not web or not user:
                print("Website and Username/Email cannot be empty.")
                continue  # Continue the loop to prompt the user again
        
        # Check if the record exists in the database
        
        query = "SELECT * FROM manager WHERE Website = %s AND Username = %s"
        val = (web, user)
        
        mycursor.execute(query, val)
        rec = mycursor.fetchone()  

        if rec:
           print("Rec Found !!\n ")
           return rec,val
        
        else:
            print("No matching record found for the provided Website and Username/Email. \n")
            web,user = False,False


def delete():
    
            rec,val = specific()

            web ,user = val[0],val[1]
     
            delete_query = "DELETE FROM manager WHERE Website = %s AND Username = %s"
 
            mycursor.execute(delete_query, val)
            mydb.commit()  
 
            print(f"Deleted record for Website: {web} and Username/Email: {user}\n")

            while True:
                
                ch = input("Do you want to delete another record? (y/n): ").lower()
                
                if ch == "y":
                    time.sleep(2)
                    break  # Break the inner loop to continue deleting more records
                
                elif ch == "n":
                    time.sleep(2)
                    return  # Exit the function
                
                else:
                    print("Invalid input, please enter Y or N.")


def display_specific():

    while True:
        rec,val = specific()

        print("\nRecord Found : \n")
        print(f"Website : {rec[0]}")
        print(f"Username : {rec[1]}")
        print(f"Password : {rec[2]}\n")

        while True:
            ch = input("Do you want to search more records? (y/n)").lower()

            if ch == 'y':
                time.sleep(2)
                break # Break the inner loop to continue deleting more records
            
            elif ch == 'n':
                time.sleep(2)
                return # Exit the function
            
            else:
                print("Invalid input, please enter Y or N.")

def display():
    global mycursor  # Ensure mycursor is defined globally or passed to the function

    print("\nDo you want to display all records with the same: ")
    
    while True:
        try:
            ch = int(input("1. Website \n2. Username/Mail \n>>> "))
            if ch not in [1, 2]:
                print("Choose either 1 or 2.")
                continue
            break
        except ValueError:
            print("Choose either 1 or 2.")
            continue 

    if ch == 1:
        web_name = input("Enter Website Name: ").strip()
        query = "SELECT * FROM manager WHERE Website = %s"
        val = (web_name,)
        
    elif ch == 2:
        user = input("Enter Username / MailID: ").strip()
        query = "SELECT * FROM manager WHERE Username = %s"
        val = (user,)

    mycursor.execute(query, val)
    rec = mycursor.fetchall()

    if rec:
        for i in rec:
            print(f"\nWebsite: {i[0]} \nUsername/Email: {i[1]} \nPassword: {i[2]}")
    else:
        print("No records found.")

    time.sleep(1)
    return


def add_pass():

    while True:
        web = input("Enter Website Name :").strip()
        user = input("Enter Username / Email : ").strip()
        password = input("Enter Password : ")

        rec,val = specific(web,user)

        if web == rec[0] and user == rec[1]:
            print("\n An Entry Already exists for the same website and username !! ")
            time.sleep(1)

        else:
            query = "INSERT INTO manager VALUES (%s,%s,%s)"
            val = (web,user,password)

            mycursor.execute(query,val)

            print(mycursor.rowcount,"record(s) inserted !!")
            time.sleep(2)
            return
        
def main():

    while True:
        print("\n---- Welcome To PassKeeper ----\n")
        print("Choose What you want to do :  ")
        print("1. Add a new pass \n2. Delete a pass")
        print("3. Display a Specific Record \n4. Display Specific Records with same website or password")
        print("5. Display all Records \n0. Exit")
        
        ch = int(input("Enter Your Choice : "))

        if ch == 1:
            add_pass()
        
        elif ch == 2:
            delete()

        elif ch == 3:
            display_specific()
        
        elif ch == 4:
            display()

        elif ch == 5:
            display_all()
        
        elif ch == 0:
            return
        
        else:
            print("Select from the range [0,5]")

login()