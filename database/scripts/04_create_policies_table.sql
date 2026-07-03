USE cat_modelling_db;

CREATE TABLE policies (

    policy_id INT AUTO_INCREMENT PRIMARY KEY,

    property_id INT NOT NULL,

    policy_number VARCHAR(30) NOT NULL UNIQUE,

    policy_type ENUM(
        'Home',
        'Commercial',
        'Industrial'
    ) NOT NULL,

    coverage_amount DECIMAL(15,2) NOT NULL,

    premium_amount DECIMAL(10,2) NOT NULL,

    start_date DATE NOT NULL,

    end_date DATE NOT NULL,

    policy_status ENUM(
        'Active',
        'Expired',
        'Cancelled'
    ) DEFAULT 'Active',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_policy_property
        FOREIGN KEY(property_id)
        REFERENCES properties(property_id)

);