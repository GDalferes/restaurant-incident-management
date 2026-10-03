from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import health, staff, incidents, assignments, tips, stations, certifications

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="The Rusty Anchor Incident Management System",
    description="Restaurant incident tracking, staff certification, and customer tip intake for The Rusty Anchor diner.",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, tags=["health"])
app.include_router(staff.router, prefix="/api/staff", tags=["staff"])
app.include_router(incidents.router, prefix="/api/incidents", tags=["incidents"])
app.include_router(assignments.router, prefix="/api/assignments", tags=["assignments"])
app.include_router(tips.router, prefix="/api/tips", tags=["tips"])
app.include_router(stations.router, prefix="/api/stations", tags=["stations"])
app.include_router(certifications.router, prefix="/api/certifications", tags=["certifications"])


@app.get("/")
def read_root():
    return {
        "message": "Welcome to The Rusty Anchor Incident Management System",
        "documentation": "/docs",
    }
