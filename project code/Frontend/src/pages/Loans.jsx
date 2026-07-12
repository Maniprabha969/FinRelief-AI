import { useEffect, useState } from "react";
import API from "../api/axios";

function Loans() {
  const [loans, setLoans] = useState([]);

  useEffect(() => {
    fetchLoans();
  }, []);

  const fetchLoans = async () => {
    try {
      const response = await API.get("/all-loans");
      setLoans(response.data);
    } catch (error) {
      console.error(error);
      alert("Failed to fetch loans");
    }
  };

  const editLoan = async (loan) => {
    const newEMI = prompt(
      "Enter new EMI:",
      loan.EMI
    );

    if (newEMI === null) {
      return;
    }

    try {
      await API.put(`/update-loan/${loan.LoanID}`, {
        LenderName: loan.LenderName,
        LoanType: loan.LoanType,
        OutstandingAmount: loan.OutstandingAmount,
        InterestRate: loan.InterestRate,
        EMI: parseFloat(newEMI),
        OverdueMonths: loan.OverdueMonths
      });

      alert("Loan updated successfully");

      fetchLoans();

    } catch (error) {
      console.error(error);
      alert("Failed to update loan");
    }
  };

  const deleteLoan = async (loanId) => {
    try {
      await API.delete(`/delete-loan/${loanId}`);

      alert("Loan deleted successfully");

      fetchLoans();

    } catch (error) {
      console.error(error);
      alert("Failed to delete loan");
    }
  };

  return (
    <div>
      <h1>All Loans</h1>

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>Loan ID</th>
            <th>Lender</th>
            <th>Loan Type</th>
            <th>Outstanding Amount</th>
            <th>Interest Rate</th>
            <th>EMI</th>
            <th>Overdue Months</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {loans.map((loan) => (
            <tr key={loan.LoanID}>
              <td>{loan.LoanID}</td>
              <td>{loan.LenderName}</td>
              <td>{loan.LoanType}</td>
              <td>₹{loan.OutstandingAmount}</td>
              <td>{loan.InterestRate}%</td>
              <td>₹{loan.EMI}</td>
              <td>{loan.OverdueMonths}</td>

              <td>
                <button onClick={() => editLoan(loan)}>
                  Edit
                </button>

                <button onClick={() => deleteLoan(loan.LoanID)}>
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Loans;