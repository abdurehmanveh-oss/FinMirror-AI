def run_simulation(current_savings, monthly_cashflow, income_change_percent, expense_change_percent, months):
    # Scenario ke hisaab se income aur expense adjust karo
    adjusted_cashflow = monthly_cashflow * (1 + (income_change_percent - expense_change_percent) / 100)

    projected_balances = []
    balance = current_savings

    for month in range(1, months + 1):
        balance += adjusted_cashflow
        projected_balances.append(round(balance, 2))

    return projected_balances


def check_risk_flags(projected_balances):
    flags = []
    if any(b < 0 for b in projected_balances):
        flags.append("balance_going_negative")
    if projected_balances[-1] < projected_balances[0]:
        flags.append("declining_trend")
    return flags
if __name__ == "__main__":
    balances = run_simulation(
        current_savings=150000,
        monthly_cashflow=20000,
        income_change_percent=-20,
        expense_change_percent=0,
        months=12
    )
    print("Projected Balances:", balances)
    print("Risk Flags:", check_risk_flags(balances))