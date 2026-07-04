USE cat_modelling_db;

INSERT INTO reinsurance
(
policy_id,
claim_id,
reinsurer_company,
reinsurance_type,
ceded_amount,
recovered_amount,
recovery_status,
recovery_date,
remarks
)

VALUES
(
1,
1,
'Munich Re',
'Excess of Loss',
500000.00,
500000.00,
'Recovered',
'2026-08-01',
'Reinsurance recovery completed.'
);