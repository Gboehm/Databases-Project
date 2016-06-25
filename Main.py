import mysql.connector
from mysql.connector import errorcode

from view import view

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

    cursor.execute("SELECT userid FROM administrators WHERE userid = %s", (id,))
    admin = cursor.fetchone()


    print("Commands:")

    commands = ["View",
                "Change",
                ]

    while 1:
        for command in commands:
            print(command)

        operation = input("Please input a command\n")

        if operation.lower() == 'view':
            if admin:
                while 1:
                    op = input("Type yes to view change requests, or no to view streets and intersections\n")

                    if op.lower() == 'yes' or op.lower() == 'no':
                        break
                #if op.lower() == 'yes':
                    #View change requests function here


            view(cursor)


        elif operation.lower() == 'change':
            changerequest(cursor, id)

        temp = input("Perform another operation?\n")

        if temp.lower() == "no":
            cnx.close()
            sys.exit()
