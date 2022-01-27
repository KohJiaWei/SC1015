# Basic Libraries
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt # we only need pyplot
sb.set() # set the default Seaborn style for graphics

csv_data = pd.read_csv('train.csv')
csv_data.head()

csv_data.dtypes

filtered = csv_data.select_dtypes(include='int64')
filtered.head()

filtered.columns

#identified actual numeric variable
#LotArea
#SalePrice
#pool area
array = ["LotArea","SalePrice","PoolArea"]
filtered = csv_data.drop(columns = ["LotArea","SalePrice","PoolArea"])


filtered['SalePrice'].mean()


filtered['SalePrice'].median()

filtered['SalePrice'].quantile([0.25,0.5,0.75])

f = plt.figure(figsize=(24, 4))
sb.boxplot(data = filtered['SalePrice'], orient = "h")

f = plt.figure(figsize=(16, 8))
sb.histplot(data = filtered['SalePrice'])

f = plt.figure(figsize=(16, 8))
sb.kdeplot(data = filtered['SalePrice'])

filtered['LotArea'].mean()

filtered['LotArea'].median()

filtered['LotArea'].quantile([0.25,0.5,0.75])

f = plt.figure(figsize=(24, 4))
sb.boxplot(data = filtered['LotArea'], orient = "h")

f = plt.figure(figsize=(16, 8))
sb.histplot(data = filtered['LotArea'])

f = plt.figure(figsize=(16, 8))
sb.kdeplot(data = filtered['LotArea'])

# Create a joint dataframe by concatenating the two variables
jointDF = pd.concat([filtered['LotArea'], filtered['SalePrice']], axis = 1).reindex(filtered['LotArea'].index)
jointDF

sb.jointplot(data = jointDF, x = filtered['LotArea'] ,y = filtered['SalePrice'], height=6, ratio=5)

filtered['LotArea'].corr(filtered['SalePrice'])
