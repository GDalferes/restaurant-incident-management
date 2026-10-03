from datetime import datetime, date
from typing import Optional, List
from pydantic import BaseModel


# Staff Schemas
class StaffBase(BaseModel):
    name: str
    username: str
    email: Optional[str] = None
    role: str
    specialization: Optional[str] = None
    compliance_status_id: Optional[int] = None
    photo: Optional[int] = None


class StaffCreate(StaffBase):
    password: str


class StaffResponse(StaffBase):
    staff_id: int

    class Config:
        from_attributes = True


# Certification Schemas
class CertificationBase(BaseModel):
    staff_id: int
    type_id: Optional[int] = None
    cert_level: Optional[str] = None
    expiration: Optional[date] = None
    status_id: Optional[int] = None


class CertificationCreate(CertificationBase):
    pass


class CertificationResponse(CertificationBase):
    certification_id: int

    class Config:
        from_attributes = True


# Station Schemas
class StationBase(BaseModel):
    name: str
    location: Optional[str] = None
    risk_level_id: Optional[int] = None
    status_id: Optional[int] = None


class StationCreate(StationBase):
    pass


class StationResponse(StationBase):
    station_id: int

    class Config:
        from_attributes = True


# Assignment Schemas
class AssignmentBase(BaseModel):
    staff_id: int
    station_id: int
    shift_date: Optional[date] = None
    status_id: Optional[int] = None
    status_explanation: Optional[str] = None


class AssignmentCreate(AssignmentBase):
    pass


class AssignmentUpdate(BaseModel):
    status_id: Optional[int] = None
    status_explanation: Optional[str] = None


class AssignmentResponse(AssignmentBase):
    assignment_id: int

    class Config:
        from_attributes = True


# Incident Schemas
class IncidentBase(BaseModel):
    summary: Optional[str] = None
    station_id: Optional[int] = None
    staff_id: Optional[int] = None
    incident_date: Optional[datetime] = None
    incident_type: Optional[str] = None
    item_name: Optional[str] = None
    photo: Optional[int] = None
    policy_recommendation: Optional[str] = None


class IncidentCreate(IncidentBase):
    pass


class IncidentUpdate(BaseModel):
    summary: Optional[str] = None
    station_id: Optional[int] = None
    staff_id: Optional[int] = None
    incident_type: Optional[str] = None
    item_name: Optional[str] = None
    policy_recommendation: Optional[str] = None


class IncidentResponse(IncidentBase):
    incident_id: int

    class Config:
        from_attributes = True


# Witness Schemas
class WitnessBase(BaseModel):
    incident_id: int
    staff_id: Optional[int] = None
    involvement_type_id: Optional[int] = None


class WitnessCreate(WitnessBase):
    pass


class WitnessResponse(WitnessBase):
    witness_id: int

    class Config:
        from_attributes = True


# Interview Schemas
class InterviewBase(BaseModel):
    incident_id: int
    staff_id: Optional[int] = None
    statement: Optional[str] = None


class InterviewCreate(InterviewBase):
    pass


class InterviewResponse(InterviewBase):
    interview_id: int

    class Config:
        from_attributes = True


# Evidence Schemas
class EvidenceBase(BaseModel):
    incident_id: int
    description: Optional[str] = None
    station_id: Optional[int] = None
    source_id: Optional[int] = None
    photo: Optional[int] = None


class EvidenceCreate(EvidenceBase):
    pass


class EvidenceResponse(EvidenceBase):
    evidence_id: int

    class Config:
        from_attributes = True


# Customer Tip Schemas
class CustomerTipBase(BaseModel):
    description: Optional[str] = None
    location: Optional[str] = None
    time_reported: Optional[datetime] = None
    guest_name: Optional[str] = None
    guest_email: Optional[str] = None
    image_attachment: Optional[int] = None
    status_id: Optional[int] = None


class CustomerTipCreate(CustomerTipBase):
    pass


class CustomerTipUpdate(BaseModel):
    status_id: Optional[int] = None
    description: Optional[str] = None


class CustomerTipResponse(CustomerTipBase):
    tip_id: int
    created_on: datetime

    class Config:
        from_attributes = True


# Policy Schemas
class PolicyBase(BaseModel):
    title: Optional[str] = None
    policy_category: Optional[str] = None
    document: Optional[int] = None


class PolicyCreate(PolicyBase):
    pass


class PolicyResponse(PolicyBase):
    policy_id: int

    class Config:
        from_attributes = True
