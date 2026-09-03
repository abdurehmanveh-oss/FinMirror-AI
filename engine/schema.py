from dataclasses import dataclass
from typing import List


@dataclass
class FinancialData:
    income: float
    fixed_expenses: float
    variable_expenses: float
    current_savings: float
    savings_goal: float
    goal_deadline_months: int


@dataclass
class Scenario:
    income_change_percent: float
    expense_change_percent: float
    months: int


@dataclass
class SimulationResult:
    current_savings: float
    monthly_cashflow: float
    projected_balance: float
    scenario_description: str
    risk_flags: List[str]