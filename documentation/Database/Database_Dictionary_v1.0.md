# Database Dictionary

## Project Name

AI-Powered CAT Modelling & Risk Assessment Platform

---

# Database Information

| Item | Details |
|------|----------|
| Database Name | cat_modelling_db |
| Database Type | MySQL |
| Version | 1.0 |
| Total Tables | 10 |
| Storage Engine | InnoDB |
| Character Set | UTF8MB4 |

---

# Table Summary

| Table Name | Purpose |
|------------|----------|
| users | Store system users |
| properties | Store insured property details |
| policies | Store insurance policy information |
| catastrophe_events | Store natural disaster events |
| risk_assessment | Store calculated risk scores |
| ml_predictions | Store machine learning prediction results |
| claims | Store insurance claim information |
| reinsurance | Store reinsurance recommendations |
| reports | Store generated report details |
| audit_logs | Store system activity logs |



---

# Table Details

## Table Name

users

### Purpose

Stores user account information for authentication and authorization.

### Primary Key

user_id

### Important Columns

| Column | Description |
|---------|-------------|
| user_id | Unique User ID |
| full_name | User Full Name |
| email | Email Address |
| password | Encrypted Password |
| role | User Role |
| phone | Contact Number |
| status | Active / Inactive |
| created_at | Account Creation Date |
| updated_at | Last Updated Date |




---

# Table Details

## Table Name

properties

### Purpose

Stores insured property information used for catastrophe risk assessment and financial loss prediction.

### Primary Key

property_id

### Important Columns

| Column | Description |
|---------|-------------|
| property_id | Unique Property ID |
| owner_name | Property Owner Name |
| property_name | Property Name |
| address | Property Address |
| city | City |
| state | State |
| pincode | Postal Code |
| building_type | Residential / Commercial / Industrial |
| construction_material | Brick / Concrete / Steel / Wood |
| construction_year | Year of Construction |
| floors | Number of Floors |
| occupancy_type | Owner Occupied / Tenant / Vacant |
| sum_insured | Total Insured Amount |
| premium | Insurance Premium |
| flood_zone | Flood Risk Zone |
| earthquake_zone | Earthquake Risk Zone |
| cyclone_zone | Cyclone Risk Zone |
| created_at | Record Creation Date |
| updated_at | Record Update Date |