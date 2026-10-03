from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import TRAAssignment
from app.schemas import AssignmentCreate, AssignmentResponse, AssignmentUpdate

router = APIRouter()


@router.get("/", response_model=list[AssignmentResponse])
def list_assignments(db: Session = Depends(get_db)):
    """List all assignments."""
    assignments = db.query(TRAAssignment).all()
    return assignments


@router.post("/", response_model=AssignmentResponse, status_code=status.HTTP_201_CREATED)
def create_assignment(assignment: AssignmentCreate, db: Session = Depends(get_db)):
    """Create a new assignment."""
    db_assignment = TRAAssignment(**assignment.model_dump())
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment


@router.get("/{assignment_id}", response_model=AssignmentResponse)
def get_assignment(assignment_id: int, db: Session = Depends(get_db)):
    """Get a specific assignment by ID."""
    assignment = db.query(TRAAssignment).filter(TRAAssignment.assignment_id == assignment_id).first()
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return assignment


@router.patch("/{assignment_id}", response_model=AssignmentResponse)
def update_assignment(assignment_id: int, assignment_update: AssignmentUpdate, db: Session = Depends(get_db)):
    """Update an assignment (typically to approve/block)."""
    assignment = db.query(TRAAssignment).filter(TRAAssignment.assignment_id == assignment_id).first()
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")

    for field, value in assignment_update.model_dump(exclude_unset=True).items():
        setattr(assignment, field, value)

    db.commit()
    db.refresh(assignment)
    return assignment
