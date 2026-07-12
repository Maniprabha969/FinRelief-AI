import { useNavigate } from "react-router-dom";

function Dashboard() {
  return (
    <div>
      <h1>FinRelief AI Dashboard</h1>

      <h3>Available Features</h3>

      <ul>
        <li>View Loans</li>
        <li>Add Loan</li>
        <li>Settlement Prediction</li>
        <li>AI Negotiation Letter</li>
      </ul>

      <p>
        Select an option from the navigation buttons above.
      </p>
    </div>
  );
}

export default Dashboard;