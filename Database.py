import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='baba')

if mydb.is_connected():
    print("Connection established !!! ")
else:
    print("Connection Failed")

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE password_manager")

mycursor.execute("USE password_manager")
mycursor.execute("CREATE TABLE manager(Website VARCHAR(50), Username VARCHAR(50), Password VARCHAR(50))")

mycursor.execute("""INSERT INTO manager (Website, Username, Password) VALUES
                 ('Website', 'Username', 'Password')
                 ('Amazon', 'Prime', 'IamPrimeUser'),
                 ('Forest', 'Prime', 'Green@Cover_'),
                 ('River', 'Prime', 'LargeForest'),
                 ('Disney', 'Hotstar', 'IamPremiumUser'),
                 ('Disney', 'Plus', 'Avengers_'),
                 ('Disney', 'PlusStar', '@ssemble__'),
                 ('Crunchy', 'Roll', 'IamPremiumUser')""")

mydb.commit()
