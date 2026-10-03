# The Rusty Anchor Incident Management System

A complete restaurant incident tracking, staff certification management, and customer tip intake system for The Rusty Anchor diner.

## Overview

This is a backend API built with FastAPI and PostgreSQL that implements the full data model from The Rusty Anchor use case:

- **Staff Management** — track roles, specializations, compliance status, and certifications
- **Station Operations** — manage kitchen/dining stations with risk levels and operational status
- **Incident Reporting** — log incidents with witnesses, interviews, and evidence
- **Staff Assignments** — schedule staff to stations with approval/blocking workflow
- **Customer Tips** — anonymous public tip submissions with auto-conversion to incidents
- **Certifications** — track staff certification types, levels, and expiration dates

## Tech Stack

- **Backend:** Python 3.11+ with FastAPI
- **Database:** PostgreSQL 16
- **ORM:** SQLAlchemy 2.0
- **API Documentation:** Swagger UI & ReDoc (built-in)
- **Local Development:** Docker Compose for PostgreSQL

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── config.py              # Configuration settings
│   ├── database.py            # Database connection and session management
│   ├── main.py                # FastAPI application definition
│   ├── models.py              # SQLAlchemy models (exact schema)
│   ├── schemas.py             # Pydantic schemas for API requests/responses
│   └── routers/
│       ├── health.py          # Health check endpoint
│       ├── staff.py           # Staff CRUD endpoints
│       ├── incidents.py       # Incident, witness, interview, evidence endpoints
│       ├── assignments.py     # Assignment approval/blocking endpoints
│       ├── tips.py            # Customer tip and conversion endpoints
│       ├── stations.py        # Station management endpoints
│       └── certifications.py  # Certification tracking endpoints
├── database/
│   └── schema.sql             # Complete PostgreSQL schema + seed data
├── docker-compose.yml         # Docker setup for local PostgreSQL
├── requirements.txt           # Python dependencies
├── .env.example               # Environment variables template
└── README.md
```

## Quick Start

### 1. Prerequisites

- Python 3.11+
- Docker & Docker Compose
- Git

### 2. Clone and Setup

```bash
git clone https://github.com/GDalferes/restaurant-incident-management.git
cd restaurant-incident-management

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env
```

### 3. Start PostgreSQL

```bash
docker compose up -d
```

This will:
- Start a PostgreSQL 16 container on `localhost:5432`
- Create the database `rusty_anchor`
- Run the schema initialization with all tables and seed data

### 4. Run the API

```bash
uvicorn app.main:app --reload
```

The API will be available at:
- **API:** http://127.0.0.1:8000
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## Seeded Data

The database is automatically populated with:

### Staff
- `mgr.chip` (Manager) — Chip Barnacle
- `staff.marlin` (Fry Cook) — Marlin Fintastic
- `staff.coral` (Grill Specialist) — Coral Finley
- `staff.gil` (Server/Host) — Gil Waverly
- `staff.barry` (Dishwashing) — Barry Cuda

### Stations
- Fry Station (Back Kitchen, High Risk)
- Grill Line (Back Kitchen, High Risk)
- Walk-In Freezer (Storage Wing, Medium Risk)
- Dining Floor (Main Hall, Low Risk)
- Secret Sauce Vault (Restricted Wing, High Risk, Closed)

### Reference Data
- Certification Types: Food Handler, Grill Safety, Recipe Security, First Aid/CPR
- Statuses: Active, Expired, Pending Review (certs)
- Compliance Statuses: Compliant, Non-Compliant, Under Review
- Risk Levels: Low, Medium, High
- Assignment Statuses: Pending, Approved, Blocked
- Tip Statuses: New, Reviewed, Converted to Incident, Dismissed

## API Endpoints

### Staff Management
```
GET    /api/staff/           - List all staff
POST   /api/staff/           - Create new staff member
GET    /api/staff/{staff_id} - Get specific staff
PATCH  /api/staff/{staff_id} - Update staff
```

### Incidents
```
GET    /api/incidents/                        - List all incidents
POST   /api/incidents/                        - Create incident
GET    /api/incidents/{incident_id}          - Get incident
PATCH  /api/incidents/{incident_id}          - Update incident
POST   /api/incidents/{incident_id}/witnesses    - Add witness
POST   /api/incidents/{incident_id}/interviews   - Add interview
POST   /api/incidents/{incident_id}/evidence     - Add evidence
```

### Customer Tips
```
GET    /api/tips/              - List all tips
POST   /api/tips/              - Submit customer tip (public)
GET    /api/tips/{tip_id}      - Get specific tip
PATCH  /api/tips/{tip_id}      - Update tip status
POST   /api/tips/{tip_id}/convert - Convert tip to incident
```

### Assignments
```
GET    /api/assignments/                  - List all assignments
POST   /api/assignments/                  - Create assignment
GET    /api/assignments/{assignment_id}  - Get assignment
PATCH  /api/assignments/{assignment_id}  - Approve/block assignment
```

### Stations
```
GET  /api/stations/           - List all stations
POST /api/stations/           - Create station
GET  /api/stations/{station_id} - Get station
```

### Certifications
```
GET  /api/certifications/                   - List all certifications
POST /api/certifications/                   - Create certification
GET  /api/certifications/{cert_id}         - Get certification
GET  /api/certifications/staff/{staff_id}  - Get staff certifications
```

## Example API Calls

### Submit a Customer Tip (Public)

```bash
curl -X POST "http://127.0.0.1:8000/api/tips/" \
  -H "Content-Type: application/json" \
  -d '{
    "description": "The fryer oil looks dirty and smells burnt",
    "location": "Back Kitchen",
    "guest_name": "Anonymous",
    "guest_email": null,
    "status_id": 1
  }'
