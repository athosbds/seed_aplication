from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .database import Base

# CLASSES FEITA COM ORM SQLALCHEMY INTEGRADAS AO BANCO DE DADOS LOCAL
class Merchant(Base):
    __tablename__ = "merchants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    country = Column(String, nullable=False)
class Lender(Base):
    __tablename__ = "lenders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    rating = Column(String, nullable=True)
class RateCard(Base):
    __tablename__ = "rate_cards"

    id = Column(Integer, primary_key=True, index=True)
    lender_id = Column(Integer, ForeignKey("lenders.id"), nullable=False)
    plan_name = Column(String, nullable=False)
    installments = Column(Integer, nullable=False)
    interest_rate = Column(Float, nullable=False)
class RiskPolicy(Base):
    __tablename__ = "risk_policies"

    id = Column(Integer, primary_key=True, index=True)
    lender_id = Column(Integer, ForeignKey("lenders.id"), nullable=False)
    rule = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
