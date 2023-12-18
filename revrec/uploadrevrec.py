import os
import pandas as pd
from revrec.models import revrecmodel

def process_excel_file(file_path):
    try:
        df = pd.read_excel(file_path)

        for index, row in df.iterrows():
            revrecmodel.objects.create(
                name = row[0],
                deal = row[1],
                due_date = row[2],
            )
        os.remove(file_path)
        return True, 'Data imported successfully'

    except Exception as e:
        # Handle errors during the import process
        error_message = f"Error importing data from Excel file: {str(e)}"
        return False, error_message