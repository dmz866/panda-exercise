import pandas as pd
import matplotlib as plt

n = pd.Series([1,2,3,4,5,6])
#print(n.mean()) #promedio

#sum
n.sum()

c = pd.Series(['red', 'blue', 'yellow'])

d = pd.Series(['sedan', 'suv', 'pick up'])


#Create dataframe
table = pd.DataFrame({'Car Type': d, 'Color': c})

#Create csv
#table.to_csv('test_files/test_file.csv')

#Read csv
cars = pd.read_csv('test_files/ventas-autos.csv')

#Columns type
#print(cars.dtypes)

#print(cars)

# Statistics for number columns only
#print(cars.describe())

# Info
#print(cars.info())

# List columns
#print(cars.columns)

#List n rows (default 5 rows)
#print(cars.head())
#print(cars.head(8))

#List last n rows (default 5 rows)
#cars.tail()

#Select specific row
#print(cars.loc[2])

#Select multiple rows
#print(cars.iloc[[1,2,7]])

#Select specific column
#print(cars['Kilometraje'].mean())

#Filters
#print(cars[cars['Kilometraje'] > 100000])
#print(cars[cars['Color'] == 'Blanco'])

#Cross tables
#print(pd.crosstab(cars['Fabricante'], cars['Puertas']))

#Group by
#print(cars.groupby(['Fabricante']).mean())


##########################################

#print(cars['Kilometraje'].plot())
#print(cars['Kilometraje'].hist())


