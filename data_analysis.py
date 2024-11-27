# Goal: Sum up the results for all PAHs in the dataset file based on high/low molecular weights

import pandas as pd

combined_dataset = pd.read_excel("Data/combined_dataset.xlsx")
print(combined_dataset.columns)

# Low Molecular Weight PAH
low_PAH = ['Acenaphthene', 'Anthracene', 'Phenanthrene', 'Biphenyl', 'Naphthalene', '2,6-dimethylnaphthalene', 'Fluorene', '1-methylnaphthalene', '2-methylnaphthalene', '1-methylphenanthrene']
print("Low PAH:", low_PAH)

# High Molecular Weight PAH
high_PAH = ['Benzo(a)anthracene', 'Benzo(a)pyrene', 'Benzo(e)pyrene', 'Chrysene', 'Dibenz(a,h)anthracene', 'Fluoranthene', 'Perylene', 'Pyrene']
print("High PAH:", high_PAH)

# Filter to include only rows where "analytename" column matches the high/low PAHs
PAHS_data = combined_dataset[combined_dataset["analytename"].isin(low_PAH + high_PAH)]

print(PAHS_data)

# Add a column for molecular weight and label each row high or low based on PAH
PAHS_data["molecular_weight"] = PAHS_data["analytename"].apply(
    lambda x: "High" if x in high_PAH else "low"
)

# Group by molecular weight and sum the results
PAHS_summary = PAHS_data.groupby("molecular_weight")["result"].sum().reset_index()
print(PAHS_summary)

# Create new excelsheet
PAHS_summary.to_excel("Data/pahs_summary.xlsx", index=False)