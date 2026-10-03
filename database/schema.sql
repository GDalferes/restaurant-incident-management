-- iShift Hackathon: The Rusty Anchor Data Model
-- Converted from MySQL to PostgreSQL syntax

-- Reference / lookup tables

CREATE TABLE TRA_CERT_STATUS (
  id            SERIAL PRIMARY KEY,
  value         VARCHAR(50) NOT NULL,
  is_active     BOOLEAN DEFAULT true,
  sort_order    INT
);

CREATE TABLE TRA_CERT_TYPE (
  id            SERIAL PRIMARY KEY,
  value         VARCHAR(50) NOT NULL,
  is_active     BOOLEAN DEFAULT true,
  sort_order    INT
);

CREATE TABLE TRA_COMPLIANCE_STATUS (
  id            SERIAL PRIMARY KEY,
  value         VARCHAR(50) NOT NULL,
  is_active     BOOLEAN DEFAULT true,
  sort_order    INT
);

CREATE TABLE TRA_RISK_LEVEL (
  id            SERIAL PRIMARY KEY,
  value         VARCHAR(50) NOT NULL,
  is_active     BOOLEAN DEFAULT true,
  sort_order    INT
);

CREATE TABLE TRA_STATION_STATUS (
  id            SERIAL PRIMARY KEY,
  value         VARCHAR(50) NOT NULL,
  is_active     BOOLEAN DEFAULT true,
  sort_order    INT
);

CREATE TABLE TRA_ASSIGNMENT_STATUS (
  id            SERIAL PRIMARY KEY,
  value         VARCHAR(50) NOT NULL,
  is_active     BOOLEAN DEFAULT true,
  sort_order    INT
);

CREATE TABLE TRA_INVOLVEMENT_TYPE (
  id            SERIAL PRIMARY KEY,
  value         VARCHAR(50) NOT NULL,
  is_active     BOOLEAN DEFAULT true,
  sort_order    INT
);

CREATE TABLE TRA_EVIDENCE_SOURCE (
  id            SERIAL PRIMARY KEY,
  value         VARCHAR(50) NOT NULL,
  is_active     BOOLEAN DEFAULT true,
  sort_order    INT
);

CREATE TABLE TRA_TIP_STATUS (
  id            SERIAL PRIMARY KEY,
  value         VARCHAR(50) NOT NULL,
  is_active     BOOLEAN DEFAULT true,
  sort_order    INT
);

-- Core tables

CREATE TABLE TRA_STAFF (
  staff_id            SERIAL PRIMARY KEY,
  name                VARCHAR(100) NOT NULL,
  username            VARCHAR(50) NOT NULL UNIQUE,
  password            VARCHAR(100) NOT NULL,
  email               VARCHAR(150),
  role                VARCHAR(20) NOT NULL,
  specialization      VARCHAR(100),
  compliance_status_id INT,
  photo               INT,
  FOREIGN KEY (compliance_status_id) REFERENCES TRA_COMPLIANCE_STATUS(id)
);

CREATE TABLE TRA_CERTIFICATION (
  certification_id    SERIAL PRIMARY KEY,
  staff_id            INT NOT NULL,
  type_id             INT,
  cert_level          VARCHAR(50),
  expiration          DATE,
  status_id           INT,
  FOREIGN KEY (staff_id) REFERENCES TRA_STAFF(staff_id),
  FOREIGN KEY (type_id) REFERENCES TRA_CERT_TYPE(id),
  FOREIGN KEY (status_id) REFERENCES TRA_CERT_STATUS(id)
);

CREATE TABLE TRA_STATION (
  station_id          SERIAL PRIMARY KEY,
  name                VARCHAR(100) NOT NULL,
  location            VARCHAR(150),
  risk_level_id       INT,
  status_id           INT,
  FOREIGN KEY (risk_level_id) REFERENCES TRA_RISK_LEVEL(id),
  FOREIGN KEY (status_id) REFERENCES TRA_STATION_STATUS(id)
);

CREATE TABLE TRA_ASSIGNMENT (
  assignment_id       SERIAL PRIMARY KEY,
  staff_id            INT NOT NULL,
  station_id          INT NOT NULL,
  shift_date          DATE,
  status_id           INT,
  status_explanation  VARCHAR(255),
  FOREIGN KEY (staff_id) REFERENCES TRA_STAFF(staff_id),
  FOREIGN KEY (station_id) REFERENCES TRA_STATION(station_id),
  FOREIGN KEY (status_id) REFERENCES TRA_ASSIGNMENT_STATUS(id)
);

CREATE TABLE TRA_INCIDENT (
  incident_id         SERIAL PRIMARY KEY,
  summary             TEXT,
  station_id          INT,
  staff_id            INT,
  incident_date       TIMESTAMP,
  incident_type       VARCHAR(100),
  item_name           VARCHAR(150),
  photo               INT,
  policy_recommendation VARCHAR(255),
  FOREIGN KEY (station_id) REFERENCES TRA_STATION(station_id),
  FOREIGN KEY (staff_id) REFERENCES TRA_STAFF(staff_id)
);

CREATE TABLE TRA_WITNESS (
  witness_id          SERIAL PRIMARY KEY,
  incident_id         INT NOT NULL,
  staff_id            INT,
  involvement_type_id INT,
  FOREIGN KEY (incident_id) REFERENCES TRA_INCIDENT(incident_id),
  FOREIGN KEY (staff_id) REFERENCES TRA_STAFF(staff_id),
  FOREIGN KEY (involvement_type_id) REFERENCES TRA_INVOLVEMENT_TYPE(id)
);

