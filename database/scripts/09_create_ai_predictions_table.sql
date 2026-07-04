USE cat_modelling_db;

CREATE TABLE ai_predictions (

    prediction_id INT AUTO_INCREMENT PRIMARY KEY,

    assessment_id INT NOT NULL,

    predicted_loss DECIMAL(15,2) NOT NULL,

    predicted_risk_score DECIMAL(5,2) NOT NULL,

    recommended_premium DECIMAL(10,2) NOT NULL,

    confidence_score DECIMAL(5,2) NOT NULL,

    prediction_model VARCHAR(100) NOT NULL,

    prediction_date DATE NOT NULL,

    remarks TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_prediction_assessment
        FOREIGN KEY (assessment_id)
        REFERENCES risk_assessment(assessment_id)

);