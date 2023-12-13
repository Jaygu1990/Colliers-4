import os
import pandas as pd
from vendor.models import AXvendor

def process_excel_file(file_path):
    try:
        # Clear existing data in AXvendor model
        AXvendor.objects.all().delete()

        # Read data from Excel file into a DataFrame
        df = pd.read_excel(file_path)
        print(df)
        # Iterate through DataFrame rows and create AXvendor objects
        for index, row in df.iterrows():
            AXvendor.objects.create(
                vendor_name = row[0],
                vendor_code = row[1],
                vendor_address = row[2],
                vendor_type = row[3],
            )
        os.remove(file_path)
        return True, 'Data imported successfully'

    except Exception as e:
        # Handle errors during the import process
        error_message = f"Error importing data from Excel file: {str(e)}"
        return False, error_message
