USE cat_modelling_db;

INSERT INTO audit_logs
(
user_id,
module_name,
action_type,
record_id,
ip_address,
remarks
)

VALUES
(
1,
'Policies',
'INSERT',
1,
'127.0.0.1',
'Policy created successfully.'
);