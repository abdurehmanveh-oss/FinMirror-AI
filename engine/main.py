import json
from calculations import calculate_monthly_cashflow, calculate_months_to_goal
from simulation import run_simulation, check_risk_flags


def generate_financial_twin_output(financial_data, scenario):
    # Step 1: Current state nikalo
    monthly_cashflow = calculate_monthly_cashflow(
        financial_data["income"],
        financial_data["fixed_expenses"],
        financial_data["variable_expenses"]
    )

    # Step 2: Simulation chalao
    projected_balances = run_simulation(
        current_savings=financial_data["current_savings"],
        monthly_cashflow=monthly_cashflow,
        income_change_percent=scenario["income_change_percent"],
        expense_change_percent=scenario["expense_change_percent"],
        months=scenario["months"]
    )

    # Step 3: Risk flags nikalo
    risk_flags = check_risk_flags(projected_balances)

    # Step 4: Final JSON banao
    result = {
        "current_balance": financial_data["current_savings"],
        "monthly_cashflow": monthly_cashflow,
        "scenario": scenario,
        "projected_balances": projected_balances,
        "risk_flags": risk_flags
    }

    return result


if __name__ == "__main__":
    sample_user = {
        "income": 100000,
        "fixed_expenses": 35000,
        "variable_expenses": 20000,
        "current_savings": 150000,
        "savings_goal": 300000,
        "goal_deadline_months": 12
    }

    sample_scenario = {
        "income_change_percent": -20,
        "expense_change_percent": 0,
        "months": 12
    }

    output = generate_financial_twin_output(sample_user, sample_scenario)
    print(json.dumps(output, indent=2)) 