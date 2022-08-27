import pandas as pd
auto=pd.read_csv("Automobile_data.csv")
print(auto.head(200))
print(auto.info())
print(auto["price"].astype(str).astype(int).mean()) #here i converted datatype object to int 
print(auto[auto["price"]==auto["price"].max()]) #doubt
print(auto[auto["price"]==auto["price"].min()])
print(auto[auto["horsepower"]>100].count())
print(auto[auto["body-style"]=="hatchback"].info())
print(auto["make"].unique()) #for checking repititions in brands
print(auto["make"].value_counts().head(3)) #if we want we can use  .head() for top 3 cars 
print(auto[auto["price"]==7099]["make"])
print(auto[auto["price"]>40000])
print(auto[(auto["body-style"]=="sedan") &( auto["price"]<7000) ])






















