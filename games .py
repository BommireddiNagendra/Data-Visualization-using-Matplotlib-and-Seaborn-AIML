import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
# part1
games=pd.read_csv("games.csv")
print(games.head())
print(games.info())
print(games["playingtime"].mean())
print(games["total_comments"].max())
print(games[games["id"]==1500]["name"])
print(games[games["id"]==1500]["yearpublished"])
print(games[games["total_comments"]==games['total_comments'].max()]["name"])
print(games[games["total_comments"]==games['total_comments'].min()])
print(games.groupby("type").mean()['minage'])
print(games["id"].nunique()) #no of unique values(nunique)
print(games["type"].value_counts())   #we can  use groupby also
print(games[["playingtime","total_comments"]].corr())
# part2
sns.set(color_codes=True)
games.dropna(inplace=True) #for neglecting null values
print(games.info())
sns.displot(games["average_rating"],kde="True")
sns.distplot(games["average_rating"])
sns.jointplot(games["minage"],games["average_rating"])
sns.pairplot(games[["playingtime","minage","average_rating"]])
sns.stripplot(games["type"],games["playingtime"],jitter=True)
sns.regplot(x="playingtime",y='average_rating',data=games[games["playingtime"]<500])
plt.show() 
