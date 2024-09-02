import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user='root', password = 'Apc@2007#CS')

if mydb.is_connected():
    print("Connection established")
else:
    print("Connection Failed")

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE password_manager2")

mycursor.execute("USE password_manager2")
mycursor.execute("CREATE TABLE manager(Website VARCHAR(50), Username VARCHAR(50), Password VARCHAR(50))")

mycursor.execute("""INSERT INTO manager VALUES 
                 (Amazon,Prime,IamPrimeUser),
                 (Disney,Hotstar,IamPremiumUser),
                 (Crunchy,Roll,IamPremiumUser)""")