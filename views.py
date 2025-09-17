from controllers.database import SessionLocal
from controllers.models import Merchant
# POSSIBILITANDO VISUALIZAÇÃO DO BANCO COM ORM SQLALCHEMY
db = SessionLocal()
merchants = db.query(Merchant).all()
print(merchants)
db.close()
