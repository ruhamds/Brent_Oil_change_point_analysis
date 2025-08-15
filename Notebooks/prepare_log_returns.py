import pandas as pd

# Load the CSV
df = pd.read_csv(r"C:\Users\Antifragile\Desktop\Brent_Oil_change_point_analysis\Notebooks\processed_brent_data.csv")

# Format the date column
df["Date"] = pd.to_datetime(df["Date"])
df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

# Select only Date and log_returns
log_returns = df[["Date", "log_returns"]].dropna()

# Save to JSON format
log_returns.to_json("App/Backend/data/log_returns.json", orient="records", indent=2)

print("✅ log_returns.json created successfully!")
