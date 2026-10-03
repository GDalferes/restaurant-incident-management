from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import TRACertification
from app.schemas import CertificationCreate, CertificationResponse

router = APIRouter()


@router.get("/", response_model=list[CertificationResponse])
def list_certifications(db: Session = Depends(get_db)):
    """List all certifications."""
    certs = db.query(TRACertification).all()
    return certs


@router.post("/", response_model=CertificationResponse, status_code=status.HTTP_201_CREATED)
def create_certification(cert: CertificationCreate, db: Session = Depends(get_db)):
    """Create a new certification."""
    db_cert = TRACertification(**cert.model_dump())
    db.add(db_cert)
    db.commit()
    db.refresh(db_cert)
    return db_cert


@router.get("/{cert_id}", response_model=CertificationResponse)
def get_certification(cert_id: int, db: Session = Depends(get_db)):
    """Get a specific certification by ID."""
    cert = db.query(TRACertification).filter(TRACertification.certification_id == cert_id).first()
    if not cert:
        raise HTTPException(status_code=404, detail="Certification not found")
    return cert


@router.get("/staff/{staff_id}", response_model=list[CertificationResponse])
def get_staff_certifications(staff_id: int, db: Session = Depends(get_db)):
    """Get all certifications for a specific staff member."""
    certs = db.query(TRACertification).filter(TRACertification.staff_id == staff_id).all()
    return certs
