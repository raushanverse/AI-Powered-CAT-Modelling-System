# REST API Design

## User Module

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /users | Get all users |
| GET | /users/<id> | Get user by ID |
| POST | /users | Create new user |
| PUT | /users/<id> | Update user |
| DELETE | /users/<id> | Delete user |

---

## Property Module

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /properties | Get all properties |
| POST | /properties | Add property |
| PUT | /properties/<id> | Update property |
| DELETE | /properties/<id> | Delete property |

---

## Policy Module

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /policies | Get all policies |
| POST | /policies | Create policy |
| PUT | /policies/<id> | Update policy |
| DELETE | /policies/<id> | Delete policy |

---

## Claims Module

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /claims | Get all claims |
| POST | /claims | Raise claim |
| PUT | /claims/<id> | Update claim status |

---

## AI Prediction Module

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /predict-risk | Predict catastrophe risk |
| GET | /predictions | View prediction history |

---

## Reinsurance Module

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /reinsurance | View reinsurance records |
| POST | /reinsurance | Create reinsurance record |