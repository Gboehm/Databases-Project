from mysql.connector import cursor

def changeRequest(cursor):
    while 1:
        street = input("Please provide the name of the street for the change request: \n")

        stmt = ("SELECT s.streetname, f.description, f.startaddress, f.endaddress, f.featureid "
                "FROM streets s "
                "INNER JOIN features f "
                "ON f.streetid = s.streetid "
                "WHERE s.streetname = %s")

        cursor.execute(stmt, (street,))
        result = cursor.fetchone()

        if result:
            print("feature id: ", result[4])
            if result[2]:
                if result[3]:
                    print(result[0], "has a", result[1], "from", result[2], "to", result[3])
                else:
                    print(result[0], "has a", result[1], "starting at", result[2])
            else:
                print(result[0], "has a", result[1])
            break

    for result in cursor:
        print("feature id: ", result[4])
        if result[2]:
            if result[3]:
                print(result[0], "has a", result[1], "from", result[2], "to", result[3])
            else:
                print(result[0], "has a", result[1], "starting at", result[2])
        else:
            print(result[0], "has a", result[1])

    While 1:
        type = input("Would you like to make a new feature, update an existing feature, or delete a feature?\n",
                     "input 'new', 'update', or 'delete")
        if type.lower() == 'new':

        if type.lower() == 'update':

        if type.lower() == 'delete':
