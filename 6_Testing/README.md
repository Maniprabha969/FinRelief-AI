FUNCTIONAL AND PERFORMANCE TESTING

Performance Testing

Each module of FinRelief AI was tested manually against its corresponding API endpoint using tools such as the FastAPI interactive Swagger UI (/docs) and the React frontend, to verify both functional correctness and response performance under normal local development conditions.

<img width="330" height="396" alt="image" src="https://github.com/user-attachments/assets/d7d18e5c-db66-4bd0-b958-ad52fb339169" />

6.1.2	Performance Observations

As FinRelief AI was tested in a local development environment (Uvicorn development server with SQLite), the following response-time observations are indicative rather than production benchmarks, but they demonstrate that the system performs comfortably for its intended single-user, low-concurrency use case:
The Registration/Login module responds quickly because it performs only a single password hashing or verification operation using bcrypt, followed by an indexed database lookup based on the user's email address. This minimizes authentication time while ensuring secure password handling.
The Loan Management module, which includes adding, viewing, updating, and deleting loan records, also exhibits fast response times. These operations involve straightforward SQLite CRUD queries on a single table without complex joins or nested transactions, resulting in efficient execution.
The Financial Profile and Analysis module performs lightweight arithmetic calculations on data already retrieved from the database. Since most computations are executed in memory, the module generates analytical results with minimal processing delay, providing users with near-instant financial insights.

<img width="676" height="384" alt="image" src="https://github.com/user-attachments/assets/db2644aa-f5c4-44dc-b201-0a3d48f683bf" />
