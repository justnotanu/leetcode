import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    
    cleaned_students = students.dropna(subset=['name'])
    return cleaned_students
  