import numpy as np 
import pandas as pd 
print(pd.__version__)
'''
myData = np.array(['a','b','c','d', 'e', 'Cat', 42])
mySeries = pd.Series(myData)
print (mySeries)
print(type(mySeries))

myData = np.array([134.29, 136.97, 250.31, 312.28])
mySeries = pd.Series(myData,index=['IBM','P&G','Microsoft','Home Depot'])
print (mySeries)
#I want KO in my series. Add a new row to the series for KO
mySeries["KO"] = 62.5
print(mySeries)
#I want to delete the P&G row
mySeries = mySeries.drop("P&G")
print(mySeries)

print(mySeries['IBM']) #index notation
print(mySeries[['IBM','KO']]) #index and list notation


myData = np.array([134.29, 136.97, 250.31, 312.28])
mySeries = pd.Series(myData,index=['IBM','P&G','Microsoft','Home Depot'], name="Stock Price")
myData1 = np.array(['120.573B', '336.72B', '1.885T' , '335.974B'])
mySeries1 = pd.Series(myData1, index=['IBM','P&G','Microsoft','Home Depot'], name="Market Cap")
myDataFrame = pd.concat([mySeries, mySeries1], axis=1)
print(myDataFrame)
#Add a name to the index column: "Company"
myDataFrame.index.name = "Company"
print(myDataFrame)
#I would like to add ACN, trading at $286 and Mkt Cap is 180B
'''

purchases = {
    'guava': [4, 8, 1, 11],
    'pears': [44, 33, 88, 12],
    'avocados':[42, 100, 50, 900]
}
df = pd.DataFrame(purchases)
print(df)
df.index=['Kroger', 'Publix', 'Remke', 'IGA']
df.index.name = 'Store'
print(df)
# Add two new rows by creating a new DataFrame and appending it to our DataFrame
newRows = {'guavas': [10, 20],
           'pears':[111,222],
           'avocados':[200,3000]}
newDF = pd.DataFrame(newRows)
#print (newDF)
newDF.index=['Thriftway', 'Meijer']
newDF.index.name = 'Store'
#print(newDF)
# ignore_index = True means create a new index # for the row
# sort = False means don't sort the columns
df = pd.concat([newDF, df], ignore_index=False, sort=False)
print(df)
#We realized there's a problem with our guavas.
#Delete all columns with missing values
df = df.dropna(axis=1) #could also use: axis='columns'
print(df)

apples = {'apples':[1,2,3,4,5,6]}
# items() returns the iterator of the dictionary
for key,value in apples.items():
    df[key] = value
print(df)
#I wanna know the total apples across all stores
Total = df['apples'].sum()
print(Total)