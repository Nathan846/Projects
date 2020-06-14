import matplotlib.pyplot as plt
import pandas as pd
fd = pd.read_csv('fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
fd['Date'] = pd.to_datetime(fd['Date'])
fd.set_index('Date',inplace=True)
fd.Data_Value = fd.Data_Value/10
df = fd.loc['2005-01-01':'2014-12-31']
df1 = fd.loc['2015-01-01':'2015-12-31']
df.reset_index(inplace=True)
df1.reset_index(inplace=True)
df['Month'] = df['Date'].dt.month
df['Days'] = df['Date'].dt.day
df1['Month'] = df1['Date'].dt.month
df1['Days'] = df1['Date'].dt.day
df.set_index(['Month','Days','ID'],inplace=True)
df1.set_index(['Month','Days','ID'],inplace=True)
df.sort_index(inplace=True)
df1.sort_index(inplace=True)
mindf = df[df['Element']=='TMIN']
maxdf = df[df['Element']=='TMAX']
minscatter = df1[df1['Element']=='TMIN']
maxscatter = df1[df1['Element']=='TMAX']
mind = mindf.groupby(level=(0,1)).min()
minscat = minscatter.groupby(level=(0,1)).min()
mind.drop((2,29),inplace=True)
try:
    print(mind.loc[(2,29)])
except:
    print('Leap value deleted')
mind.reset_index(inplace=True)
minscat.reset_index(inplace=True)
mind.drop('Date',axis=1,inplace=True)
mind['Datetime'] = '2015'+mind['Days'].astype(str) + mind['Month'].astype(str)
mind['newDate'] = pd.to_datetime('2015'+mind['Month'].astype(str)+'-'+mind['Days'].astype(str), format='%Y%m-%d')
minscat['newDate'] = pd.to_datetime('2015'+minscat['Month'].astype(str)+'-'+minscat['Days'].astype(str), format='%Y%m-%d')

mind.set_index('newDate',inplace=True)
minscat.set_index('newDate',inplace=True)
min_df = mind['Data_Value']

maxd = maxdf.groupby(level=(0,1)).max()
maxs = maxscatter.groupby(level=(0,1)).max()
#print(maxscatter)
print(maxd.loc[(2,29)])
maxd.drop((2,29),inplace=True)
try:
    print(maxd.loc[(2,29)])
except:
    print('Leap value deleted')#maxd
    
maxd.reset_index(inplace=True)
maxs.reset_index(inplace=True)
print(maxd.head())
maxd['newDate'] = pd.to_datetime('2015'+maxd['Month'].astype(str)+'-'+maxd['Days'].astype(str), format='%Y%m-%d')
maxd.set_index('newDate',inplace=True)
maxs['newDate'] = pd.to_datetime('2015'+maxs['Month'].astype(str)+'-'+maxs['Days'].astype(str), format='%Y%m-%d')
maxs.set_index('newDate',inplace=True)

mind.sort_index(inplace=True)
mind.sort_index(inplace=True)
min_df = mind['Data_Value']
max_df = maxd['Data_Value']
minscat = minscat['Data_Value']
maxscat = maxs['Data_Value']
mi = minscat[min_df>minscat]
mi.head()
ma = maxscat[max_df<maxscat]
ma.head()
u = mi.index.values
x = max_df.index.values
from matplotlib.pyplot import figure
figure(num=None, figsize=(8, 6), facecolor='w', edgecolor='k')
ax = plt.gca()
plt.plot(x, min_df, color='lightblue', markersize=10,label='Min.Temp')
plt.plot(x, max_df, color='coral', markersize=10,label='Max.Temp')
u = mi.index.values
plt.scatter(u,mi,color='darkblue',label='Decade low points')
plt.scatter(ma.index.values,ma,color='red',label='Decade high points')
ax.legend(title='legend',frameon=False)
ax.fill_between(x,min_df.values.flatten(),max_df.values.flatten(),color='grey',alpha=0.5)
plt.title('Maximum/Minimum Temperature span over 10 years')
ax.set_xlabel('Month',fontsize=18)
ax.set_ylabel('Temperature in C',fontsize=18)
plt.show()
