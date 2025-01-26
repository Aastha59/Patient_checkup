#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the dataset from the CSV file
df = pd.read_csv("hospital_treatment.csv")

# Statistical analysis
age_mean = df["Age"].mean()
age_median = df["Age"].median()
age_std = df["Age"].std()

length_mean = df["Length of Stay (days)"].mean()
length_median = df["Length of Stay (days)"].median()
length_std = df["Length of Stay (days)"].std()

# Display results
print("Age Statistics:")
print(f"Mean: {age_mean}")
print(f"Median: {age_median}")
print(f"Standard Deviation: {age_std}\n")

print("Length of Stay Statistics:")
print(f"Mean: {length_mean}")
print(f"Median: {length_median}")
print(f"Standard Deviation: {length_std}")


# In[ ]:




