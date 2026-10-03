from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


# Reference / Lookup Tables
class TRACertStatus(Base):
    __tablename__ = "TRA_CERT_STATUS"
    id = Column(Integer, primary_key=True)
    value = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    sort_order = Column(Integer)


class TRACertType(Base):
    __tablename__ = "TRA_CERT_TYPE"
    id = Column(Integer, primary_key=True)
    value = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    sort_order = Column(Integer)


class TRAComplianceStatus(Base):
    __tablename__ = "TRA_COMPLIANCE_STATUS"
    id = Column(Integer, primary_key=True)
    value = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    sort_order = Column(Integer)


class TRARiskLevel(Base):
    __tablename__ = "TRA_RISK_LEVEL"
    id = Column(Integer, primary_key=True)
    value = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    sort_order = Column(Integer)


class TRAStationStatus(Base):
    __tablename__ = "TRA_STATION_STATUS"
    id = Column(Integer, primary_key=True)
    value = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    sort_order = Column(Integer)


class TRAAssignmentStatus(Base):
    __tablename__ = "TRA_ASSIGNMENT_STATUS"
    id = Column(Integer, primary_key=True)
    value = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    sort_order = Column(Integer)


class TRAInvolvementType(Base):
    __tablename__ = "TRA_INVOLVEMENT_TYPE"
    id = Column(Integer, primary_key=True)
    value = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    sort_order = Column(Integer)


class TRAEvidenceSource(Base):
    __tablename__ = "TRA_EVIDENCE_SOURCE"
    id = Column(Integer, primary_key=True)
    value = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    sort_order = Column(Integer)


class TRATipStatus(Base):
    __tablename__ = "TRA_TIP_STATUS"
    id = Column(Integer, primary_key=True)
    value = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    sort_order = Column(Integer)


# Core Tables
class TRAStaff(Base):
    __tablename__ = "TRA_STAFF"
    staff_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(150))
    role = Column(String(20), nullable=False)
    specialization = Column(String(100))
    compliance_status_id = Column(Integer, ForeignKey("TRA_COMPLIANCE_STATUS.id"))
    photo = Column(Integer)

    certifications = relationship("TRACertification", back_populates="staff")
    assignments = relationship("TRAAssignment", back_populates="staff")
    incidents = relationship("TRAIncident", back_populates="staff")
    witnesses = relationship("TRAWitness", back_populates="staff")
    interviews = relationship("TRAInterview", back_populates="staff")


class TRACertification(Base):
    __tablename__ = "TRA_CERTIFICATION"
    certification_id = Column(Integer, primary_key=True)
    staff_id = Column(Integer, ForeignKey("TRA_STAFF.staff_id"), nullable=False)
    type_id = Column(Integer, ForeignKey("TRA_CERT_TYPE.id"))
    cert_level = Column(String(50))
    expiration = Column(Date)
    status_id = Column(Integer, ForeignKey("TRA_CERT_STATUS.id"))

    staff = relationship("TRAStaff", back_populates="certifications")


class TRAStation(Base):
    __tablename__ = "TRA_STATION"
    station_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    location = Column(String(150))
    risk_level_id = Column(Integer, ForeignKey("TRA_RISK_LEVEL.id"))
    status_id = Column(Integer, ForeignKey("TRA_STATION_STATUS.id"))

    assignments = relationship("TRAAssignment", back_populates="station")
    incidents = relationship("TRAIncident", back_populates="station")


class TRAAssignment(Base):
    __tablename__ = "TRA_ASSIGNMENT"
    assignment_id = Column(Integer, primary_key=True)
    staff_id = Column(Integer, ForeignKey("TRA_STAFF.staff_id"), nullable=False)
    station_id = Column(Integer, ForeignKey("TRA_STATION.station_id"), nullable=False)
    shift_date = Column(Date)
    status_id = Column(Integer, ForeignKey("TRA_ASSIGNMENT_STATUS.id"))
    status_explanation = Column(String(255))

    staff = relationship("TRAStaff", back_populates="assignments")
    station = relationship("TRAStation", back_populates="assignments")


class TRAIncident(Base):
    __tablename__ = "TRA_INCIDENT"
    incident_id = Column(Integer, primary_key=True)
    summary = Column(Text)
    station_id = Column(Integer, ForeignKey("TRA_STATION.station_id"))
    staff_id = Column(Integer, ForeignKey("TRA_STAFF.staff_id"))
    incident_date = Column(DateTime)
    incident_type = Column(String(100))
    item_name = Column(String(150))
    photo = Column(Integer)
    policy_recommendation = Column(String(255))

    station = relationship("TRAStation", back_populates="incidents")
    staff = relationship("TRAStaff", back_populates="incidents")
    witnesses = relationship("TRAWitness", back_populates="incident")
    interviews = relationship("TRAInterview", back_populates="incident")
    evidence_list = relationship("TRAEvidence", back_populates="incident")


class TRAWitness(Base):
    __tablename__ = "TRA_WITNESS"
    witness_id = Column(Integer, primary_key=True)
    incident_id = Column(Integer, ForeignKey("TRA_INCIDENT.incident_id"), nullable=False)
    staff_id = Column(Integer, ForeignKey("TRA_STAFF.staff_id"))
    involvement_type_id = Column(Integer, ForeignKey("TRA_INVOLVEMENT_TYPE.id"))

    incident = relationship("TRAIncident", back_populates="witnesses")
    staff = relationship("TRAStaff", back_populates="witnesses")


class TRAInterview(Base):
    __tablename__ = "TRA_INTERVIEW"
    interview_id = Column(Integer, primary_key=True)
    incident_id = Column(Integer, ForeignKey("TRA_INCIDENT.incident_id"), nullable=False)
    staff_id = Column(Integer, ForeignKey("TRA_STAFF.staff_id"))
    statement = Column(Text)

    incident = relationship("TRAIncident", back_populates="interviews")
    staff = relationship("TRAStaff", back_populates="interviews")


class TRAEvidence(Base):
    __tablename__ = "TRA_EVIDENCE"
    evidence_id = Column(Integer, primary_key=True)
    incident_id = Column(Integer, ForeignKey("TRA_INCIDENT.incident_id"), nullable=False)
    description = Column(String(255))
    station_id = Column(Integer, ForeignKey("TRA_STATION.station_id"))
    source_id = Column(Integer, ForeignKey("TRA_EVIDENCE_SOURCE.id"))
    photo = Column(Integer)

    incident = relationship("TRAIncident", back_populates="evidence_list")


class TRACustomerTip(Base):
    __tablename__ = "TRA_CUSTOMER_TIP"
    tip_id = Column(Integer, primary_key=True)
    description = Column(Text)
    location = Column(String(150))
    time_reported = Column(DateTime)
    guest_name = Column(String(100))
    guest_email = Column(String(150))
    image_attachment = Column(Integer)
    status_id = Column(Integer, ForeignKey("TRA_TIP_STATUS.id"))
    created_on = Column(DateTime, default=datetime.utcnow)


class TRAPolicy(Base):
    __tablename__ = "TRA_POLICY"
    policy_id = Column(Integer, primary_key=True)
    title = Column(String(150))
    policy_category = Column(String(100))
    document = Column(Integer)
