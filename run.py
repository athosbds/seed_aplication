from controllers.database import Base, engine
import controllers.models
from seed.seeds import seed_data
# CRIAÇÃO DO BANCO DE DADOS E CARREGANDO OS DADOS JSON
print("Criando tabelas.")
Base.metadata.create_all(bind=engine)
seed_data()
