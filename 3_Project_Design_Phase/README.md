
PROJECT DESIGN

Problem Solution Fit

The problem-solution fit maps each identified pain point of the borrower directly to a specific module implemented in FinRelief AI, confirming that the proposed solution genuinely addresses the problem defined during the ideation phase.

<img width="722" height="352" alt="image" src="https://github.com/user-attachments/assets/8494a6bf-1a36-4d57-b753-77b1577409c1" />

Proposed Solution

FinRelief AI is proposed as a full-stack web application with the following core modules, all of which are implemented in the project's backend and reflected in the frontend UI:

<img width="575" height="372" alt="image" src="https://github.com/user-attachments/assets/cb39cc76-42b3-44a7-a95b-e01ebe077d1e" />

Solution Architecture

FinRelief AI follows a classic three-tier web application architecture, cleanly separating presentation, business logic, and data persistence:

Tier 1 – Presentation Layer
Built with React.js and Vite, this layer renders all forms and views (registration, login, loan management, financial dashboard) and communicates with the backend exclusively through Axios-based HTTP calls to the FastAPI REST API.

Tier 2 – Application / Business Logic Layer
Implemented in FastAPI (main.py), this layer validates incoming requests using Pydantic schemas and delegates calculations to dedicated service modules: settlement_engine.py (settlement amount logic), risk_engine.py (risk scoring logic), and ai_engine.py (negotiation letter drafting, designed to be extended with live Google Gemini API calls).

Tier 3 – Data Layer
SQLAlchemy ORM models (models.py) define six tables — Users, FinancialProfile, Loans, SettlementPrediction, AINegotiation, and AIHistory — persisted in a SQLite database file (finrelief.db). All database access is routed through a single, reusable session dependency (get_db) defined in database.py.

<img width="441" height="383" alt="image" src="https://github.com/user-attachments/assets/5456aeaa-4d22-4de2-a816-4ef029fc5be0" />

Entitity diagram ER :

<img width="529" height="369" alt="image" src="https://github.com/user-attachments/assets/7d69b609-6d67-4ad2-92b8-2d427ddadd01" />

Architecture Diagram (textual representation)

<img width="497" height="265" alt="image" src="https://github.com/user-attachments/assets/b9819e21-81b8-4d16-af61-cd42eb0b98e1" />

<img width="391" height="382" alt="image" src="https://github.com/user-attachments/assets/babe72e8-76ff-4bfd-baa9-ce13af45776b" />

