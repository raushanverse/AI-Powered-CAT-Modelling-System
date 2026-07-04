USE cat_modelling_db;

CREATE TABLE reinsurance (

    reinsurance_id INT AUTO_INCREMENT PRIMARY KEY,

    policy_id INT NOT NULL,

    claim_id INT NOT NULL,

    reinsurer_company VARCHAR(100) NOT NULL,

    reinsurance_type ENUM(
        'Facultative',
        'Quota Share',
        'Surplus',
        'Excess of Loss'
    ) NOT NULL,

    ceded_amount DECIMAL(15,2) NOT NULL,

    recovered_amount DECIMAL(15,2) DEFAULT 0.00,

    recovery_status ENUM(
        'Pending',
        'Recovered',
        'Rejected'
    ) DEFAULT 'Pending',

    recovery_date DATE,

    remarks TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_reinsurance_policy
        FOREIGN KEY (policy_id)
        REFERENCES policies(policy_id),

    CONSTRAINT fk_reinsurance_claim
        FOREIGN KEY (claim_id)
        REFERENCES claims(claim_id)

);