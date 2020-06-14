import pandas as pd
def convert_housing_data_to_quarters():
    states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 
          'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 
          'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 
          'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 
          'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 
          'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 
          'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 
          'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 
          'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 
          'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 
          'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 
          'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 
          'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 
          'VA': 'Virginia'}
    df = pd.read_csv('City_Zhvi_AllHomes.csv')
    df['State'] = df['State'].replace(states)
    L = [df.columns[i] for i in range(3,51)]
    df.drop(labels=[df.columns[0]]+L,axis=1,inplace=True)
    for i in range(2000,2016):
        df[str(i)+'q1'] = df[[str(i)+'-01',str(i)+'-02',str(i)+'-03']].mean(axis=1)
        df[str(i)+'q2'] = df[[str(i)+'-04',str(i)+'-05',str(i)+'-06']].mean(axis=1)
        df[str(i)+'q3'] = df[[str(i)+'-07',str(i)+'-08',str(i)+'-09']].mean(axis=1)
        df[str(i)+'q4'] = df[[str(i)+'-10',str(i)+'-11',str(i)+'-12']].mean(axis=1)
    df['2016q1']=df[['2016-01','2016-02','2016-03']].mean(axis=1)
    df['2016q2']=df[['2016-04','2016-05','2016-06']].mean(axis=1)
    df['2016q3']=df[['2016-07','2016-08']].mean(axis=1)
    L = [df.columns[i] for i in range(2,202)]
    df.drop(labels=L,axis=1,inplace=True)
    df.set_index(['State','RegionName'],inplace=True)
    df.sort_index(inplace=True)
    return df