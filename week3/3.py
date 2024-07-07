import pandas as pd
import numpy as np

bp = pd.read_csv("Building_Permits.csv")


print(bp.sample(2))

print(bp.isnull())


# print(bp.isnull().sum())
print(bp.shape)

# print(bp.dropna().isnull().sum())
# print(bp.dropna(axis=1).shape)
# print(bp.fillna(0).shape)
# print(bp.fillna(0).isnull().sum())
print(bp.fillna(method='ffill',axis=0).isnull().sum())

# Fill missing values with mean
bp_mean_filled = bp.fillna(bp.mean())

# Fill missing values with median
bp_median_filled = bp.fillna(bp.median())

print("After filling missing values with mean:")
print(bp_mean_filled.isnull().sum())

print("After filling missing values with median:")
print(bp_median_filled.isnull().sum())