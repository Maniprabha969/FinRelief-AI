from dotenv import load_dotenv

load_dotenv()


def generate_negotiation_letter(user, loan, settlement):

    letter = f"""
LOAN SETTLEMENT NEGOTIATION REQUEST LETTER

Date: __________


To,
The Loan Settlement Department

Subject: Request for Loan Settlement Consideration


Dear Sir/Madam,

I am writing this letter to request your consideration for a settlement
arrangement regarding my outstanding loan account.

Customer Details:
Name: {user.Name}

Financial Situation:
Monthly Income: {user.MonthlyIncome}
Monthly Expenses: {user.MonthlyExpenses}


Loan Details:
Outstanding Amount: {loan.OutstandingAmount}
Interest Rate: {loan.InterestRate}%
Overdue Months: {loan.OverdueMonths}


Based on my current financial circumstances, I would like to propose a
settlement amount of {settlement['settlement_amount']}.

This settlement proposal represents approximately
{settlement['settlement_percent']}% of the outstanding amount.

I kindly request your consideration and approval of this settlement
proposal. I believe this will help both parties reach a mutually beneficial
resolution.

Thank you for your understanding and support.


Sincerely,

{user.Name}
"""

    return letter