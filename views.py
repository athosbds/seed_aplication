from controllers.database import SessionLocal
from controllers.models import Merchant, Lender, RateCard, RiskPolicy

db = SessionLocal()
merchants = db.query(Merchant).all()
print("Merchants:", [m.__dict__ for m in merchants])
lender = db.query(Lender).filter(Lender.name == "Banco Alpha").first()
print("Lender filtrado:", lender.__dict__ if lender else None)
db.close()