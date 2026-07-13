
Development Phase
Overview

The development phase of FinRelief AI focused on building a scalable, modular, and intelligent debt management platform capable of assisting borrowers throughout the financial recovery process. The application was developed using a full-stack architecture consisting of a React.js frontend, FastAPI backend services, SQLite database management, and Google Gemini AI integration.

The system was developed incrementally by implementing backend APIs, integrating database operations, connecting frontend interfaces, and enabling AI-powered financial assistance functionalities.

Backend Development

The backend was developed using FastAPI, which provided high-performance RESTful APIs for authentication, financial processing, loan management, and AI integration.

Technologies Used
FastAPI
SQLAlchemy ORM
SQLite Database
Pydantic Data Validation
Uvicorn ASGI Server
Core Backend Modules
Authentication Module

The authentication module manages borrower registration and login functionality. Passwords are securely processed and user credentials are validated before granting access to the platform.

Implemented APIs:

User Registration
User Login
Loan Management Module

The loan management module allows borrowers to digitally maintain all their loan information in a centralized system.

Implemented functionalities include:

Add new loan accounts
View existing loans
Update loan information
Delete loan records
Track overdue status and outstanding balances
Financial Processing Module

The financial engine performs borrower financial analysis by evaluating income, expenses, EMI commitments, and debt burden indicators.

The module calculates:

Monthly surplus amount
EMI ratio
Debt-to-income ratio
Financial stress indicators

These calculations assist in generating personalized recommendations for financial recovery.

Settlement Prediction Engine

The settlement prediction engine analyzes loan information and borrower financial conditions to estimate suitable settlement amounts and recovery strategies.

The prediction process considers:

Outstanding loan amount
Interest rate
Monthly EMI
Overdue duration
Borrower repayment capability

The generated recommendations help borrowers understand realistic settlement opportunities.

AI Negotiation Module

The AI negotiation module integrates Google Gemini AI to automate lender communication and settlement discussions.

The module generates:

Personalized negotiation strategies
Professional settlement request letters
Borrower-specific financial guidance

This significantly reduces manual effort during debt negotiation processes.

Frontend Development

The frontend application was developed using React.js and Vite to provide a fast, responsive, and user-friendly interface for borrowers.

Technologies Used
React.js
Vite
Axios
React Router DOM
Developed Components

The following user interface modules were implemented:

Registration Page

Allows new borrowers to create accounts by entering personal and financial information.

Login Page

Provides secure authentication and access to platform services.

Loan Management Interface

Enables borrowers to add, update, view, and remove loan information through an intuitive interface.

Settlement Prediction Interface

Allows users to request AI-assisted settlement recommendations for selected loans.

Negotiation Letter Interface

Generates lender-specific negotiation letters and settlement requests using AI capabilities.

API Integration

The frontend communicates with backend services through REST APIs using Axios.

The API integration layer handles:

User authentication requests
Loan management operations
Settlement prediction requests
AI letter generation services
Data retrieval and synchronization
AI Integration

Google Gemini AI was integrated into FinRelief AI to provide intelligent financial assistance and automate debt negotiation workflows.

The AI services are responsible for:

Generating personalized negotiation strategies.
Producing professional settlement request letters.
Providing borrower-specific financial recommendations.
Assisting users in making informed debt recovery decisions.
Database Integration

SQLite and SQLAlchemy ORM were used for persistent storage and management of borrower information and financial records.

The database stores:

User information
Financial profiles
Loan records
Settlement recommendations
AI-generated negotiation history

The ORM layer ensures efficient communication between application services and database tables while maintaining data consistency and integrity.
