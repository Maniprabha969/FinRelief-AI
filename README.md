# FinRelief AI
# FinRelief AI

## Overview

FinRelief AI is an AI-powered financial relief and debt settlement platform designed to help users manage their loans, analyze their financial condition, predict settlement opportunities, and generate professional negotiation letters for lenders.

The application combines financial analytics with artificial intelligence to support individuals facing financial difficulties and simplify the debt settlement process.

---

## Problem Statement

Many borrowers struggle to manage multiple loans and negotiate settlements with financial institutions. Traditional processes are often complex, time-consuming, and lack personalized guidance.

FinRelief AI addresses this problem by providing:

- Centralized loan management
- Financial profile analysis
- Settlement recommendations
- AI-generated negotiation assistance

---

## Features

### User Management
- User Registration
- Secure User Login
- Password Protection

### Financial Profile Analysis
- Monthly Income Tracking
- Monthly Expense Tracking
- Financial Health Evaluation

### Loan Management
- Add Loan Details
- View Existing Loans
- Update Loan Information
- Delete Loans

### Settlement Prediction Engine
- Analyze overdue loans
- Evaluate outstanding amounts
- Predict possible settlement values
- Provide financial recommendations

### AI Negotiation Letter Generator
- Automatically generate professional settlement request letters
- Customize lender communication
- Reduce manual effort during negotiation

---

## Technology Stack

### Frontend
- React.js
- Vite
- Axios
- React Router DOM

### Backend
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

### Database
- SQLite

### Artificial Intelligence
- Google Gemini API

---

## Project Architecture

```
Frontend (React + Vite)
            │
            ▼
Backend APIs (FastAPI)
            │
            ▼
Database (SQLite)
            │
            ▼
AI Services (Google Gemini API)
```

---

## Project Structure

```
FinRelief-AI/
│
├── Backend/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── auth.py
│   ├── requirements.txt
│   ├── ai_service.py
│   └── gemini_service.py
│
├── Frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   └── ...
│
└── README.md
```

---



## API Endpoints

### Authentication
- POST `/register`
- POST `/login`

### Loan Management
- POST `/add-loan`
- GET `/all-loans`
- PUT `/update-loan/{loan_id}`
- DELETE `/delete-loan/{loan_id}`

### Financial Intelligence
- POST `/predict-settlement`
- POST `/generate-letter`

---

## Sample Workflow

1. Register a new user account.
2. Login to the application.
3. Add financial details and loans.
4. View and manage loans.
5. Predict settlement opportunities.
6. Generate AI negotiation letters.
7. Use recommendations to negotiate with lenders.

---

## Future Enhancements

- JWT Authentication
- Email Notifications
- Multiple Loan Optimization
- Credit Score Analysis
- Advanced Machine Learning Models
- Cloud Database Support
- PDF Export for Negotiation Letters

---

## License

This project was developed for educational and academic purposes.

### Backend Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the backend server:

```bash
uvicorn main:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---
<img width="940" height="460" alt="Screenshot 2026-07-12 091434" src="https://github.com/user-attachments/assets/1c0e908d-ce27-4c26-a05c-b63784e05ae5" />


<img width="944" height="457" alt="Screenshot 2026-07-12 091447" src="https://github.com/user-attachments/assets/431cc856-e31e-44a6-b679-fe87eaa62ca7" />


<img width="946" height="437" alt="Screenshot 2026-07-11 223705" src="https://github.com/user-attachments/assets/d103e4ce-461e-4b82-a98f-3a2662e6d525" />

### Frontend Setup

Install dependencies:

```bash
npm install
```

Start the frontend server:

```bash
npm run dev
```

Frontend URL:

```
http://localhost:5173
```

---
<img width="957" height="459" alt="Screenshot 2026-07-11 223855" src="https://github.com/user-attachments/assets/c32167a5-5dd7-464e-977b-7ae8ecf1b547" />

<img width="950" height="338" alt="Screenshot 2026-07-11 223945" src="https://github.com/user-attachments/assets/d3e58d6b-0a1c-43c6-bec9-87d6d8c2f1fe" />

<img width="853" height="437" alt="Screenshot 2026-07-11 224006" src="https://github.com/user-attachments/assets/4f70bf7c-1a4a-4de4-a929-39cc2d44a976" />

<img width="820" height="389" alt="Screenshot 2026-07-11 224019" src="https://github.com/user-attachments/assets/7ba19e6e-9def-44eb-b10d-f44f26f9ee83" />

<img width="539" height="318" alt="Screenshot 2026-07-11 224036" src="https://github.com/user-attachments/assets/96b7315e-cc8a-41ba-8e14-2fd283dc68db" />


Project Demo video:

https://drive.google.com/file/d/1pZGBPrGA_C1WcX-Dsj3DaMkPxcyW13TT/view?usp=sharing

