from database.db import get_db_connection

connection = get_db_connection()

if connection:
    print("Database Test Passed ✅")
    connection.close()
else:
    print("Database Test Failed ❌")