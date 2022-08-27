import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns 
sns.set(color_codes=True)
auto=pd.read_csv('Automobile_data.csv')
print(auto.shape)
print(auto.head())
sns.lmplot(x='city-mpg',y='highway-mpg',hue='fuel-type',data=auto)
plt.show()