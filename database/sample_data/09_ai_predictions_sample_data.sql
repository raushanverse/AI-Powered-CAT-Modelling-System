USE cat_modelling_db;

INSERT INTO ai_predictions
(
assessment_id,
predicted_loss,
predicted_risk_score,
recommended_premium,
confidence_score,
prediction_model,
prediction_date,
remarks
)

VALUES
(
1,
1250000.00,
72.50,
18000.00,
95.20,
'Random Forest',
'2026-07-04',
'Initial AI prediction generated.'
);