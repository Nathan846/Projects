
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv`. This is the dataset to use for this assignment. Note: The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Ann Arbor, Michigan, United States**, and the stations the data comes from are shown on the map below.

# In[205]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]
    print(df.columns)

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='b', alpha=0.5,s=200)

    
    return mplleaflet.display()
leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')


# In[102]:

import pandas as pd


# In[157]:

fd = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
fd['Date'] = pd.to_datetime(fd['Date'])
fd.set_index('Date',inplace=True)
fd.Data_Value = fd.Data_Value/10
df = fd.loc['2005-01-01':'2014-12-31']
df1 = fd.loc['2015-01-01':'2015-12-31']
df.reset_index(inplace=True)
df1.reset_index(inplace=True)


# In[158]:

df['Month'] = df['Date'].dt.month
df['Days'] = df['Date'].dt.day
df1['Month'] = df1['Date'].dt.month
df1['Days'] = df1['Date'].dt.day


# In[159]:

df.set_index(['Month','Days','ID'],inplace=True)
df1.set_index(['Month','Days','ID'],inplace=True)


# In[160]:

df.sort_index(inplace=True)
df1.sort_index(inplace=True)


# In[161]:

mindf = df[df['Element']=='TMIN']
maxdf = df[df['Element']=='TMAX']
minscatter = df1[df1['Element']=='TMIN']
maxscatter = df1[df1['Element']=='TMAX']


# In[162]:

mind = mindf.groupby(level=(0,1)).min()
minscat = minscatter.groupby(level=(0,1)).min()


# In[121]:

#minscat


# In[163]:

mind.drop((2,29),inplace=True)
try:
    print(mind.loc[(2,29)])
except:
    print('Leap value deleted')
mind.reset_index(inplace=True)
minscat.reset_index(inplace=True)
mind.drop('Date',axis=1,inplace=True)


# In[164]:

mind['Datetime'] = '2015'+mind['Days'].astype(str) + mind['Month'].astype(str)
mind['newDate'] = pd.to_datetime('2015'+mind['Month'].astype(str)+'-'+mind['Days'].astype(str), format='%Y%m-%d')
minscat['newDate'] = pd.to_datetime('2015'+minscat['Month'].astype(str)+'-'+minscat['Days'].astype(str), format='%Y%m-%d')


# In[204]:

mind.head()


# In[166]:


mind.set_index('newDate',inplace=True)
minscat.set_index('newDate',inplace=True)
min_df = mind['Data_Value']


# In[168]:

maxd = maxdf.groupby(level=(0,1)).max()
maxs = maxscatter.groupby(level=(0,1)).max()


# In[169]:

#print(maxscatter)
print(maxd.loc[(2,29)])
maxd.drop((2,29),inplace=True)
try:
    print(maxd.loc[(2,29)])
except:
    print('Leap value deleted')#maxd


# In[203]:

maxd.reset_index(inplace=True)
maxs.reset_index(inplace=True)
print(maxd.head())


# In[173]:

maxd['newDate'] = pd.to_datetime('2015'+maxd['Month'].astype(str)+'-'+maxd['Days'].astype(str), format='%Y%m-%d')
maxd.set_index('newDate',inplace=True)
maxs['newDate'] = pd.to_datetime('2015'+maxs['Month'].astype(str)+'-'+maxs['Days'].astype(str), format='%Y%m-%d')
maxs.set_index('newDate',inplace=True)


# In[34]:

mind.sort_index(inplace=True)
mind.sort_index(inplace=True)


# In[174]:

min_df = mind['Data_Value']
max_df = maxd['Data_Value']
minscat = minscat['Data_Value']
maxscat = maxs['Data_Value']


# In[38]:

all(min_df.index==max_df.index)


# In[41]:

import matplotlib.pyplot as plt


# In[202]:

mi = minscat[min_df>minscat]
mi.head()


# In[201]:

ma = maxscat[max_df<maxscat]
ma.head()


# In[206]:

x = max_df.index.values
from matplotlib.pyplot import figure
figure(num=None, figsize=(8, 6), facecolor='w', edgecolor='k')
ax = plt.gca()
plt.plot(x, min_df, color='navy', markersize=10,label='Min.Temp')
plt.plot(x, max_df, color='navy', markersize=10,label='Max.Temp')
u = mi.index.values
plt.scatter(u,mi,color='darkblue',label='Decade low points')
plt.scatter(ma.index.values,ma,color='red',label='Decade high points')
ax.legend(title='legend',frameon=False)
ax.fill_between(x,min_df.values.flatten(),max_df.values.flatten(),color='aquamarine',alpha=0.5)
plt.title('Maximum/Minimum Temperature span over 10 years')
ax.set_xlabel('Month',fontsize=18)
ax.set_ylabel('Temperature in C',fontsize=18)
plt.show()


# In[ ]:



