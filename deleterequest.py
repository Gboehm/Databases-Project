from mysql.connector import cursor

def deleterequest(cursor, id, placeid, which, results):
    if which == 0:
        while 1:
            featid = input("Please input the feature id from the above list you would like to update:\n")
            isafeat = 0
            for result in results:
                if result[4] == featid:
                    isafeat = 1
            if isafeat:
                break
            else:
                print("Not a valid feature id from the results. Try again")
        delete = ("INSERT INTO change_requests "
                  "(userid, featureid, changetype, streetid) "
                  "VALUES (%s, %s, %s, %s)")
        cursor.execute(delete, (id, featid, "delete", placeid))
        print("Change request submitted")
    elif which == 1:
        while 1:
            featid = "Please input the feature id from the above list you would like to update:"
            isafeat = 0
            for result in results:
                if result[2] == featid:
                    isafeat = 1
            if isafeat:
                break
            else:
                print("Not a valid feature id from the results. Try again")
        delete = ("INSERT INTO change_requests "
                  "(userid, featureid, changetype, intersectionid) "
                  "VALUES (%s, %s, %s, %s)")
        cursor.execute(delete, (id, featid, "delete", placeid))
        print("Change request submitted")
