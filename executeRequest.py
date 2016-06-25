def executeRequest(cursor, request, adminID):
    if request[3].lower() == 'delete':
        stmt = ("DELETE FROM features f "
                "WHERE EXISTS "
                "(SELECT * "
                " FROM features f "
                " INNER JOIN change_requests c "
                " ON f.featureid = c.featureid "
                " WHERE f.featureid = %s) "
                )
        cursor.execute(stmt, (request[2],))

        stmt = ("UPDATE change_requests "
                "SET approved = %s "
                "WHERE requestid = %s")
        cursor.execute(stmt, (adminID, request[0]))

    elif request[3].lower() == 'new':
        if request[4]:
            if request[6]:
                if request[7]:
                    stmt = ("INSERT INTO features "
                            "(streetid, startaddress, endaddress, description) "
                            "VALUES (%s, %s, %s, %s)"
                            )
                    cursor.execute(stmt, (request[4], request[6], request[7], request[8]))
                else:
                    stmt = ("INSERT INTO features "
                            "(streetid, startaddress, description) "
                            "VALUES (%s, %s, %s)"
                            )
                    cursor.execute(stmt, (request[4], request[6], request[8]))
            else:
                stmt = ("INSERT INTO features "
                        "(streetid, description) "
                        "VALUES (%s, %s)"
                        )
                cursor.execute(stmt, (request[4], request[8]))
        else:
            stmt = ("INSERT INTO features "
                    "(intersectionid, description) "
                    "VALUES (%s, %s)"
                    )
            cursor.execute(stmt, (request[5], request[8]))

        stmt = ("UPDATE change_requests "
                "SET approved = %s "
                "WHERE requestid = %s")
        cursor.execute(stmt, (adminID, request[0]))

    elif request[3].lower() == 'update':
        if request[6]:
            stmt = ("UPDATE features "
                    "SET startaddress = %s "
                    "WHERE featureid = %s")

            cursor.execute(stmt, (request[6], request[2]))
        if request[7]:
            stmt = ("UPDATE features "
                    "SET endaddress = %s "
                    "WHERE featureid = %s")

            cursor.execute(stmt, (request[7], request[2]))
        if request[8]:
            stmt = ("UPDATE features "
                    "SET description = %s "
                    "WHERE featureid = %s")

            cursor.execute(stmt, (request[8], request[2]))

        stmt = ("UPDATE change_requests "
                "SET approved = %s "
                "WHERE requestid = %s")
        cursor.execute(stmt, (adminID, request[0]))
