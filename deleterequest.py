from mysql.connector import cursor
from changeRequest import results

def deleterequest(cursor, id, placeid, which):
    if which == 0:
        while 1:
            featid = "Please input the feature id from the above list you would like to update:"
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
