"""
Small shared helper functions for the engine package.
Add reusable utilities here as the project grows.
"""

def round_currency(value, decimals=2):
    """Round a monetary value consistently across the engine."""
    return round(value, decimals)