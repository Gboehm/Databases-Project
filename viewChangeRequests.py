from executeRequest import executeRequest


def viewChangeRequests(cnx, cursor, adminID):
    while 1:
        stmt = ("SELECT COUNT(*)"
                "FROM change_requests "
                "WHERE approved IS NULL")
        cursor.execute(stmt)
        result = cursor.fetchone()

        print("There are", result[0], "pending change requests.")

        while 1:
            op = input("View change request by id or view new requests? Input 'id' or 'new'\n")

            if op.lower() == 'id' or op.lower() == 'new':
                break
            else:
                print("Invalid input")

        if op.lower() == 'id':
            while 1:
                id = input("Input an id to see change_requests\n")

                stmt = ("SELECT u.username, c.* "
                        "FROM users u "
                        "INNER JOIN change_requests c "
                        "ON u.userid = c.userid "
                        "WHERE c.requestid = %s")

                cursor.execute(stmt, (id,))
                results = cursor.fetchone()

                if results:
                    break
                else:
                    print("No requests found with the given id.")

                    while 1:
                        op = input("Search again? Yes or No\n")

                        if op.lower() == 'yes' or op.lower() == 'no':
                            break

                    if op.lower() == 'no':
                        break
                    else:
                        continue
            if results:
                if results[5]:
                    stmt = ("SELECT s.streetname "
                            "from streets s "
                            "WHERE streetid = %s")
                    cursor.execute(stmt, (results[5],))
                    name = cursor.fetchone()[0]

                elif results[6]:
                    stmt = ("SELECT DISTINCT s.streetname "
                            "FROM streets s "
                            "INNER JOIN intersections i "
                            "ON s.streetid = i.street1 "
                            "OR s.streetid = i.street2 "
                            "WHERE i.intersectionid = %s")

                    cursor.execute(stmt, (results[6],))
                    name = "the intersection of " + cursor.fetchone()[0] + " and " + cursor.fetchone()[0]

                print("User", result[0], "wants to", result[4], "the following information on", name)

                if result[7]:
                    print("Start address:", result[7])
                if result[8]:
                    print("End address:", result[8])
                if result[9]:
                    print("Description:", result[9])
                if result[10]:
                    stmt = ("SELECT u.username "
                            "FROM u.users "
                            "WHERE u.userid = %s"
                            )
                    cursor.execute(stmt, (result[10],))
                    print("This request was approved by:", cursor.fetchone()[0])
                else:
                    while 1:
                        op = input("Approve this request? Yes or No\n")

                        if op.lower() == 'yes' or op.lower() == 'no':
                            break
                    if op.lower() == 'yes':
                        request = results[1:10]
                        executeRequest(cnx, cursor, request, adminID)
        elif op.lower() == 'new':
            while 1:
                stmt = ("SELECT u.username, c.* "
                        "FROM users u "
                        "INNER JOIN change_requests c "
                        "ON u.userid = c.userid "
                        "WHERE c.approved IS NULL "
                        "LIMIT 1")

                cursor.execute(stmt)
                results = cursor.fetchone()

                if not results:
                    print("No unapproved requests found.")
                    break

                if results[5]:
                    stmt = ("SELECT s.streetname "
                            "from streets s "
                            "WHERE streetid = %s")
                    cursor.execute(stmt, (results[5],))
                    name = cursor.fetchone()[0]

                elif results[6]:
                    stmt = ("SELECT DISTINCT s.streetname "
                            "FROM streets s "
                            "INNER JOIN intersections i "
                            "ON s.streetid = i.street1 "
                            "OR s.streetid = i.street2 "
                            "WHERE i.intersectionid = %s")

                    cursor.execute(stmt, (results[6],))
                    name = "the intersection of " + cursor.fetchone()[0] + " and " + cursor.fetchone()[0]

                if results[4] == 'new':
                    task = 'insert'
                else:
                    task = results[4]
                print("User", results[0], "wants to", task, "the following information on", name)

                if results[7]:
                    print("Start address:", results[7])
                if results[8]:
                    print("End address:", results[8])
                if results[9]:
                    print("Description:", results[9])

                while 1:
                    op = input("Approve this request? Yes or No\n")

                    if op.lower() == 'yes' or op.lower() == 'no':
                        break
                if op.lower() == 'yes':
                    request = results[1:10]
                    executeRequest(cnx, cursor, request, adminID)
                while 1:
                    op = input("View another request? Yes or No\n")

                    if op.lower() == 'yes' or op.lower() == 'no':
                        break
                if op.lower() == 'no':
                    break
        while 1:
            op = input("View more requests? Yes or No\n")

            if op.lower() == 'yes' or op.lower() == 'no':
                break
        if op.lower() == 'no':
            break