CREATE TABLE TRA_INTERVIEW (
  interview_id        SERIAL PRIMARY KEY,
  incident_id         INT NOT NULL,
  staff_id            INT,
  statement           TEXT,
  FOREIGN KEY (incident_id) REFERENCES TRA_INCIDENT(incident_id),
  FOREIGN KEY (staff_id) REFERENCES TRA_STAFF(staff_id)
);

CREATE TABLE TRA_EVIDENCE (
  evidence_id         SERIAL PRIMARY KEY,
  incident_id         INT NOT NULL,
  description         VARCHAR(255),
  station_id          INT,
  source_id           INT,
  photo               INT,
  FOREIGN KEY (incident_id) REFERENCES TRA_INCIDENT(incident_id),
  FOREIGN KEY (station_id) REFERENCES TRA_STATION(station_id),
  FOREIGN KEY (source_id) REFERENCES TRA_EVIDENCE_SOURCE(id)
);

CREATE TABLE TRA_CUSTOMER_TIP (
  tip_id              SERIAL PRIMARY KEY,
  description         TEXT,
  location            VARCHAR(150),
  time_reported       TIMESTAMP,
  guest_name          VARCHAR(100),
  guest_email         VARCHAR(150),
  image_attachment    INT,
  status_id           INT,
  created_on          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (status_id) REFERENCES TRA_TIP_STATUS(id)
);

CREATE TABLE TRA_POLICY (
  policy_id           SERIAL PRIMARY KEY,
  title               VARCHAR(150),
  policy_category     VARCHAR(100),
  document            INT
);

-- ============================================================
-- Seed data for reference / lookup tables
-- ============================================================

INSERT INTO TRA_CERT_TYPE (value, is_active, sort_order) VALUES
  ('Food Handler Certification', true, 1),
  ('Grill Safety Certification', true, 2),
  ('Recipe Security Clearance', true, 3),
  ('First Aid / CPR', true, 4);

INSERT INTO TRA_CERT_STATUS (value, is_active, sort_order) VALUES
  ('Active', true, 1),
  ('Expired', true, 2),
  ('Pending Review', true, 3);

INSERT INTO TRA_COMPLIANCE_STATUS (value, is_active, sort_order) VALUES
  ('Compliant', true, 1),
  ('Non-Compliant', true, 2),
  ('Under Review', true, 3);

INSERT INTO TRA_RISK_LEVEL (value, is_active, sort_order) VALUES
  ('Low', true, 1),
  ('Medium', true, 2),
  ('High', true, 3);

INSERT INTO TRA_STATION_STATUS (value, is_active, sort_order) VALUES
  ('Open', true, 1),
  ('Closed', true, 2),
  ('Under Cleaning', true, 3);

INSERT INTO TRA_ASSIGNMENT_STATUS (value, is_active, sort_order) VALUES
  ('Pending', true, 1),
  ('Approved', true, 2),
  ('Blocked', true, 3);

INSERT INTO TRA_INVOLVEMENT_TYPE (value, is_active, sort_order) VALUES
  ('Witness', true, 1),
  ('Reporting Staff', true, 2),
  ('Customer', true, 3),
  ('Bystander', true, 4);

INSERT INTO TRA_EVIDENCE_SOURCE (value, is_active, sort_order) VALUES
  ('Staff Submission', true, 1),
  ('Customer Submission', true, 2),
  ('Security Footage', true, 3),
  ('Photo', true, 4);

INSERT INTO TRA_TIP_STATUS (value, is_active, sort_order) VALUES
  ('New', true, 1),
  ('Reviewed', true, 2),
  ('Converted to Incident', true, 3),
  ('Dismissed', true, 4);

-- ============================================================
-- Seed data: sample kitchen/dining stations
-- ============================================================

INSERT INTO TRA_STATION (name, location, risk_level_id, status_id) VALUES
  ('Fry Station', 'Back Kitchen', 3, 1),
  ('Grill Line', 'Back Kitchen', 3, 1),
  ('Walk-In Freezer', 'Storage Wing', 2, 1),
  ('Dining Floor', 'Main Hall', 1, 1),
  ('Secret Sauce Vault', 'Restricted Wing', 3, 2);

-- ============================================================
-- Seed data: sample staff & manager (login accounts included)
-- ============================================================

INSERT INTO TRA_STAFF (name, username, password, email, role, specialization, compliance_status_id, photo) VALUES
  ('Chip Barnacle', 'mgr.chip', 'password123', 'chip.barnacle@rustyanchor.com', 'Manager', NULL, 1, NULL),
  ('Marlin Fintastic', 'staff.marlin', 'password123', 'marlin.fintastic@rustyanchor.com', 'Staff', 'Fry Cook', 1, NULL),
  ('Coral Finley', 'staff.coral', 'password123', 'coral.finley@rustyanchor.com', 'Staff', 'Grill Specialist', 1, NULL),
  ('Gil Waverly', 'staff.gil', 'password123', 'gil.waverly@rustyanchor.com', 'Staff', 'Server / Host', 3, NULL),
  ('Barry Cuda', 'staff.barry', 'password123', 'barry.cuda@rustyanchor.com', 'Staff', 'Dishwashing & Sanitation', 2, NULL);