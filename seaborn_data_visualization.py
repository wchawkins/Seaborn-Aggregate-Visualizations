from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.ticker as mtick

df = pd.read_csv("kiva_data.csv")
print(df.head())

# Creates the figure, note: you're only using this syntax so that you can modify the y-axis ticks later
import matplotlib.ticker as mtick

# Visualization one-- Bar Plot
f, ax = plt.subplots(figsize=(15, 10))
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
sns.barplot(data=df, x="country", y = "loan_amount")
plt.title("Loan Amounts by Country")
sns.set_palette("Dark2")
sns.set_style("whitegrid")
plt.show()

# Visualization two-- Nested Bar Plot
f, ax = plt.subplots(figsize=(15, 10))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
sns.barplot(data=df, x="country", y = "loan_amount", hue="gender")
plt.title("Loan Amounts by Country and Sex")
sns.set_palette("Dark2")
sns.set_style("whitegrid")
plt.show()

# Visualization three-- Box Plot
f, ax = plt.subplots(figsize=(15, 10))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
sns.boxplot(data=df, x="country", y = "loan_amount")
plt.title("Loan Amount Distributions by Country")
sns.set_palette("Dark2")
sns.set_style("whitegrid")
plt.show()

# Visualition four-- Violin Plot
f, ax = plt.subplots(figsize=(15, 10))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
sns.violinplot(data=df, x="activity", y = "loan_amount")
plt.title("Loan Amounts and Distributions by Business Type")
sns.set_palette("Dark2")
sns.set_style("whitegrid")
plt.show()

# Visualization five-- Nexted Violin Plot
f, ax = plt.subplots(figsize=(15, 10))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
sns.violinplot(data=df, x="country", y = "loan_amount", hue="gender", split=True)
plt.title("Loan Amounts and Distributions by Country and Gender")
sns.set_palette("Dark2")
sns.set_style("whitegrid")
plt.show()
