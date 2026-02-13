import pandas as pd

# Read CSV file
df = pd.read_csv('mock_data.csv')

# Read TSV file
df = pd.read_csv('mock_data.tsv', sep='\t')

# Write to CSV
df.to_csv('new_mock_data.csv', index=False)

# Write to TSV
df.to_csv('new_mock_data.tsv', sep='\t', index=False)

# Read the data first
df = pd.read_csv('mock_data.csv')

# Filter rows (example: filter by first name)
filtered = df[df['first_name'] == 'Jereme']

# Group by column and count
grouped = df.groupby('last_name').size()
print(grouped)