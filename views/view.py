from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers.database import SessionLocal
from controllers.models import RateCard, Lender

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/offers")
def list_offers(db: Session = Depends(get_db)):
    offers = db.query(RateCard).all()
    response = []
    for offer in offers:
        lender = db.query(Lender).filter(Lender.id == offer.lender_id).first()
        response.append({
            "plan_name": offer.plan_name,
            "installments": offer.installments,
            "interest_rate": offer.interest_rate,
            "lender": lender.name if lender else None
        })
    return response