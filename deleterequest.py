from mysql.connector import cursor


def deleterequest(cursor, id, placeid, which):
    if which == 0:
        featid = "Please input the feature id from the above list you would like to delete:"
        delete = ("INSERT INTO changerequest "
                  "(userid, featureid, changetype, streetid) "
                  "VALUES (%s, %s, %s)")
        cursor.execute(delete, (id, featid, "delete", placeid))
    elif which == 1:
        featid = "Please input the feature id from the above list you would like to delete:"
        delete = ("INSERT INTO changerequest "
                  "(userid, featureid, changetype, streetid) "
                  "VALUES (%s, %s, %s)")
        cursor.execute(delete, (id, featid, "delete", streetid))
