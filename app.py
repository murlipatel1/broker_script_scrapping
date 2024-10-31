import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load each CSV file
csv1 = pd.read_csv('Angel_one.csv')
csv2 = pd.read_csv('NSE_CD.csv')
csv3 = pd.read_csv('NSE_CM.csv')
csv4 = pd.read_csv('TradeApiInstruments_Cash.csv')

# Print columns to verify their presence
print("CSV1 Columns:", csv1.columns)
print("CSV2 Columns:", csv2.columns)
print("CSV3 Columns:", csv3.columns)
print("CSV4 Columns:", csv4.columns)

# Strip leading and trailing spaces from column names
csv2.columns = csv2.columns.str.strip()
csv3.columns = csv3.columns.str.strip()

# Normalize column names across DataFrames, using 'symbol' or 'instrument_name' for a common identifier
csv1 = csv1.rename(columns={"token": "id", "symbol": "symbol", "name": "instrument_name", "exch_seg": "exchange"})
csv2 = csv2.rename(columns={"id": "id", "symbol": "symbol", "instrument_name": "instrument_name", "symbol_exchange": "exchange"})
csv3 = csv3.rename(columns={"id": "id", "symbol": "symbol", "company_name": "instrument_name", "symbol_exchange": "exchange"})
csv4 = csv4.rename(columns={"instrumentToken": "id", "symbol": "symbol", "instrumentName": "instrument_name", "exchange": "exchange"})

# Check if 'symbol' or 'instrument_name' is available in all CSVs and use for merging
merge_key = "symbol" if "symbol" in csv1.columns and "symbol" in csv2.columns and "symbol" in csv3.columns and "symbol" in csv4.columns else "instrument_name"

# Perform the merge using the identified key
merged_df = pd.merge(csv1, csv2, on=merge_key, how="outer", suffixes=('_csv1', '_csv2'))
merged_df = pd.merge(merged_df, csv3, on=merge_key, how="outer", suffixes=('', '_csv3'))
merged_df = pd.merge(merged_df, csv4, on=merge_key, how="outer", suffixes=('', '_csv4'))

# Display the first few rows of the merged DataFrame
print("Merged DataFrame Preview:")
print(merged_df.head())

# Visualization: Distribution of lot sizes across brokers
plt.figure(figsize=(10, 6))
sns.histplot(data=merged_df, x="lotsize", color="blue", label="CSV1", kde=True)
sns.histplot(data=merged_df, x="lot_size", color="orange", label="CSV2", kde=True)
sns.histplot(data=merged_df, x="lot_size", color="green", label="CSV3", kde=True)
sns.histplot(data=merged_df, x="lotSize", color="red", label="CSV4", kde=True)
plt.legend()
plt.title("Distribution of Lot Sizes Across Brokers")
plt.xlabel("Lot Size")
plt.ylabel("Frequency")
plt.show()

# Visualization: Count of instruments by exchange across brokers
plt.figure(figsize=(10, 6))
sns.countplot(data=merged_df, x="exchange")
plt.title("Instrument Count by Exchange Across Brokers")
plt.xlabel("Exchange")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()
