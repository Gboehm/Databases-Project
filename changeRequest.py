from mysql.connector import cursor

def changerequest(cursor, id):
    while 1:
        street = input("Please provide the name of the street for the change request: \n")

        stmt = ("SELECT s.streetname, f.description, f.startaddress, f.endaddress, f.featureid, s.streetid "
                "FROM streets s "
                "INNER JOIN features f "
                "ON f.streetid = s.streetid "
                "WHERE s.streetname = %s")

        cursor.execute(stmt, (street,))
        result = cursor.fetchone()

        if result:
            streetid = result[5]
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

    while 1:
        type = input("Would you like to make a new feature, update an existing feature, or delete a feature?\n",
                     "input 'new', 'update', or 'delete")
        if type.lower() == 'new':
            start = input('If there is a start address, input it. Otherwise press enter')
            end = input('If there is an end address, input it. Otherwise press enter')
            desc = input('Please input the bike feature description:')
            if start.isdigit():
                if end.isdigit():
                    new = ("INSERT INTO changerequest "
                           "(userid, changetype, streetid, startaddress, endaddress, description) "
                           "VALUES (%s, %s, %s, %s, %s, %s)")
                    cursor.execute(new, (id,"new",streetid,start,end, desc))
                else:
                    new = ("INSERT INTO changerequest "
                           "(userid, changetype, streetid, startaddress,description) "
                           "VALUES (%s, %s, %s, %s, %s)")
                    cursor.execute(new, (id, "new", streetid, start, desc))
            else:
                new = ("INSERT INTO changerequest "
                       "(userid, changetype, streetid, startaddress, endaddress, description) "
                       "VALUES (%s, %s, %s, %s)")
                cursor.execute(new, (id, "new", streetid, desc))
            break

        if type.lower() == 'update':
            featid = "Please input the feature id from the above list you would like to update:"
            start = input('If changing/adding start address, input it. Otherwise press enter')
            end = input('If changing/adding end address, input it. Otherwise press enter')
            desc = input('Please input updated bike feature description:')
            if start.isdigit():
                if end.isdigit():
                    new = ("INSERT INTO changerequest "
                           "(userid, featureid, changetype, streetid, startaddress, endaddress, description) "
                           "VALUES (%s, %s, %s, %s, %s, %s, %s)")
                    cursor.execute(new, (id,featid,"update",streetid,start,end, desc))
                else:
                    new = ("INSERT INTO changerequest "
                           "(userid, featureid, changetype, streetid, startaddress,description) "
                           "VALUES (%s, %s, %s, %s, %s, %s)")
                    cursor.execute(new, (id, featid, "update", streetid, start, desc))
            else:
                new = ("INSERT INTO changerequest "
                       "(userid, featureid, changetype, streetid, startaddress, endaddress, description) "
                       "VALUES (%s, %s, %s, %s, %s)")
                cursor.execute(new, (id, featid, "update", streetid, desc))
            break
        if type.lower() == 'delete':
            featid = "Please input the feature id from the above list you would like to delete:"
            delete = ("INSERT INTO changerequest "
                   "(userid, featureid, changetype, streetid) "
                   "VALUES (%s, %s, %s)")
            cursor.execute(delete, (id, featid, "delete", streetid))
            break