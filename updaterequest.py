from mysql.connector import cursor
from changeRequest import results

def updaterequest(cursor, id, placeid, which):

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
        start = input('If changing/adding start address, input it. Otherwise press enter\n')
        end = input('If changing/adding end address, input it. Otherwise press enter\n')
        desc = input('Please input updated bike feature description:\n')
        if start.isdigit():
            if end.isdigit():
                new = ("INSERT INTO change_requests "
                       "(userid, featureid, changetype, streetid, startaddress, endaddress, description) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s)")
                cursor.execute(new, (id, featid, "update", placeid, start, end, desc))
            else:
                new = ("INSERT INTO change_requests "
                       "(userid, featureid, changetype, streetid, startaddress,description) "
                       "VALUES (%s, %s, %s, %s, %s, %s)")
                cursor.execute(new, (id, featid, "update", placeid, start, desc))
        else:
            new = ("INSERT INTO change_requests "
                   "(userid, featureid, changetype, streetid, startaddress, endaddress, description) "
                   "VALUES (%s, %s, %s, %s, %s)")
            cursor.execute(new, (id, featid, "update", placeid, desc))
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
        desc = input('Please input updated bike feature description:')
        new = ("INSERT INTO change_requests "
               "(userid, featureid, changetype,intersectionid, description) "
               "VALUES (%s, %s, %s, %s, %s)")
        cursor.execute(new, (id, featid, "update", placeid, desc))