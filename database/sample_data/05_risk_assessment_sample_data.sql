USE cat_modelling_db;

INSERT INTO risk_assessment
(
property_id,
policy_id,
flood_risk_score,
earthquake_risk_score,
cyclone_risk_score,
wildfire_risk_score,
overall_risk_score,
risk_category,
assessment_date,
assessed_by,
remarks
)

VALUES
(
1,
1,
80.50,
35.20,
15.80,
5.00,
59.13,
'Medium',
'2026-07-03',
1,
'Initial CAT Risk Assessment'
);