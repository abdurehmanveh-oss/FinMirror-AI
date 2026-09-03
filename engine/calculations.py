def calculate_monthly_cashflow(income, fixed_expenses, variable_expenses):
    return income - (fixed_expenses + variable_expenses)


def calculate_months_to_goal(current_savings, savings_goal, monthly_cashflow):
    if monthly_cashflow <= 0:
        return None  # goal never reached at this rate
    remaining = savings_goal - current_savings
    months_needed = remaining / monthly_cashflow
    return round(months_needed, 1)
if __name__ == "__main__":
    cashflow = calculate_monthly_cashflow(100000, 35000, 20000)
    print("Monthly Cashflow:", cashflow)
    print("Months to Goal:", calculate_months_to_goal(150000, 300000, cashflow))