from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import PersonCreate, PersonResponse
from app.services import person_service
from app.core.database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PersonResponse)
def create_person(person: PersonCreate, db: Session = Depends(get_db)):
    return person_service.create_person(db, person)

@router.get("/", response_model=list[PersonResponse])
def read_persons(db: Session = Depends(get_db)):
    return person_service.get_persons(db)
