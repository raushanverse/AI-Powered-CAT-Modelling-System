USE cat_modelling_db;

INSERT INTO catastrophe_events
(
event_name,
disaster_type,
event_date,
country,
state,
city,
severity_level,
estimated_loss,
affected_population,
latitude,
longitude,
remarks
)

VALUES
(
'Patna Flood 2025',
'Flood',
'2025-08-15',
'India',
'Bihar',
'Patna',
'High',
85000000.50,
250000,
25.5941,
85.1376,
'Heavy rainfall caused severe flooding.'
);