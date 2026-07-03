USE cat_modelling_db;

INSERT INTO claims
(
policy_id,
event_id,
claim_number,
claim_date,
claimed_amount,
approved_amount,
claim_status,
surveyor_name,
settlement_date,
remarks
)

VALUES
(
1,
1,
'CLM20260001',
'2026-07-05',
850000.00,
800000.00,
'Approved',
'Rakesh Singh',
'2026-07-15',
'Claim approved after survey.'
);