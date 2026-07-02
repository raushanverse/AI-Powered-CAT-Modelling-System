# System Architecture

## Project Name

AI-Powered CAT Modelling & Risk Assessment Platform

---

# Architecture Overview

The system follows a three-tier architecture consisting of Presentation Layer, Application Layer, and Data Layer.

The platform enables insurance organizations to manage insured properties, perform catastrophe risk assessment, predict financial losses using Machine Learning, and generate business reports.

---

# Architecture Layers

## 1. Presentation Layer

Technology:

- HTML
- CSS
- Bootstrap
- JavaScript

Responsibilities:

- User Login
- Dashboard
- Property Forms
- CAT Event Screens
- Reports

---

## 2. Application Layer

Technology:

- Python
- Flask

Responsibilities:

- Business Logic
- Authentication
- Risk Calculation
- API Services
- Machine Learning Integration
- Report Generation

---

## 3. Data Layer

Technology:

- MySQL

Responsibilities:

- Store Users
- Store Properties
- Store CAT Events
- Store Claims
- Store Risk Scores
- Store Reports

---

# Machine Learning Layer

Technology:

- Python
- Scikit-Learn

Responsibilities:

- Predict Financial Loss
- Predict Claim Amount
- Risk Classification

---

# Reporting Layer

Technology:

- PDF
- Excel
- Power BI

Responsibilities:

- Executive Reports
- CAT Reports
- Risk Reports
- Dashboard Analytics



                  USER
                    │
                    ▼
         Web Browser (Chrome/Edge)
                    │
                    ▼
      Frontend (HTML + CSS + JavaScript)
                    │
        HTTP Request / Response
                    │
                    ▼
      Flask Backend (Python APIs)
                    │
     ┌──────────────┼───────────────┐
     │              │               │
     ▼              ▼               ▼
 MySQL DB      ML Prediction     Report Engine
     │              │               │
     └──────────────┼───────────────┘
                    ▼
            Power BI Dashboard