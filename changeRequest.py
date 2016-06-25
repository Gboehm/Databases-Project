from mysql.connector import cursor
results = None

from deleterequest import deleterequest
from newRequest import newrequest
from updaterequest import updaterequest

def changerequest(cnx, cursor, id):
    while 1:
        temp = input("Changing street or intersection? \n")

        if temp == "street":
            while (1):
                street = input("Please provide the name of the street for the change request: \n")
                stmt = ("SELECT s.streetname "
                        "FROM streets s "
                        "WHERE s.streetname = %s")
                cursor.execute(stmt, (street,))
                if cursor.with_rows:
                    break
                else: "Not a valid street name, try  again"

            stmt = ("SELECT s.streetname, f.description, f.startaddress, f.endaddress, f.featureid, s.streetid "
                        "FROM streets s "
                        "INNER JOIN features f "
                        "ON f.streetid = s.streetid "
                        "WHERE s.streetname = %s")

            cursor.execute(stmt, (street,))
            results = cursor.fetchall()
            if len(results) > 0:
                hasfeats = 1
                for result in results:
                    streetid = result[5]
                    print("feature id: ", result[4])
                    if result[2]:
                        if result[3]:
                            print(result[0], "has a", result[1], "from", result[2], "to", result[3])
                        else:
                            print(result[0], "has a", result[1], "starting at", result[2])
                    else:
                        print(result[0], "has a", result[1])
            else:
                hasfeats = 0
                print("No features on this street, can only add new \n")
            while 1:
                type = input("Would you like to make a new feature, update an existing feature, or delete a feature?\n"
                             "input 'new', 'update', or 'delete\n")
                if type.lower() == 'new':
                    newrequest(cnx,cursor,id,streetid,0)
                    break
                if hasfeats:
                    if type.lower() == 'update':
                        updaterequest(cnx,cursor,id,streetid,0, results)
                        break
                    if type.lower() == 'delete':
                        deleterequest(cnx,cursor,id,streetid,0, results)
                        break
                print("Not a valid input \n")
            type = input("Would you like to continue changing? Yes or No\n")
            if type.lower() == "no":
                return
        if temp == "intersection":
            while 1:
                street1 = input("Please input a cross street name.\n")
                street2 = input("Please input the other cross street name.\n")

                stmt = ("SELECT i.intersectionid "
                        "FROM intersections i "
                        "INNER JOIN streets s "
                        "ON i.street1 = s.streetid "
                        "OR i.street2 = s.streetid "
                        "WHERE s.streetname = %s AND "
                        "i.intersectionid IN "
                        "(SELECT i.intersectionid "
                        " FROM intersections i "
                        " INNER JOIN streets s "
                        " ON i.street1 = s.streetid "
                        " OR i.street2 = s.streetid "
                        " WHERE s.streetname = %s) "
                        )
                cursor.execute(stmt, (street1, street2))
                if cursor.with_rows:
                    interid = cursor.fetchone()[0]
                    break
                else: "Not a valid intersection, try  again"


            stmt = ("SELECT DISTINCT f.description, i.intersectionid, f.featureid "
                    "FROM features f "
                    "INNER JOIN intersections i "
                    "ON f.intersectionid = i.intersectionid "
                    "INNER JOIN streets s "
                    "ON i.street1 = s.streetid "
                    "OR i.street2 = s.streetid "
                    "WHERE s.streetname = %s AND "
                    "i.intersectionid IN "
                    "(SELECT i.intersectionid "
                    " FROM intersections i "
                    " INNER JOIN streets s "
                    " ON i.street1 = s.streetid "
                    " OR i.street2 = s.streetid "
                    " WHERE s.streetname = %s) "
                    )

            cursor.execute(stmt, (street1, street2))
            results = cursor.fetchall()
            if len(results) > 0:
                hasfeats = 1
                print("The intersection of", street1, "and", street2, "has the following: \n")
                for result in results:
                    print(result[0])
            else:
                hasfeats = 0
                print("No features found on the intersection of", street1, "and", street2)
                print("\n Can only make new features for this intersection")
                newrequest(cnx,cursor, id, interid, 1)
                return

            while 1:
                type = input("Would you like to make a new feature, update an existing feature, or delete a feature?\n"
                             "input 'new', 'update', or 'delete\n")
                if type.lower() == 'new':
                    newrequest(cnx,cursor, id, interid, 1)
                    break
                if hasfeats:
                    if type.lower() == 'update':
                        updaterequest(cnx,cursor, id, interid, 1, results)
                        break
                    if type.lower() == 'delete':
                        deleterequest(cnx,cursor, id, interid,1, results)
                        break
                else: print("Not a valid input \n")
            type = input("Would you like to continue changing? Yes or No")
            if type.lower() == "no":
                return