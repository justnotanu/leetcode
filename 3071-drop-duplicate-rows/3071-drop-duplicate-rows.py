import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # Remove duplicates based on the 'email' column, keeping the first occurrence
    customers_unique = customers.drop_duplicates(subset='email', keep='first')
    
    return customers_unique
 