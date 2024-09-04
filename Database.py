import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='Apc@2007#CS')

if mydb.is_connected():
    print("Connection established")
else:
    print("Connection Failed")

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE password_manager2")

mycursor.execute("USE password_manager2")
mycursor.execute("CREATE TABLE IF NOT EXISTS manager(Website VARCHAR(50), Username VARCHAR(50), Password VARCHAR(50))")

mycursor.execute("""INSERT INTO manager (Website, Username, Password) VALUES 
                 ('Amazon', 'Prime', 'IamPrimeUser'),
                 ('Forest', 'Prime', 'Green@Cover_'),
                 ('River', 'Prime', 'LargeForest'),
                 ('Disney', 'Hotstar', 'IamPremiumUser'),
                 ('Disney', 'Plus', 'Avengers_'),
                 ('Disney', 'PlusStar', '@ssemble__'),
                 ('Crunchy', 'Roll', 'IamPremiumUser')""")

mydb.commit()
