import pandas as pd
import numpy as np

df= pd.read_csv('all_mtg_cards.csv', low_memory=False)
#print (df.shape)
#print (df.head)


#Fix TWO issues with the data set using techniques you've learned in class. Issue 1
#print (df.names.unique)

#names column is only filled with nan values
df.drop(df.columns[[3]], axis=1, inplace = True)
#print (df.columns)

#Fix TWO issues with the data set using techniques you've learned in class. Issue 2
#print (df.multiverse_id.unique)

#multiverse_id has multiple NaN values
df.dropna(axis=0, how = 'any', thresh = None, subset= ['multiverse_id'], inplace= True)
print (df.multiverse_id.unique)
