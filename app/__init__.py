from sqlalchemy import Column, Integer, String, Text, Date, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class TRAComplianceStatus(Base):
    __tablename__ = "TRA_COMPLIANCE_STATUS"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String(50), nullable=False)


class TRA_CERT_STATUS(Base):
    __tablename__ = "TRA_CERT_STATUS"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String(50), nullable=False)


class TRA_CERT_TYPE(Base):
    __tablename__ = "TRA_CERT_TYPE"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String(50), nullable=False)


class TRA_RISK_LEVEL(Base):
    __tablename__ = "TRA_RISK_LEVEL"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String(50), nullable=False)


class TRA_STATION_STATUS(Base):
    __tablename__ = "TRA_STATION_STATUS"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String(50), nullable=False)


class TRA_ASSIGNMENT_STATUS(Base):
    __tablename__ = "TRA_ASSIGNMENT_STATUS"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String(50), nullable=False)


class TRA_TIP_STATUS(Base):
    __tablename__ = "TRA_TIP_STATUS"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String(50), nullable=False)


class TRA_STAFF(Base):
    __tablename__ = "TRA_STAFF"
    staff_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(150), nullable=True)
    role = Column(String(20), nullable=False)
    specialization = Column(String(100), nullable=True)
    compliance_status_id = Column(Integer, ForeignKey("TRA_COMPLIANCE_STATUS.id"), nullable=True)
    photo = Column(Integer, nullable=True)


class TRA_CERTIFICATION(Base):
    __tablename__ = "TRA_CERTIFICATION"
    certification_id = Column(Integer, primary_key=True, index=True)
    staff_id = Column(Integer, ForeignKey("TRA_STAFF.staff_id"), nullable=False)
    type_id = Column(Integer, ForeignKey("TRA_CERT_TYPE.id"), nullable=True)
    cert_level = Column(String(50), nullable=True)
    expiration = Column(Date, nullable=True)
    status_id = Column(Integer, ForeignKey("TRA_CERT_STATUS.id"), nullable=True)


class TRA_STATION(Base):
    __tablename__ = "TRA_STATION"
    station_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    location = Column(String(150), nullable=True)
    risk_level_id = Column(Integer, ForeignKey("TRA_RISK_LEVEL.id"), nullable=True)
    status_id = Column(Integer, ForeignKey("TRA_STATION_STATUS.id"), nullable=True)


class TRA_ASSIGNMENT(Base):
    __tablename__ = "TRA_ASSIGNMENT"
    assignment_id = Column(Integer, primary_key=True, index=True)
    staff_id = Column(Integer, ForeignKey("TRA_STAFF.staff_id"), nullable=False)
    station_id = Column(Integer, ForeignKey("TRA_STATION.station_id"), nullable=False)
    shift_date = Column(Date, nullable=True)
    status_id = Column(Integer, ForeignKey("TRA_ASSIGNMENT_STATUS.id"), nullable=True)
    status_explanation = Column(String(255), nullable=True)


class TRA_INCIDENT(Base):
    __tablename__ = "TRA_INCIDENT"
    incident_id = Column(Integer, primary_key=True, index=True)
    summary = Column(Text, nullable=True)
    station_id = Column(Integer, ForeignKey("TRA_STATION.station_id"), nullable=True)
    staff_id = Column(Integer, ForeignKey("TRA_STAFF.staff_id"), nullable=True)
    incident_date = Column(DateTime, default=datetime.utcnow)
    incident_type = Column(String(100), nullable=True)
    item_name = Column(String(150), nullable=True)
    photo = Column(String(255), nullable=True)
    policy_recommendation = Column(String(255), nullable=True)
    status = Column(String(50), default="Open")


class TRA_WITNESS(Base):
    __tablename__ = "TRA_WITNESS"
    witness_id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(Integer, ForeignKey("TRA_INCIDENT.incident_id"), nullable=False)
    staff_id = Column(Integer, ForeignKey("TRA_STAFF.staff_id"), nullable=True)
    involvement_type_id = Column(Integer, nullable=True)


class TRA_INTERVIEW(Base):
    __tablename__ = "TRA_INTERVIEW"
    interview_id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(Integer, ForeignKey("TRA_INCIDENT.incident_id"), nullable=False)
    staff_id = Column(Integer, ForeignKey("TRA_STAFF.staff_id"), nullable=True)
    statement = Column(Text, nullable=True)


class TRA_EVIDENCE(Base):
    __tablename__ = "TRA_EVIDENCE"
    evidence_id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(Integer, ForeignKey("TRA_INCIDENT.incident_id"), nullable=False)
    description = Column(String(255), nullable=True)
    station_id = Column(Integer, ForeignKey("TRA_STATION.station_id"), nullable=True)
    source_id = Column(Integer, nullable=True)
    photo = Column(String(255), nullable=True)


class TRA_CUSTOMER_TIP(Base):
    __tablename__ = "TRA_CUSTOMER_TIP"
    tip_id = Column(Integer, primary_key=True, index=True)
    description = Column(Text, nullable=True)
    location = Column(String(150), nullable=True)
    time_reported = Column(DateTime, default=datetime.utcnow)
    guest_name = Column(String(100), nullable=True)
    guest_email = Column(String(150), nullable=True)
    image_attachment = Column(String(255), nullable=True)
    status_id = Column(Integer, ForeignKey("TRA_TIP_STATUS.id"), nullable=True)
    created_on = Column(DateTime, default=datetime.utcnow)


class TRA_POLICY(Base):
    __tablename__ = "TRA_POLICY"
    policy_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=True)
    policy_category = Column(String(100), nullable=True)
    document = Column(String(255), nullable=True)
