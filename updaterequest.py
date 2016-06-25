from mysql.connector import cursor


def changerequest(cursor, id, placeid, which):
    if which == 0:
        featid = "Please input the feature id from the above list you would like to update:"
        start = input('If changing/adding start address, input it. Otherwise press enter')
        end = input('If changing/adding end address, input it. Otherwise press enter')
        desc = input('Please input updated bike feature description:')
        if start.isdigit():
            if end.isdigit():
                new = ("INSERT INTO changerequest "
                       "(userid, featureid, changetype, streetid, startaddress, endaddress, description) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s)")
                cursor.execute(new, (id, featid, "update", streetid, start, end, desc))
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
    elif which == 1:
        featid = "Please input the feature id from the above list you would like to update:"
        desc = input('Please input updated bike feature description:')
        new = ("INSERT INTO changerequest "
               "(userid, featureid, changetype,intersectionid, description) "
               "VALUES (%s, %s, %s, %s, %s)")
        cursor.execute(new, (id, featid, "update", streetid, desc))