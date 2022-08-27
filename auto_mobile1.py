
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_color_codes=True
auto=pd.read_csv("Automobile_data.csv")
# print(auto.head())
sns.displot(auto["normalized-losses"],kde=True,rug=True)
sns.jointplot(auto["engine-size"],auto["horsepower"],kind="resid")
sns.pairplot(auto[["num-of-cylinders"],auto["engine-size"],auto["horsepower"]])
sns.stripplot(auto["fuel-type"],auto["horsepower"],jitter=True)
sns.swarmplot(auto["fuel-type"],auto["horsepower"])
sns.boxplot(auto["num-of-doors"],auto["horsepower"],hue=auto["fuel-type"])
sns.countplot(auto["body-style"],hue=auto["fuel-type"])
sns.pointplot(auto["num-of-doors"],auto["horsepower"],hue=auto["fuel-type"])
plt.show()