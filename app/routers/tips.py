from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import TRACustomerTip, TRAIncident
from app.schemas import CustomerTipCreate, CustomerTipResponse, CustomerTipUpdate

router = APIRouter()


@router.get("/", response_model=list[CustomerTipResponse])
def list_tips(db: Session = Depends(get_db)):
    """List all customer tips."""
    tips = db.query(TRACustomerTip).all()
    return tips


@router.post("/", response_model=CustomerTipResponse, status_code=status.HTTP_201_CREATED)
def create_tip(tip: CustomerTipCreate, db: Session = Depends(get_db)):
    """Create a new customer tip (public endpoint, no authentication required)."""
    db_tip = TRACustomerTip(**tip.model_dump())
    db.add(db_tip)
    db.commit()
    db.refresh(db_tip)
    return db_tip


@router.get("/{tip_id}", response_model=CustomerTipResponse)
def get_tip(tip_id: int, db: Session = Depends(get_db)):
    """Get a specific tip by ID."""
    tip = db.query(TRACustomerTip).filter(TRACustomerTip.tip_id == tip_id).first()
    if not tip:
        raise HTTPException(status_code=404, detail="Tip not found")
    return tip


@router.patch("/{tip_id}", response_model=CustomerTipResponse)
def update_tip(tip_id: int, tip_update: CustomerTipUpdate, db: Session = Depends(get_db)):
    """Update a tip (typically to change status)."""
    tip = db.query(TRACustomerTip).filter(TRACustomerTip.tip_id == tip_id).first()
    if not tip:
        raise HTTPException(status_code=404, detail="Tip not found")

    for field, value in tip_update.model_dump(exclude_unset=True).items():
        setattr(tip, field, value)

    db.commit()
    db.refresh(tip)
    return tip


@router.post("/{tip_id}/convert", response_model=dict)
def convert_tip_to_incident(tip_id: int, db: Session = Depends(get_db)):
    """Convert a customer tip into a formal incident."""
    tip = db.query(TRACustomerTip).filter(TRACustomerTip.tip_id == tip_id).first()
    if not tip:
        raise HTTPException(status_code=404, detail="Tip not found")

    # Create incident from tip
    incident = TRAIncident(
        summary=tip.description,
        incident_type="Customer Tip",
        incident_date=tip.time_reported,
        station_id=None,  # Can be set by manager later
        staff_id=None,    # Can be set by manager later
    )
    db.add(incident)
    db.commit()
    db.refresh(incident)

    # Update tip status
    tip.status_id = 3  # "Converted to Incident"
    db.commit()

    return {
        "message": "Tip converted to incident",
        "incident_id": incident.incident_id,
        "tip_id": tip.tip_id,
    }
