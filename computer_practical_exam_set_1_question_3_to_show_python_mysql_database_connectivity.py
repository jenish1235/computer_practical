import mysql.connector

try:
    connection_with_sql_server = mysql.connector.connect(host = "localhost", user = "root", password = "root")
    print("Connection with mysql server done")

    cursor = connection_with_sql_server.cursor()
    cursor.execute("CREATE DATABASE database1")
    print("Database created")

    #now for connecting to the database

    connection_with_database = mysql.connector.connect( host = "localhost" , user = "root" , password = "root" , database = "database1" )
    print("Connection with database is done")

    
except Exception as e :
    print(e)

