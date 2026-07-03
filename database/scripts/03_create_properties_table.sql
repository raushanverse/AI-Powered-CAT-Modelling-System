USE cat_modelling_db;

CREATE TABLE properties (

    property_id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL,

    property_name VARCHAR(100) NOT NULL,

    owner_name VARCHAR(100) NOT NULL,

    address TEXT NOT NULL,

    city VARCHAR(50) NOT NULL,

    state VARCHAR(50) NOT NULL,

    pincode VARCHAR(10) NOT NULL,

    building_type ENUM(
        'Residential',
        'Commercial',
        'Industrial'
    ) NOT NULL,

    construction_material ENUM(
        'Brick',
        'Concrete',
        'Steel',
        'Wood'
    ) NOT NULL,

    construction_year YEAR NOT NULL,

    floors INT NOT NULL,

    occupancy_type ENUM(
        'Owner',
        'Tenant',
        'Vacant'
    ) NOT NULL,

    sum_insured DECIMAL(15,2) NOT NULL,

    premium DECIMAL(10,2) NOT NULL,

    flood_zone ENUM(
        'Low',
        'Medium',
        'High'
    ) DEFAULT 'Low',

    earthquake_zone ENUM(
        'Low',
        'Medium',
        'High'
    ) DEFAULT 'Low',

    cyclone_zone ENUM(
        'Low',
        'Medium',
        'High'
    ) DEFAULT 'Low',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_property_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)

);