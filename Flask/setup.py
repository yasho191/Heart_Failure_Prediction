import pymysql
db=pymysql.connect(host="database-1.crewf9jbpd79.ap-south-1.rds.amazonaws.com",
        user='yash',
        password='7083581881',
        database="mydb"
        )

cursor=db.cursor()

#cursor.execute('CREATE DATABASE mydb')
cursor.execute("SHOW DATABASES")

for i in cursor:
    print(i)
cursor.execute("CREATE TABLE customers (email VARCHAR(255), password VARCHAR(255))")


