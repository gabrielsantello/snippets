import pandas as pd

#Create dataframe
df = pd.DataFrame({'customer': ['A', 'A', 'B', 'B', 'C', 'C'],
                   'customer-type': ['Regular', 'Low', 'High', 'Regular', 'Regular', "Low"],
                   'frequency': [15, 3, 24, 25, 9, 5],
                   })

'''
df.groupby('customer')\ #group by customer
.agg({'frequency': [min, max]})\ #aggregate by 'frequency', return min and max values
.rename(columns={'min': 'amt1', 'max': 'amt2'})\ #rename columns min/max
.droplevel(0, axis=1)\ #drop the level created by 'frequency' aggregation
.reset_index() #remove 'customer' from the index
'''
df.groupby('customer').agg({'frequency': [min, max]}).rename(columns={'min': 'amt1', 'max': 'amt2'}).droplevel(0, axis=1).reset_index()