import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    if 'salary' not in employees.columns:
        raise ValueError("The DataFrame must contain a 'salary' column.")
    
    # Create the bonus column by doubling the salary
    employees['bonus'] = employees['salary'] * 2
    
    return employees
       