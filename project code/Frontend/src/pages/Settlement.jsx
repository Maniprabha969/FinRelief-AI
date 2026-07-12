import { useState } from "react";
import API from "../api/axios";

function Settlement() {
  const [loanId, setLoanId] = useState("");
  const [result, setResult] = useState(null);

  const predictSettlement = async () => {
    try {
      const response = await API.post("/predict_settlement", {
        LoanID: parseInt(loanId)
      });

      setResult(response.data);
    } catch (error) {
      console.log(error);
      console.log(error.response);
      console.log(error.message);

      alert(error.message);
    }
  };

  return (
    <div>
      <h1>Settlement Prediction</h1>

      <input
        type="number"
        placeholder="Enter Loan ID"
        value={loanId}
        onChange={(e) => setLoanId(e.target.value)}
      />

      <br /><br />

      <button onClick={predictSettlement}>
        Predict Settlement
      </button>

      {result && (
  <div style={{
    marginTop: "20px",
    padding: "20px",
    border: "1px solid #ccc",
    borderRadius: "10px"
  }}>
    <h2>Settlement Prediction Result</h2>

    <p>
      <strong>Loan ID:</strong> {result.LoanID}
    </p>

    <p>
      <strong>Recommended Settlement Amount:</strong>
      ₹{result.SettlementAmount}
    </p>
  </div>
)}
    </div>
  );
}

export default Settlement;