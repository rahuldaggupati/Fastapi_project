
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db
import math

router = APIRouter(prefix="/addresses", tags=["addresses"])

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

@router.post("/", response_model=schemas.AddressResponse)
def create(addr: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db, addr)

@router.get("/", response_model=list[schemas.AddressResponse])
def list_all(db: Session = Depends(get_db)):
    return crud.get_addresses(db)

@router.put("/{address_id}", response_model=schemas.AddressResponse)
def update(address_id: int, addr: schemas.AddressCreate, db: Session = Depends(get_db)):
    obj = crud.update_address(db, address_id, addr)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.delete("/{address_id}")
def remove(address_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_address(db, address_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"message": "deleted"}

@router.get("/nearby", response_model=list[schemas.AddressResponse])
def nearby(lat: float, lon: float, distance_km: float, db: Session = Depends(get_db)):
    addresses = crud.get_addresses(db)
    return [a for a in addresses if haversine(lat, lon, a.latitude, a.longitude) <= distance_km]
