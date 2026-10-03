from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import TRAStation
from app.schemas import StationCreate, StationResponse

router = APIRouter()


@router.get("/", response_model=list[StationResponse])
def list_stations(db: Session = Depends(get_db)):
    """List all stations."""
    stations = db.query(TRAStation).all()
    return stations


@router.post("/", response_model=StationResponse, status_code=status.HTTP_201_CREATED)
def create_station(station: StationCreate, db: Session = Depends(get_db)):
    """Create a new station."""
    db_station = TRAStation(**station.model_dump())
    db.add(db_station)
    db.commit()
    db.refresh(db_station)
    return db_station


@router.get("/{station_id}", response_model=StationResponse)
def get_station(station_id: int, db: Session = Depends(get_db)):
    """Get a specific station by ID."""
    station = db.query(TRAStation).filter(TRAStation.station_id == station_id).first()
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")
    return station
