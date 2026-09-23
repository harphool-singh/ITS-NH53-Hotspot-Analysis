import pandas as pd

# Load the Excel file
file_path = r"C:\Users\harph\OneDrive\Desktop\ITS\New folder\NH-53 Accident.xlsx"
xls = pd.ExcelFile(file_path)

# Check the sheet names
print(xls.sheet_names)

# Load the 2020 sheet
df_2020 = pd.read_excel(file_path, sheet_name='2020')  # Assuming the sheet is named '2020'

# Optional: reset index and remove empty rows/columns if needed
df_2020 = df_2020.dropna(how='all')

# Save to CSV
output_csv = r"C:\Users\harph\OneDrive\Desktop\ITS\New folder\NH53_Accidents_2020.csv"
df_2020.to_csv(output_csv, index=False)

print(f"2020 data saved to: {output_csv}")
