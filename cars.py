import pandas as pd

df = pd.read_csv("carSale.csv")

for col in df.columns[1:]:
    df[col] = df[col].str.replace(',', '').astype(int)

jan_aug_total = df.iloc[:, 1:].sum()

manufacture_totals = df.set_index(df.columns[0]).sum(axis=1)

print("Task 1: Addition for all manufacturers (January to August):")
print(jan_aug_total)
print("\nTask 2: Total sum of numbers for each manufacturer:")
print(manufacture_totals)
