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
    FROM users
    """

    cursor.execute(query)

    users = cursor.fetchall()

    cursor.close()
    connection.close()

    return users


def create_user(data):
    connection = get_db_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    query = """
    INSERT INTO users
    (
        full_name,
        employee_id,
        email,
        phone,
        password,
        role,
        office_location,
        status
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        data["full_name"],
        data["employee_id"],
        data["email"],
        data["phone"],
        data["password"],
        data["role"],
        data["office_location"],
        "Active"
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return True


def get_user_by_id(user_id):
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
    FROM users
    WHERE user_id = %s
    """

    cursor.execute(query, (user_id,))

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user