```

### Create an Incident

```bash
curl -X POST "http://127.0.0.1:8000/api/incidents/" \
  -H "Content-Type: application/json" \
  -d '{
    "summary": "Grease fire near fry station — contained by staff",
    "station_id": 1,
    "staff_id": 2,
    "incident_date": "2024-10-03T14:30:00",
    "incident_type": "Fire Hazard",
    "item_name": "Deep Fryer Unit A"
  }'
```

### Approve an Assignment

```bash
curl -X PATCH "http://127.0.0.1:8000/api/assignments/1" \
  -H "Content-Type: application/json" \
  -d '{
    "status_id": 2,
    "status_explanation": "All certifications verified"
  }'
```

### Convert a Tip to an Incident

```bash
curl -X POST "http://127.0.0.1:8000/api/tips/1/convert"
```

## Database Schema Notes

The schema uses:
- **Reference tables** (TRA_*_STATUS, TRA_RISK_LEVEL, etc.) for lookup values and extensibility
- **Foreign keys** for data integrity
- **SERIAL PRIMARY KEYS** for auto-incrementing IDs
- **Timestamps** for audit trails
- **TEXT fields** for detailed descriptions and statements

## Next Steps

1. **Authentication** — Add JWT-based login with role-based access control
2. **File Uploads** — Implement photo/document attachment storage (S3/local)
3. **Frontend** — Build React UI with manager dashboard and staff portal
4. **AI Integration** — Add classification, summarization, and anomaly detection
5. **Notifications** — Implement email/SMS alerts for status changes
6. **Reporting** — Add analytics and export (CSV/PDF) functionality

## Troubleshooting

### Database connection error

Make sure PostgreSQL is running:
```bash
docker compose ps
```

If not running, restart it:
```bash
docker compose up -d
```

### Port 5432 already in use

Change the port in `docker-compose.yml`:
```yaml
ports:
  - "5433:5432"  # Maps local 5433 to container 5432
```

Then update `.env`:
```
DATABASE_URL=postgresql://postgres:postgres@localhost:5433/rusty_anchor
```

### Tables not created

Verify the schema loaded:
```bash
docker compose logs db | grep "schema"
```

Or manually run the schema:
```bash
psql -U postgres -d rusty_anchor -h localhost -f database/schema.sql
```

## License

MIT
