from database.db import get_db_connection


def get_all_users():
    connection = get_db_connection()

    if connection is None:
        return None

    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT
            user_id,
            full_name,
            employee_id,
            email,
            phone,
            role,
            office_location,
            status,
            created_at,
            updated_at,
            last_login
        FROM users;"""

    cursor.execute(query)

    users = cursor.fetchall()

    cursor.close()
    connection.close()

    return users