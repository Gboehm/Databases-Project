import mysql.connector
from mysql.connector import errorcode

from View import View

try:
    cnx = mysql.connector.connect(user="root", password="root", host='127.0.0.1', database='projectdb')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = cnx.cursor()

    while 1:
        username = input("Please input your username.\n")
        password = input("Please input your password.\n")

        cursor.execute("SELECT userid FROM users WHERE username=%s AND password=%s", (username, password))

        result = cursor.fetchone()

        if result:
            id = result[0]
            break
        else:
            print("Not Found")
            continue

    print("Commands:")

    commands = ["View",
                "Insert",
                ]

    while 1:
        for command in commands:
            print(command)

        operation = input("Please input a command\n")

        if operation.lower() == 'view':

            View(cursor)


        elif operation.lower() == 'insert':
            break

        temp = input("Perform another operation?\n")

        if temp.lower() == "no":
            break
