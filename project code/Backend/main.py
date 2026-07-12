from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Base, User, FinancialProfile, Loan, SettlementPrediction, AINegotiation
from schemas import UserRegister, UserLogin, FinancialInput, LoanCreate, LoanUpdate, SettlementInput, SettlementResponse, NegotiationInput
from auth import hash_password, verify_password
from services.settlement_engine import calculate_settlement
from services.risk_engine import calculate_risk
from services.ai_engine import generate_negotiation_letter
from models import AIHistory

app = FastAPI(
    title="FinRelief AI",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/all-loans")
def get_all_loans(db: Session = Depends(get_db)):
    loans = db.query(Loan).all()

    return [
        {
            "LoanID": loan.LoanID,
            "UserID": loan.UserID,
            "LenderName": loan.LenderName,
            "LoanType": loan.LoanType,
            "OutstandingAmount": loan.OutstandingAmount,
            "InterestRate": loan.InterestRate,
            "EMI": loan.EMI,
            "OverdueMonths": loan.OverdueMonths
        }
        for loan in loans
    ]

@app.get("/")
def home():
    return {
        "message": "FinRelief AI Backend Running Successfully"
    }

@app.post("/create-test-loan")
def create_test_loan(db: Session = Depends(get_db)):
    loan = Loan(
        LoanID=1,
        UserID=1,
        LenderName="HDFC Bank",
        LoanType="Personal Loan",
        OutstandingAmount=50000,
        InterestRate=12.5,
        EMI=5000,
        OverdueMonths=8
    )

    db.add(loan)
    db.commit()

    return {"message": "Test loan created"}
# ==========================
# Register User
# ==========================
@app.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    # Check if email already exists
    existing_user = db.query(User).filter(User.Email == user.Email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash password
    hashed_password = hash_password(user.Password)

    # Create new user
    new_user = User(
        Name=user.Name,
        Email=user.Email,
        Password=hashed_password,
        MonthlyIncome=user.MonthlyIncome,
        MonthlyExpenses=user.MonthlyExpenses
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User Registered Successfully"
    }
# ==========================
# Login User
# ==========================
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.Email == user.Email).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid Email")

    if not verify_password(user.Password, db_user.Password):
        raise HTTPException(status_code=400, detail="Invalid Password")

    return {
        "message": "Login Successful",
        "UserID": db_user.UserID,
        "Name": db_user.Name
    }
@app.post("/financial-profile")
def financial_profile(data: FinancialInput, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.UserID == data.UserID).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    monthly_surplus = user.MonthlyIncome - user.MonthlyExpenses
    emi_ratio = (data.TotalEMI / user.MonthlyIncome) * 100
    dti_ratio = ((user.MonthlyExpenses + data.TotalEMI) / user.MonthlyIncome) * 100

    if dti_ratio < 35:
        stress = "Low"
    elif dti_ratio < 50:
        stress = "Medium"
    else:
        stress = "High"

    profile = FinancialProfile(
        UserID=user.UserID,
        EMI_Ratio=emi_ratio,
        DTI_Ratio=dti_ratio,
        MonthlySurplus=monthly_surplus,
        StressLevel=stress
    )

    db.add(profile)
    db.commit()

    return {
        "message": "Financial Profile Saved Successfully",
        "MonthlySurplus": monthly_surplus,
        "EMIRatio": round(emi_ratio, 2),
        "DTIRatio": round(dti_ratio, 2),
        "StressLevel": stress
    }
# ==========================
# Add Loan
# ==========================
@app.post("/add-loan")
def add_loan(loan: LoanCreate, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.UserID == loan.UserID).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_loan = Loan(
        UserID=loan.UserID,
        LenderName=loan.LenderName,
        LoanType=loan.LoanType,
        OutstandingAmount=loan.OutstandingAmount,
        InterestRate=loan.InterestRate,
        EMI=loan.EMI,
        OverdueMonths=loan.OverdueMonths
    )

    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)

    return {
        "message": "Loan Added Successfully",
        "LoanID": new_loan.LoanID
    }
@app.get("/loans/{user_id}")
def get_loans(user_id: int, db: Session = Depends(get_db)):

    loans = db.query(Loan).filter(Loan.UserID == user_id).all()

    return loans
