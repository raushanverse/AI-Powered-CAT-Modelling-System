USE cat_modelling_db;

CREATE TABLE users (

    user_id INT AUTO_INCREMENT PRIMARY KEY,

    employee_id VARCHAR(20) UNIQUE,

    full_name VARCHAR(100) NOT NULL,

    email VARCHAR(100) NOT NULL UNIQUE,

    password VARCHAR(255) NOT NULL,

    role ENUM(
        'Admin',
        'CAT Analyst',
        'Underwriter',
        'Claims Officer'
    ) NOT NULL,

    phone VARCHAR(15),

    office_location VARCHAR(100),

    status ENUM(
        'Active',
        'Inactive'
    ) DEFAULT 'Active',

    last_login TIMESTAMP NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP

);