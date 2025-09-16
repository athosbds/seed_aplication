from controllers.database import SessionLocal
from controllers.models import Merchant

db = SessionLocal()
merchants = db.query(Merchant).all()
print(merchants)
db.close()
