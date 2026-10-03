from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import TRAIncident, TRAWitness, TRAInterview, TRAEvidence
from app.schemas import (
    IncidentCreate,
    IncidentResponse,
    IncidentUpdate,
    WitnessCreate,
    WitnessResponse,
    InterviewCreate,
    InterviewResponse,
    EvidenceCreate,
    EvidenceResponse,
)

router = APIRouter()


@router.get("/", response_model=list[IncidentResponse])
def list_incidents(db: Session = Depends(get_db)):
    """List all incidents."""
    incidents = db.query(TRAIncident).all()
    return incidents


@router.post("/", response_model=IncidentResponse, status_code=status.HTTP_201_CREATED)
def create_incident(incident: IncidentCreate, db: Session = Depends(get_db)):
    """Create a new incident."""
    db_incident = TRAIncident(**incident.model_dump())
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident


@router.get("/{incident_id}", response_model=IncidentResponse)
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    """Get a specific incident by ID."""
    incident = db.query(TRAIncident).filter(TRAIncident.incident_id == incident_id).first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident


@router.patch("/{incident_id}", response_model=IncidentResponse)
def update_incident(incident_id: int, incident_update: IncidentUpdate, db: Session = Depends(get_db)):
    """Update an incident."""
    incident = db.query(TRAIncident).filter(TRAIncident.incident_id == incident_id).first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    for field, value in incident_update.model_dump(exclude_unset=True).items():
        setattr(incident, field, value)

    db.commit()
    db.refresh(incident)
    return incident


# Witness endpoints
@router.post("/{incident_id}/witnesses", response_model=WitnessResponse, status_code=status.HTTP_201_CREATED)
def add_witness(incident_id: int, witness: WitnessCreate, db: Session = Depends(get_db)):
    """Add a witness to an incident."""
    incident = db.query(TRAIncident).filter(TRAIncident.incident_id == incident_id).first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    db_witness = TRAWitness(**witness.model_dump())
    db.add(db_witness)
    db.commit()
    db.refresh(db_witness)
    return db_witness


# Interview endpoints
@router.post("/{incident_id}/interviews", response_model=InterviewResponse, status_code=status.HTTP_201_CREATED)
def add_interview(incident_id: int, interview: InterviewCreate, db: Session = Depends(get_db)):
    """Add an interview statement to an incident."""
    incident = db.query(TRAIncident).filter(TRAIncident.incident_id == incident_id).first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    db_interview = TRAInterview(**interview.model_dump())
    db.add(db_interview)
    db.commit()
    db.refresh(db_interview)
    return db_interview


# Evidence endpoints
@router.post("/{incident_id}/evidence", response_model=EvidenceResponse, status_code=status.HTTP_201_CREATED)
def add_evidence(incident_id: int, evidence: EvidenceCreate, db: Session = Depends(get_db)):
    """Add evidence to an incident."""
    incident = db.query(TRAIncident).filter(TRAIncident.incident_id == incident_id).first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    db_evidence = TRAEvidence(**evidence.model_dump())
    db.add(db_evidence)
    db.commit()
    db.refresh(db_evidence)
    return db_evidence
