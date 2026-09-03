import json
from pathlib import Path
import pandas as pd
from calculations import calculate_monthly_cashflow, calculate_months_to_goal
from simulation import run_simulation, check_risk_flags


def generate_financial_twin_output(financial_data, scenario):
    monthly_cashflow = calculate_monthly_cashflow(
        financial_data["income"],
        financial_data["fixed_expenses"],
        financial_data["variable_expenses"]
    )

    projected_balances = run_simulation(
        current_savings=financial_data["current_savings"],
        monthly_cashflow=monthly_cashflow,
        income_change_percent=scenario["income_change_percent"],
        expense_change_percent=scenario["expense_change_percent"],
        months=scenario["months"]
    )

    risk_flags = check_risk_flags(projected_balances)

    result = {
        "user_id": financial_data["user_id"],
        "current_balance": financial_data["current_savings"],
        "monthly_cashflow": monthly_cashflow,
        "scenario": scenario,
        "projected_balances": projected_balances,
        "risk_flags": risk_flags
    }

    return result


if __name__ == "__main__":
    # Is file (main.py) ki apni location se path banao — cwd pe depend nahi karega
    BASE_DIR = Path(__file__).resolve().parent.parent
    csv_path = BASE_DIR / "data" / "datasets" / "sample_users.csv"

    df = pd.read_csv(csv_path)

    user_row = df[df["user_id"] == 1].iloc[0]
    sample_user = user_row.to_dict()

    sample_scenario = {
        "income_change_percent": -20,
        "expense_change_percent": 0,
        "months": 12
    }

    output = generate_financial_twin_output(sample_user, sample_scenario)
    print(json.dumps(output, indent=2, default=str))