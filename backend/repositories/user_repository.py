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

    try:
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

        return True

    except Exception as e:
        print(f"❌ Repository Error: {e}")

        connection.rollback()

        return False

    finally:
        cursor.close()
        connection.close()


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


def get_user_by_email(email):
    connection = get_db_connection()

    if connection is None:
        return None

    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE email = %s"

    cursor.execute(query, (email,))

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user


def get_user_by_employee_id(employee_id):
    connection = get_db_connection()

    if connection is None:
        return None

    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE employee_id = %s"

    cursor.execute(query, (employee_id,))

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user