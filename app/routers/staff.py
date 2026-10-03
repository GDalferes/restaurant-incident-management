from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import TRAStaff
from app.schemas import StaffCreate, StaffResponse

router = APIRouter()


@router.get("/", response_model=list[StaffResponse])
def list_staff(db: Session = Depends(get_db)):
    """List all staff members."""
    staff = db.query(TRAStaff).all()
    return staff


@router.post("/", response_model=StaffResponse, status_code=status.HTTP_201_CREATED)
def create_staff(staff: StaffCreate, db: Session = Depends(get_db)):
    """Create a new staff member."""
    db_staff = TRAStaff(**staff.model_dump())
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    return db_staff


@router.get("/{staff_id}", response_model=StaffResponse)
def get_staff(staff_id: int, db: Session = Depends(get_db)):
    """Get a specific staff member by ID."""
    staff = db.query(TRAStaff).filter(TRAStaff.staff_id == staff_id).first()
    if not staff:
        raise HTTPException(status_code=404, detail="Staff member not found")
    return staff


@router.patch("/{staff_id}", response_model=StaffResponse)
def update_staff(staff_id: int, staff_update: StaffCreate, db: Session = Depends(get_db)):
    """Update a staff member."""
    staff = db.query(TRAStaff).filter(TRAStaff.staff_id == staff_id).first()
    if not staff:
        raise HTTPException(status_code=404, detail="Staff member not found")

    for field, value in staff_update.model_dump(exclude_unset=True).items():
        setattr(staff, field, value)

    db.commit()
    db.refresh(staff)
    return staff
