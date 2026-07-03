USE cat_modelling_db;

CREATE TABLE claims (

    claim_id INT AUTO_INCREMENT PRIMARY KEY,

    policy_id INT NOT NULL,

    event_id INT NOT NULL,

    claim_number VARCHAR(30) NOT NULL UNIQUE,

    claim_date DATE NOT NULL,

    claimed_amount DECIMAL(15,2) NOT NULL,

    approved_amount DECIMAL(15,2) DEFAULT 0.00,

    claim_status ENUM(
        'Submitted',
        'Under Review',
        'Approved',
        'Rejected',
        'Paid'
    ) DEFAULT 'Submitted',

    surveyor_name VARCHAR(100),

    settlement_date DATE,

    remarks TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_claim_policy
        FOREIGN KEY (policy_id)
        REFERENCES policies(policy_id),

    CONSTRAINT fk_claim_event
        FOREIGN KEY (event_id)
        REFERENCES catastrophe_events(event_id)

);