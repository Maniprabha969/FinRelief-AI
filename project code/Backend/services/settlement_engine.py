def calculate_settlement(outstanding, overdue_months, interest_rate, income, expenses):

    disposable_income = income - expenses

    settlement_percent = 70

    if overdue_months >= 12:
        settlement_percent -= 25
    elif overdue_months >= 6:
        settlement_percent -= 15
    elif overdue_months >= 3:
        settlement_percent -= 8

    if interest_rate > 15:
        settlement_percent -= 5

    if disposable_income < 5000:
        settlement_percent -= 10

    settlement_percent = max(30, min(settlement_percent, 90))

    settlement_amount = (settlement_percent / 100) * outstanding

    return {
        "settlement_percent": settlement_percent,
        "settlement_amount": round(settlement_amount, 2),
        "risk_level": "HIGH" if settlement_percent < 50 else "MEDIUM"
    }