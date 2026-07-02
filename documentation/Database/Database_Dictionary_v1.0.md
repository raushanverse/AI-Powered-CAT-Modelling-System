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