@app.get("/financial-analysis/{user_id}")
def financial_analysis(user_id: int, db: Session = Depends(get_db)):

    # Get user
    user = db.query(User).filter(User.UserID == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Get all loans
    loans = db.query(Loan).filter(Loan.UserID == user_id).all()

    total_emi = sum(loan.EMI for loan in loans)

    monthly_surplus = user.MonthlyIncome - user.MonthlyExpenses

    dti_ratio = (
        (total_emi / user.MonthlyIncome) * 100
        if user.MonthlyIncome > 0 else 0
    )

    emi_ratio = dti_ratio

    if dti_ratio < 30:
        stress = "Low"
    elif dti_ratio < 50:
        stress = "Medium"
    else:
        stress = "High"

    return {
        "MonthlyIncome": user.MonthlyIncome,
        "MonthlyExpenses": user.MonthlyExpenses,
        "TotalEMI": total_emi,
        "MonthlySurplus": monthly_surplus,
        "DTIRatio": round(dti_ratio, 2),
        "EMIRatio": round(emi_ratio, 2),
        "StressLevel": stress
    }

@app.get("/view-loans/{user_id}")
def view_loans(user_id: int, db: Session = Depends(get_db)):

    loans = db.query(Loan).filter(Loan.UserID == user_id).all()

    if not loans:
        raise HTTPException(status_code=404, detail="No loans found")

    return loans
@app.delete("/delete-loan/{loan_id}")
def delete_loan(
    loan_id: int = Path(...),
    db: Session = Depends(get_db)
):
    loan = db.query(Loan).filter(Loan.LoanID == loan_id).first()

    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")

    db.delete(loan)
    db.commit()

    return {
        "message": "Loan deleted successfully"
    }
# ==========================
# Update Loan
# ==========================
@app.put("/update-loan/{loan_id}")
def update_loan(loan_id: int, loan: LoanUpdate, db: Session = Depends(get_db)):

    db_loan = db.query(Loan).filter(Loan.LoanID == loan_id).first()

    if not db_loan:
        raise HTTPException(status_code=404, detail="Loan not found")

    db_loan.LenderName = loan.LenderName
    db_loan.LoanType = loan.LoanType
    db_loan.OutstandingAmount = loan.OutstandingAmount
    db_loan.InterestRate = loan.InterestRate
    db_loan.EMI = loan.EMI
    db_loan.OverdueMonths = loan.OverdueMonths

    db.commit()
    db.refresh(db_loan)

    return {
        "message": "Loan Updated Successfully"
    }
@app.post("/predict_settlement")
def predict_settlement(
    data: SettlementInput,
    db: Session = Depends(get_db)
):

    loan = db.query(Loan).filter(
        Loan.LoanID == data.LoanID
    ).first()

    if not loan:
        raise HTTPException(
            status_code=404,
            detail="Loan not found"
        )

    if loan.OverdueMonths >= 6:
        settlement = loan.OutstandingAmount * 0.7
    else:
        settlement = loan.OutstandingAmount

    return {
        "LoanID": loan.LoanID,
        "SettlementAmount": settlement
    }
@app.get("/ai-history/{user_id}")
def get_ai_history(user_id: int, db: Session = Depends(get_db)):

    history = db.query(AINegotiation).filter(
        AINegotiation.UserID == user_id
    ).all()

    if not history:
        raise HTTPException(status_code=404, detail="No AI history found")

    return history
@app.post("/generate-letter")
def generate_letter(data: SettlementInput, db: Session = Depends(get_db)):

    loan = db.query(Loan).filter(Loan.LoanID == data.LoanID).first()

    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")

    user = db.query(User).filter(User.UserID == loan.UserID).first()

    settlement = calculate_settlement(
        loan.OutstandingAmount,
        loan.OverdueMonths,
        loan.InterestRate,
        user.MonthlyIncome,
        user.MonthlyExpenses
    )

    letter = generate_negotiation_letter(user, loan, settlement)

    history = AIHistory(
        UserID=user.UserID,
        LoanID=loan.LoanID,
        response=letter
    )

    db.add(history)
    db.commit()

    return {
        "letter": letter
    }