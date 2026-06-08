import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df =pd.read_csv(r"D:\RetailPulse\data\SampleSuperstore.csv.zip")
print("\nExploratry data analysis")
print("\nfirst 5 sample data",df.head())
print("\nshap of data",df.shape)
print("\ncolumns",df.columns)
print("\nmissing values ",df.isnull().sum())
print("\nstructure of data",df.info())
print("summary\n",df.describe())
#Histogram
plt.hist(df["Sales"], bins=30)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()
#corelation heatmap
corr = df[["Sales", "Quantity", "Discount", "Profit"]].corr()

sns.heatmap(corr, annot=True)

plt.title("Correlation Heatmap")
plt.show()
print("eda Completed Successfully")