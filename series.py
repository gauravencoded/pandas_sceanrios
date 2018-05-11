import pandas as pd

#empty series
print("Creating empty series")
emptySeries=pd.Series()
print(emptySeries)

#creating a series with array and index
print("Creating a series")
series=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print (series[:3]) #prints upto three values


#series with no index
print("Series made when indexes are not passed")
noIndexSeries=pd.Series(['All', 'Is','Well','Without','Index'])
print(noIndexSeries)

# series from a dictionary
print("Series made using dictionary(Key, Value pairs like js)")
dictionarySeries=pd.Series({'a':0,'b':2,'c':4,'d':6})
print(dictionarySeries)

#dictionary with new indexes(other than keys of dictionaries)
print("New indexes")
newIndexSeries=pd.Series({'a':1,'b':2,'c':3,'d':4},index=[101,'b',301,'d'])
print(newIndexSeries)

#creating a series from scalar
print("Series from scalar")
scalarSeries=pd.Series(5,index=[0,1,2,3])
print(scalarSeries)


print("Retrieving data from sereis")

print("Selecting specific value")
print(scalarSeries[2])
print("Selecting +ve range")
print(scalarSeries[:2])
print("Selecting -ve range")
print(scalarSeries[-2:])
print("Retrieve multiple values")
print(scalarSeries[[0,1,3]])


