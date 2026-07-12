def calculate_risk(overdue_months, interest_rate, outstanding, income):

    risk_score = 0

    if overdue_months > 12:
        risk_score += 40
    elif overdue_months > 6:
        risk_score += 25
    elif overdue_months > 3:
        risk_score += 15

    if interest_rate > 18:
        risk_score += 20

    if outstanding > income * 5:
        risk_score += 25

    risk_score = min(100, risk_score)

    if risk_score >= 70:
        level = "HIGH"
    elif risk_score >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "risk_score": risk_score,
        "risk_level": level
    }