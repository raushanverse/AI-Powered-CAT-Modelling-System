USE cat_modelling_db;

CREATE TABLE audit_logs (

    log_id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL,

    module_name VARCHAR(50) NOT NULL,

    action_type ENUM(
        'INSERT',
        'UPDATE',
        'DELETE',
        'LOGIN',
        'LOGOUT',
        'PREDICTION'
    ) NOT NULL,

    record_id INT,

    action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    ip_address VARCHAR(45),

    remarks TEXT,

    CONSTRAINT fk_audit_user
        FOREIGN KEY(user_id)
        REFERENCES users(user_id)

);