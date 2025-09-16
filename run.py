from controllers.database import Base, engine
import controllers.models
from seed.seeds import seed_data

print("Criando tabelas.")
Base.metadata.create_all(bind=engine)
seed_data()
