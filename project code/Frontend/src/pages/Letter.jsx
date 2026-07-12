import { useState } from "react";
import API from "../api/axios";

function Letter() {
  const [loanId, setLoanId] = useState("");
  const [letter, setLetter] = useState("");

  const generateLetter = async () => {
    try {
      const response = await API.post("/generate-letter", {
        LoanID: parseInt(loanId)
      });

      setLetter(response.data.letter);

    } catch (error) {
      console.error(error);

      if (error.response) {
        alert(error.response.data.detail);
      } else {
        alert("Could not connect to backend");
      }
    }
  };

  return (
    <div>
      <h1>AI Negotiation Letter</h1>

      <input
        type="number"
        placeholder="Enter Loan ID"
        value={loanId}
        onChange={(e) => setLoanId(e.target.value)}
      />

      <br /><br />

      <button onClick={generateLetter}>
        Generate Letter
      </button>

      {letter && (
        <div
          style={{
            marginTop: "20px",
            padding: "20px",
            border: "1px solid #ccc",
            borderRadius: "10px"
          }}
        >
          <h2>Generated Letter</h2>

          <pre
            style={{
              whiteSpace: "pre-wrap"
            }}
          >
            {letter}
          </pre>
        </div>
      )}
    </div>
  );
}

export default Letter;