# Goal: Combine multiple datasets together

# Use the analyteclasses.xlsx and station.xlsx file to pull in the analyteclass, latitude, and longitude fields into the dataset.xlsx file. You will need the analytename and stationid fields to match each dataset up.

import pandas as pd

analytic_class = pd.read_excel("Data/analyteclasses.xlsx")
# print(analytic_class)

stations = pd.read_excel("Data/stations.xlsx")
# print(stations)

dataset = pd.read_excel("Data/dataset.xlsx")
# print(dataset)

# Merge on 'analytename' and 'stationid' with left join
merged_dataset = dataset.merge(analytic_class, on="analytename", how="left")
merged_dataset = merged_dataset.merge(stations, on="stationid", how="left")

# Save combined dataset to new Excel file
# index=False prevents the DataFrame's index from being written to the Excel file
merged_dataset.to_excel("Data/combined_dataset.xlsx", index=False)

print(merged_dataset)