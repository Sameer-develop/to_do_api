from sqlalchemy.orm import Session
from app.models.person import Person
from app.schemas.person_schema import PersonCreate

def create_person(db: Session, person: PersonCreate):
    db_person = Person(name=person.name, age=person.age, city=person.city)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def get_persons(db: Session):
    return db.query(Person).all()
