USE cat_modelling_db;

CREATE TABLE risk_assessment (

    assessment_id INT AUTO_INCREMENT PRIMARY KEY,

    property_id INT NOT NULL,

    policy_id INT NOT NULL,

    flood_risk_score DECIMAL(5,2) NOT NULL,

    earthquake_risk_score DECIMAL(5,2) NOT NULL,

    cyclone_risk_score DECIMAL(5,2) NOT NULL,

    wildfire_risk_score DECIMAL(5,2) DEFAULT 0,

    overall_risk_score DECIMAL(5,2) NOT NULL,

    risk_category ENUM(
        'Low',
        'Medium',
        'High',
        'Extreme'
    ) NOT NULL,

    assessment_date DATE NOT NULL,

    assessed_by INT,

    remarks TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_risk_property
        FOREIGN KEY(property_id)
        REFERENCES properties(property_id),

    CONSTRAINT fk_risk_policy
        FOREIGN KEY(policy_id)
        REFERENCES policies(policy_id),

    CONSTRAINT fk_risk_user
        FOREIGN KEY(assessed_by)
        REFERENCES users(user_id)

);