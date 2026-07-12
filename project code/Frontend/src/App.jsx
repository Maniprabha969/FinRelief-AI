import { useState } from "react";
import Dashboard from "./pages/Dashboard";
import Loans from "./pages/Loans";
import AddLoan from "./pages/AddLoan";
import Settlement from "./pages/Settlement";
import Letter from "./pages/Letter";

function App() {
  const [page, setPage] = useState("dashboard");

  return (
    <div style={{ padding: "20px" }}>
      <h1>FinRelief AI</h1>

      <div style={{ marginBottom: "20px" }}>
        <button onClick={() => setPage("dashboard")}>
          Dashboard
        </button>

        {" "}

        <button onClick={() => setPage("loans")}>
          View Loans
        </button>

        {" "}

        <button onClick={() => setPage("addloan")}>
          Add Loan
        </button>

        {" "}

        <button onClick={() => setPage("settlement")}>
          Settlement Prediction
        </button>

        {" "}

        <button onClick={() => setPage("letter")}>
          AI Letter
        </button>
      </div>

      <hr />

      {page === "dashboard" && <Dashboard />}
      {page === "loans" && <Loans />}
      {page === "addloan" && <AddLoan />}
      {page === "settlement" && <Settlement />}
      {page === "letter" && <Letter />}
    </div>
  );
}

export default App;