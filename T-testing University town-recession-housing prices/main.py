import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from univ_towns import get_list_of_university_towns
from recession import get_recession_start,get_recession_bottom
from housing_time_conversion import convert_housing_data_to_quarters
H = convert_housing_data_to_quarters()
U = get_list_of_university_towns()
rs = get_recession_start()
rb = get_recession_bottom()
H['priceratio']=price_ratio=H[rs]/H[rb]
G = H.merge(U,how='inner',left_index=True,right_on=['State','RegionName'])
G.set_index(['State','RegionName'],inplace=True)
F = H[(~(H.index.isin(G.index)))]
F.reset_index(inplace=True)
G.reset_index(inplace=True)
t,p = ttest_ind(F['priceratio'].dropna(),G['priceratio'].dropna())
difference = True if p<0.01 else False
better = 'university towns' if(F['priceratio'].mean() > G['priceratio'].mean()) else 'non-university towns'
worse = 'non-university towns' if(F['priceratio'].mean() > G['priceratio'].mean()) else 'university towns'
print('Alternate Hypothesis: Recession has affected the housing prices of university towns more than the non-university towns')
if(difference):
    string = 'Reliably Different'
else:
    string = 'Reliably Similar'
print('An independent-samples t-test was used to check the above hypothesis. We have got a p-value of',p)
print('which suggests that the samples are', string)
if(difference):
    print('Recession has been reliably proven by the test to hit university towns and non-university towns differently',end='\n')
    print('We have found also out that recession has affected',better,'less than',worse)
'''

Output:
Alternate Hypothesis: Recession has affected the housing prices of university towns more than the non-university towns
An independent-samples t-test was used to check the above hypothesis. We have got a p-value of 0.005496427353694603 which suggests that the samples are Reliably Different
Recession has been reliably proven by the test to hit university towns and non-university towns differently
We have found also out that recession has affected university towns less than non-university towns
'''