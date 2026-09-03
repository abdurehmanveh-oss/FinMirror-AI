import pandas as pd
import random

def generate_sample_data(num_users=12):
    data = []
    for user_id in range(1, num_users + 1):
        income = random.randint(40000, 150000)
        fixed_expenses = round(income * random.uniform(0.25, 0.4))
        variable_expenses = round(income * random.uniform(0.1, 0.25))
        current_savings = random.randint(20000, 300000)
        savings_goal = current_savings + random.randint(50000, 200000)
        goal_deadline_months = random.choice([6, 12, 18, 24])

        data.append({
            "user_id": user_id,
            "income": income,
            "fixed_expenses": fixed_expenses,
            "variable_expenses": variable_expenses,
            "current_savings": current_savings,
            "savings_goal": savings_goal,
            "goal_deadline_months": goal_deadline_months
        })

    return pd.DataFrame(data)


if __name__ == "__main__":
    df = generate_sample_data()
    df.to_csv("data/datasets/sample_users.csv", index=False)
    print("Sample dataset created: data/datasets/sample_users.csv")
    print(df)