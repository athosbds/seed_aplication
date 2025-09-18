
from controllers.database import SessionLocal
from controllers.models import Merchant
# VISUALIZAÇÃO DOS JSON DENTRO QUE FORAM INSERIDOS NO BANCO DE DADOS APP.DB
db = SessionLocal()
merchants = db.query(Merchant).all()
for merchant in merchants:
    print(f'ID: {merchant.id} - Nome: {merchant.name}')