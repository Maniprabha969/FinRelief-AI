from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from database import Base
from sqlalchemy.orm import relationship

# ==========================
# Users Table
# ==========================
class User(Base):
    __tablename__ = "users"

    UserID = Column(Integer, primary_key=True, index=True)
    Name = Column(String, nullable=False)
    Email = Column(String, unique=True, index=True, nullable=False)
    Password = Column(String, nullable=False)
    MonthlyIncome = Column(Float, nullable=False)
    MonthlyExpenses = Column(Float, nullable=False)
    loans = relationship("Loan", backref="user")

# ==========================
# Financial Profile Table
# ==========================
class FinancialProfile(Base):
    __tablename__ = "financial_profile"

    ProfileID = Column(Integer, primary_key=True, index=True)
    UserID = Column(Integer, ForeignKey("users.UserID"))

    EMI_Ratio = Column(Float)
    DTI_Ratio = Column(Float)
    MonthlySurplus = Column(Float)
    StressLevel = Column(String)


# ==========================
# Loans Table
# ==========================
class Loan(Base):
    __tablename__ = "loans"

    LoanID = Column(Integer, primary_key=True, index=True)
    UserID = Column(Integer, ForeignKey("users.UserID"), index=True)

    LenderName = Column(String, nullable=False)
    LoanType = Column(String, nullable=False)

    OutstandingAmount = Column(Float, nullable=False)
    InterestRate = Column(Float, nullable=False)
    EMI = Column(Float, nullable=False)
    OverdueMonths = Column(Integer, default=0)
# ==========================
# Settlement Prediction Table
# ==========================
class SettlementPrediction(Base):
    __tablename__ = "settlement_prediction"

    SettlementID = Column(Integer, primary_key=True, index=True)

    LoanID = Column(Integer, ForeignKey("loans.LoanID"))

    SuggestedSettlement = Column(String)
    RiskCategory = Column(String)
    PredictedAmount = Column(Float)


# ==========================
# AI Negotiation Table
# ==========================
class AINegotiation(Base):
    __tablename__ = "ai_negotiation"

    AI_ID = Column(Integer, primary_key=True, index=True)

    LoanID = Column(Integer, ForeignKey("loans.LoanID"))
    UserID = Column(Integer, ForeignKey("users.UserID"))

    NegotiationStrategy = Column(Text)
    NegotiationLetter = Column(Text)
    GeneratedDate = Column(String)


# ==========================
# AI History Table
# ==========================
class AIHistory(Base):
    __tablename__ = "ai_history"

    id = Column(Integer, primary_key=True, index=True)
    UserID = Column(Integer, ForeignKey("users.UserID"))
    LoanID = Column(Integer, ForeignKey("loans.LoanID"))
    response = Column(Text)