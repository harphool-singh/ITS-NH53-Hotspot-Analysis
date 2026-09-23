import pandas as pd

# Load the CSV file
file_path = r"C:\Users\harph\OneDrive\Desktop\ITS\New folder\NH53_Accidents_2020.csv"
df = pd.read_csv(file_path)

# Drop rows where all elements are NaN
df.dropna(how='all', inplace=True)

# Drop columns where all elements are NaN
df.dropna(axis=1, how='all', inplace=True)

# Save the cleaned CSV to a new file
new_file_path = r"C:\Users\harph\OneDrive\Desktop\ITS\New folder\NH53_Accidents_2020_Cleaned.csv"
df.to_csv(new_file_path, index=False)

print(f"Cleaned CSV saved at: {new_file_path}")
