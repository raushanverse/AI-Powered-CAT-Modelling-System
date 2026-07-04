USE cat_modelling_db;

INSERT INTO properties
(
user_id,
property_name,
owner_name,
address,
city,
state,
pincode,
building_type,
construction_material,
construction_year,
floors,
occupancy_type,
sum_insured,
premium,
flood_zone,
earthquake_zone,
cyclone_zone
)

VALUES
(
1,
'Raushan Residency',
'Raushan Kumar',
'Ward No. 12, Saharsa',
'Saharsa',
'Bihar',
'852201',
'Residential',
'Concrete',
2020,
2,
'Owner',
5000000.00,
15000.00,
'Medium',
'Low',
'Low'
);