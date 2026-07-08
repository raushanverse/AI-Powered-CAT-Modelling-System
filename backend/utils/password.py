import bcrypt


def hash_password(password):
    """
    Convert plain password into hashed password
    """
    password_bytes = password.encode("utf-8")

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password.decode("utf-8")


def verify_password(password, hashed_password):
    """
    Verify plain password with hashed password
    """
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )