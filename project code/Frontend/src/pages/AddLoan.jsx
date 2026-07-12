import { useState } from "react";
import API from "../api/axios";

function AddLoan() {
  const [formData, setFormData] = useState({
    UserID: 1,
    LenderName: "",
    LoanType: "",
    OutstandingAmount: "",
    InterestRate: "",
    EMI: "",
    OverdueMonths: ""
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const addLoan = async () => {
    try {
      const response = await API.post("/add-loan", {
        UserID: parseInt(formData.UserID),
        LenderName: formData.LenderName,
        LoanType: formData.LoanType,
        OutstandingAmount: parseFloat(formData.OutstandingAmount),
        InterestRate: parseFloat(formData.InterestRate),
        EMI: parseFloat(formData.EMI),
        OverdueMonths: parseInt(formData.OverdueMonths)
      });

      alert("Loan Added Successfully");
      console.log(response.data);

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
      <h1>Add Loan</h1>

      <input
        name="LenderName"
        placeholder="Lender Name"
        onChange={handleChange}
      />

      <br /><br />

      <input
        name="LoanType"
        placeholder="Loan Type"
        onChange={handleChange}
      />

      <br /><br />

      <input
        name="OutstandingAmount"
        type="number"
        placeholder="Outstanding Amount"
        onChange={handleChange}
      />

      <br /><br />

      <input
        name="InterestRate"
        type="number"
        placeholder="Interest Rate"
        onChange={handleChange}
      />

      <br /><br />

      <input
        name="EMI"
        type="number"
        placeholder="Monthly EMI"
        onChange={handleChange}
      />

      <br /><br />

      <input
        name="OverdueMonths"
        type="number"
        placeholder="Overdue Months"
        onChange={handleChange}
      />

      <br /><br />

      <button onClick={addLoan}>
        Add Loan
      </button>
    </div>
  );
}

export default AddLoan;