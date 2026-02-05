
from sqlalchemy.orm import Session
import models

def create_address(db: Session, address):
    obj = models.Address(**address.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_addresses(db: Session):
    return db.query(models.Address).all()

def get_address(db: Session, address_id: int):
    return db.query(models.Address).filter(models.Address.id == address_id).first()

def update_address(db: Session, address_id: int, address):
    obj = get_address(db, address_id)
    if not obj:
        return None
    for k, v in address.dict().items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj

def delete_address(db: Session, address_id: int):
    obj = get_address(db, address_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
