import json
from controllers.database import SessionLocal
from controllers.models import Merchant, Lender, RateCard, RiskPolicy
# CONFIGURAÇÃO PARA CARREGAR OS JSONS
def load_json(file):
    with open(file, "r") as f:
        return json.load(f)
    
def seed_data():
    db = SessionLocal()
    try:
        merchants = load_json("seed/merchants.json")
        for m in merchants:
            db.merge(Merchant(**m))

        lenders = load_json("seed/lenders.json")
        for l in lenders:
            db.merge(Lender(**l))

        rate_cards = load_json("seed/rate_cards.json")
        for r in rate_cards:
            db.merge(RateCard(**r))

        risk_policy = load_json("seed/risk_policies.json")
        for ri in risk_policy:
            db.merge(RiskPolicy(**ri))
        db.commit()
        print("Dados inseridos.")
    finally:
        db.close()

        
    