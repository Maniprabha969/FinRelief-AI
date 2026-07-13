PROJECT OVERVIEW:
FinRelief AI is an AI-assisted web application designed to help individual borrowers understand, organise, and manage their personal debt in one place. Many people today juggle multiple loans — personal loans, credit cards, vehicle loans — across different lenders, and rarely have a single, simple view of how much they owe, how overdue they are, and how those loans affect their monthly finances. FinRelief AI addresses this gap by combining a loan management system with a rule-based financial analysis engine and an AI-assisted negotiation letter generator.
The platform is built as a three-tier web application. The frontend, developed using React.js and Vite, provides the user interface through which a borrower registers, logs in, and manages their loan and financial information. The backend, built using FastAPI (Python), exposes a REST API that performs all the business logic — user authentication, financial ratio calculations, loan record management, settlement prediction, and negotiation letter generation. Data is persisted using SQLite through the SQLAlchemy ORM, and the Google Gemini API is included in the technology stack to support AI-assisted natural language generation for the negotiation letters.
At its core, the system takes basic financial inputs from the user — monthly income, monthly expenses, and details of each loan (lender, loan type, outstanding amount, interest rate, EMI, and overdue months) — and converts them into meaningful, actionable insight: a debt-to-income (DTI) ratio, an EMI ratio, a financial stress classification, a suggested settlement percentage, and a ready-to-send settlement negotiation letter addressed to the lender.
PURPOSEP
The purpose of building FinRelief AI is to give an ordinary borrower — someone without financial or legal expertise — the tools to understand their debt situation and take the first step toward resolving it, without needing to hire a financial consultant. Specifically, the project aims to:
●	Provide a single, centralised place where a user can record and track every loan they hold, instead of relying on scattered paper statements or memory.
●	Automatically calculate key financial health indicators — EMI ratio, debt-to-income (DTI) ratio, and monthly surplus — so that users can objectively see how stressed their finances are.
●	Classify a user's financial stress level (Low / Medium / High) using clear, rule-based
thresholds, so that the feedback is transparent and explainable rather than a hidden “black box” score.
●	Estimate a realistic loan settlement amount by factoring in how overdue a loan is, its interest rate, and the borrower's disposable income, giving the user a data-informed starting point before they approach a lender.
●	Automatically draft a formally worded settlement negotiation letter using the calculated settlement figures, saving the user the time and difficulty of writing one from scratch.

  2.	IDEATION PHASE
	Problem Statement
The problem addressed by this project can be framed using a standard problem-statement template, connecting the affected user, their need, and the reason behind that need:
<img width="479" height="185" alt="image" src="https://github.com/user-attachments/assets/e0e2b343-1a2c-4a76-b209-5668b66cca11" />
In simple terms: borrowers with multiple, overdue loans lack an easy way to (a) see their complete debt picture, (b) assess how serious their situation is, and (c) begin a structured negotiation with their lender. FinRelief AI is designed to solve exactly this problem using a web-based, self-service platform.

Empathy Map Canvas
An empathy map was used during the ideation phase to better understand the target user — a borrower struggling to manage multiple overdue loans.
<img width="479" height="296" alt="image" src="https://github.com/user-attachments/assets/b331aafa-fdc3-4099-884d-54c28c3f04cc" />

<img width="473" height="301" alt="image" src="https://github.com/user-attachments/assets/5f5a2912-d1e5-43b2-8a28-BRAINSTROMING
  Based on the empathy map, the team brainstormed a wide range of possible features before narrowing down to what could realistically be implemented within the internship timeline. Ideas were grouped using the MoSCoW prioritisation technique (Must have, Should have, Could have, Won't have
— for this version).
<img width="467" height="150" alt="image" src="https://github.com/user-attachments/assets/2877c2c4-4f2e-4df9-89d1-49344832af84" />
The features marked “Must Have” directly map to the modules that were finally implemented in the FinRelief AI backend and frontend: user registration/login, loan CRUD operations, financial profile analysis, settlement prediction, and AI negotiation letter generation — as reflected in the project's REST API and database schema.
