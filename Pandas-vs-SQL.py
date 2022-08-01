#Pandas
#Concerning about SQL, we don't have to load all the dataset locally to make queries.
#When we think about Pandas, we have to.
import pandas as pd

df.head(10) #First 10 entries
df[['name', 'age']] #Returns 'name' and 'age' columns
df[(df['city'] == 'New York') & (df['salary'] >= 10000)] #Query 'WHERE'
df.groupby['country'].size() #Group By and Count