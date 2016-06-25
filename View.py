from mysql.connector import cursor

def View(cursor):
    while 1:
        type = input("View a Street or an Intersection?\n")

        if type.lower() == 'street':
            operation = input("View incidents or features?\n")

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

                for result in cursor:
                    if result[2]:
                        if result[3]:
                            print(result[0], "has a", result[1], "from", result[2], "to", result[3])
                        else:
                            print(result[0], "has a", result[1], "starting at", result[2])
                    else:
                        print(result[0], "has a", result[1])

                temp = input("View again? Yes or No?\n")

                if temp.lower() == 'no':
                    break
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
            street1 = input("Please input a cross street name.\n")
            street2 = input("Please input the other cross street name.\n")

            stmt = ("SELECT f.description, ")
            break
