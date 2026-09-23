import pandas as pd
import re

# 📂 Input and output paths
input_path = r"C:\Users\harph\OneDrive\Desktop\ITS\New folder\NH53_Accidents_2020_Cleaned.csv"
output_path = r"C:\Users\harph\OneDrive\Desktop\ITS\New folder\NH53_Accidents_2020_Cleaned_decimal.csv"

# 🔍 Function to convert DMS (e.g., N21° 06' 46.45") to Decimal Degrees
def dms_to_dd(dms_str):
    if pd.isna(dms_str):
        return None

    # Extract direction (N/S/E/W)
    direction = re.search(r'[NSEW]', dms_str)
    direction = direction.group() if direction else ''

    # Extract numeric components
    parts = re.findall(r'(\d+(?:\.\d+)?)', dms_str)
    if len(parts) < 3:
        return None

    deg, minutes, seconds = map(float, parts[:3])
    dd = deg + (minutes / 60) + (seconds / 3600)

    # South/West should be negative
    if direction in ['S', 'W']:
        dd = -dd

    return round(dd, 6)

# 🧠 Load data
df = pd.read_csv(input_path)

# 🧭 Convert both columns
df['Latitude_decimal'] = df['Latitude'].apply(dms_to_dd)
df['Longitude_decimal'] = df['Longitude'].apply(dms_to_dd)

# 💾 Save new CSV
df.to_csv(output_path, index=False)

print("✅ Conversion completed successfully!")
print(f"Saved as: {output_path}")
