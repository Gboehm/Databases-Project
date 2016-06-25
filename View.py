from mysql.connector import cursor


def View(cursor):
    while 1:
        type = input("View a Street or an Intersection?\n")

        if type.lower() == 'street':
            operation = input("View Incidents or Features?\n")

            if operation.lower() == "features":
                while 1:
                    street = input("Please input a street name.\n")

                    stmt = ("SELECT s.streetname, f.description, f.startaddress, f.endaddress "
                            "FROM streets s "
                            "INNER JOIN features f "
                            "ON f.streetid = s.streetid "
                            "WHERE s.streetname = %s")

                    cursor.execute(stmt, (street,))
                    result = cursor.fetchone()

                    if result:
                        if result[2]:
                            if result[3]:
                                print(result[0], "has a", result[1], "from", result[2], "to", result[3])
                            else:
                                print(result[0], "has a", result[1], "starting at", result[2])
                        else:
                            print(result[0], "has a", result[1])
                        break
                    else:
                        print("No features found on", street)

                        while 1:
                            op = input("Search again? Yes or No")

                            if op.lower() == 'yes' or op.lower() == 'no':
                                break
                    if op and op.lower() == 'no':
                        break

                for result in cursor:
                    if result[2]:
                        if result[3]:
                            print(result[0], "has a", result[1], "from", result[2], "to", result[3])
                        else:
                            print(result[0], "has a", result[1], "starting at", result[2])
                    else:
                        print(result[0], "has a", result[1])

            elif operation.lower() == "incidents":
                while 1:
                    street = input("Please input a street name.\n")

                    stmt = ("SELECT s.streetname, i.address, i.severity, i.description "
                            "FROM streets s "
                            "INNER JOIN incidents i "
                            "ON i.streetid = s.streetid "
                            "WHERE s.streetname = %s")

                    cursor.execute(stmt, (street,))
                    result = cursor.fetchone()

                    if result:
                        print("Street:", result[0])

                        if result[1]:
                            print("Address:", result[1])
                        if result[2]:
                            print("Severity:", result[2])
                        if result[3]:
                            print("Description:", result[3], '\n')
                        break
                    else:
                        print("No incidents found on", street)
            else:
                print("Invalid input")

                for result in cursor:
                    print("Street:", result[0])

                    if result[1]:
                        print("Address:", result[1])
                    if result[2]:
                        print("Severity:", result[2])
                    if result[3]:
                        print("Description:", result[3], '\n')

                temp = input("View again? Yes or No?\n")

                if temp.lower() == 'no':
                    break



        elif type.lower() == 'intersection':
            operation = input("View Incidents or Features?\n")

            if operation.lower() == 'features':

                while 1:
                    street1 = input("Please input a cross street name.\n")
                    street2 = input("Please input the other cross street name.\n")

                    stmt = ("SELECT DISTINCT f.description "
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
                    result = cursor.fetchone()

                    if result:
                        print("The intersection of", street1, "and", street2, "has the following:")
                        print(result[0])
                        break
                    else:
                        print("No features found on the intersection of", street1, "and", street2)

                        while 1:
                            op = input("Search again? Yes or No\n")

                            if op.lower() == 'no' or op.lower() == 'yes':
                                break
                    if op and op.lower() == 'no':
                        break

                for result in cursor:
                    print(result[0])
            elif operation.lower() == 'incidents':
                while 1:
                    street1 = input("Please input a cross street name.\n")
                    street2 = input("Please input the other cross street name.\n")

                    stmt = ("SELECT DISTINCT inc.address, inc.severity, inc.description "
                            "FROM incidents inc "
                            "INNER JOIN intersections i "
                            "ON inc.intersectionid = i.intersectionid "
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
                    result = cursor.fetchone()

                    if result:
                        if result[0]:
                            print("Address:", result[0])
                        if result[1]:
                            print("Severity:", result[1])
                        if result[2]:
                            print("Description:", result[2], '\n')
                        break
                    else:
                        print("No incidents found on the intersection of", street1, "and", street2)

                        while 1:
                            op = input("Search again? Yes or No\n")

                            if op.lower() == 'no' or op.lower() == 'yes':
                                break
                    if op and op.lower() == 'no':
                        break

                for result in cursor:
                    if result[0]:
                        print("Address:", result[0])
                    if result[1]:
                        print("Severity:", result[1])
                    if result[2]:
                        print("Description:", result[2], '\n')
            else:
                print('Invalid input')

        while 1:
            op = input("View again? Yes or No?\n")

            if op.lower() == 'yes' or op.lower() == 'no':
                break
        if op.lower() == 'no':
            break
