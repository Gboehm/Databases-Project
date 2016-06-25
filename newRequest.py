from mysql.connector import cursor

def newrequest(cursor, id, placeid, which):
    if which == 0:
        start = input('If there is a start address, input it. Otherwise press enter\n')
        end = input('If there is an end address, input it. Otherwise press enter\n')
        desc = input('Please input the bike feature description:\n')
        if start.isdigit():
            if end.isdigit():
                new = ("INSERT INTO change_requests "
                       "(userid, changetype, streetid, startaddress, endaddress, description) "
                       "VALUES (%s, %s, %s, %s, %s, %s)")
                cursor.execute(new, (id, "new", placeid, start, end, desc))
            else:
                new = ("INSERT INTO change_requests "
                       "(userid, changetype, streetid, startaddress,description) "
                       "VALUES (%s, %s, %s, %s, %s)")
                cursor.execute(new, (id, "new", placeid, start, desc))
        else:
            new = ("INSERT INTO change_requests "
                   "(userid, changetype, streetid, description) "
                   "VALUES (%s, %s, %s, %s)")
            cursor.execute(new, (id, "new", placeid, desc))
        print(id, ", new, ", placeid, ", ", desc)
        print("Change request submitted")

    elif which == 1:
        desc = input('Please input the bike feature description:')
        new = ("INSERT INTO change_requests "
               "(userid, changetype, intersectionid, description) "
               "VALUES (%s, %s, %s, %s)")
        cursor.execute(new, (id, "new", placeid, desc))
        print("Change request submitted")

