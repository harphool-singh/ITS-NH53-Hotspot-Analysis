import pandas as pd
import os
import sys

# ===============================
#  STEP 1 — FILE PATHS
# ===============================

# Input Excel file (update path if needed)
file_path = r"C:\Users\harph\OneDrive\Desktop\ITS\New folder\NH-53 Accident.xlsx"

# Output folder and CSV file path
output_folder = r"C:\Users\harph\OneDrive\Desktop\ITS\New folder\output"
output_file = os.path.join(output_folder, "NH53_Accidents_Combined.csv")

# Make sure output folder exists
os.makedirs(output_folder, exist_ok=True)

print("📂 Reading Excel file...")

# ===============================
#  STEP 2 — READ EXCEL FILE SAFELY
# ===============================
try:
    excel_file = pd.ExcelFile(file_path)
except PermissionError:
    print("❌ ERROR: File is open in Excel or locked. Please close it and rerun the script.")
    sys.exit(1)
except FileNotFoundError:
    print(f"❌ ERROR: File not found at {file_path}")
    sys.exit(1)

print("📑 Sheets found:", excel_file.sheet_names)

# ===============================
#  STEP 3 — COMBINE YEARLY SHEETS
# ===============================
combined_df = pd.DataFrame()

for sheet in excel_file.sheet_names:
    # Skip unwanted sheets like 'ALL' if needed
    if sheet.strip().upper() == "ALL":
        continue

    print(f"🔄 Reading sheet: {sheet} ...")
    try:
        df = excel_file.parse(sheet_name=sheet)
        df['Year'] = sheet  # add year column
        combined_df = pd.concat([combined_df, df], ignore_index=True)
    except Exception as e:
        print(f"⚠️ Could not read sheet '{sheet}': {e}")

# ===============================
#  STEP 4 — SAVE TO CSV
# ===============================
if not combined_df.empty:
    combined_df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"✅ Successfully combined {len(excel_file.sheet_names)} sheets.")
    print(f"💾 Saved combined file to: {output_file}")
else:
    print("⚠️ No data combined. Please check sheet names or file content.")
