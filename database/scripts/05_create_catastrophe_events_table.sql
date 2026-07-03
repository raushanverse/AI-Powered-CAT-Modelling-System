USE cat_modelling_db;

CREATE TABLE catastrophe_events (

    event_id INT AUTO_INCREMENT PRIMARY KEY,

    event_name VARCHAR(100) NOT NULL,

    disaster_type ENUM(
        'Flood',
        'Earthquake',
        'Cyclone',
        'Wildfire',
        'Landslide'
    ) NOT NULL,

    event_date DATE NOT NULL,

    country VARCHAR(50) NOT NULL,

    state VARCHAR(50) NOT NULL,

    city VARCHAR(50) NOT NULL,

    severity_level ENUM(
        'Low',
        'Medium',
        'High',
        'Extreme'
    ) NOT NULL,

    estimated_loss DECIMAL(15,2),

    affected_population INT,

    latitude DECIMAL(10,6),

    longitude DECIMAL(10,6),

    remarks TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);