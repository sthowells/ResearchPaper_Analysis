import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os # filename directory

for dirname, _, filenames in os.walk("""/Users/sethhowells/Desktop/MSDS/FALL 21/DataViz/WEEK 1/"""):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('AutoInsurance.csv')

# remove first row of dataframe
data = df.iloc[1:,:]
print(data.head(10))
"""
# quick commands
print("List of 24 variables\n")
print(data.columns)
print("Describe variable")
print(data.describe())
"""
import seaborn as sns
sns.pairplot(df)

import matplotlib.pyplot as plt

corrmat = df.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(20,20))
g=sns.heatmap(df[top_corr_features].corr(),annot=True,cmap="RdYlGn")



