# Data Dictionary

## users

**Purpose:**
Stores customer and employee information such as personal details, contact information, login credentials, and user roles.

**Primary Key:**
- user_id

---

## properties

**Purpose:**
Stores details of insured properties including location, construction details, property type, and insurance-related information.

**Primary Key:**
- property_id

**Foreign Key:**
- user_id → users(user_id)

---

## policies

**Purpose:**
Stores insurance policy information associated with insured properties including policy number, coverage amount, premium, and policy validity.

**Primary Key:**
- policy_id

**Foreign Key:**
- property_id → properties(property_id)

---

## catastrophe_events

**Purpose:**
Stores historical catastrophe events such as floods, earthquakes, cyclones, wildfires, and landslides along with their severity and estimated losses.

**Primary Key:**
- event_id

---

## risk_assessment

**Purpose:**
Stores catastrophe risk scores calculated for insured properties. These scores are later used by the AI model to predict expected losses and recommend insurance premiums.

**Primary Key:**
- assessment_id

**Foreign Keys:**
- property_id → properties(property_id)
- policy_id → policies(policy_id)
- assessed_by → users(user_id)

---

## claims

**Purpose:**
Stores insurance claim details submitted after catastrophe events including claimed amount, approved amount, claim status, survey information, and settlement details.

**Primary Key:**
- claim_id

**Foreign Keys:**
- policy_id → policies(policy_id)
- event_id → catastrophe_events(event_id)

---

## reinsurance

**Purpose:**
Stores reinsurance information used to transfer a portion of insurance risk to another insurance company (reinsurer).

**Primary Key:**
- reinsurance_id

**Foreign Keys:**
- policy_id → policies(policy_id)
- claim_id → claims(claim_id)

---

## ai_predictions

**Purpose:**
Stores AI-generated predictions such as expected financial loss, predicted risk score, recommended premium, confidence score, and prediction model details.

**Primary Key:**
- prediction_id

**Foreign Key:**
- assessment_id → risk_assessment(assessment_id)

---

## audit_logs

**Purpose:**
Stores system activity logs including user actions such as login, record creation, updates, deletions, and AI prediction events for auditing and security purposes.

**Primary Key:**
- log_id

**Foreign Key:**
- user_id → users(user_id)

---