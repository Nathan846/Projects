import pandas as pd
def get_recession_start():
    pd.set_option('display.max_rows', 500)
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''
    df = pd.ExcelFile('gdplev.xls')
    t = df.parse(usecols=[4,6],skiprows=7)
    t.columns=['Quarter','GDP']
    t = t.iloc[212:]
    t.reset_index(inplace=True)
    L=[]
    T=[]
    for i in range(2,t.index.size):
        if(t.iloc[i]['GDP']<t.iloc[i-1]['GDP'] and t.iloc[i-1]['GDP']<t.iloc[i-2]['GDP']):
            if(t.iloc[i-3]['Quarter'] in T):
                L.append(t.iloc[i-2]['Quarter'])
            else:
                T.append(t.iloc[i-2]['Quarter'])
    return L[0]
def get_recession_end():
    df = pd.ExcelFile('gdplev.xls')
    t = df.parse(usecols=[4,6],skiprows=7)
    t.columns=['Quarter','GDP']
    t = t.iloc[212:]
    G = get_recession_start()
    t.reset_index(inplace=True)
    i=t[t['Quarter']==G].index[0]
    #print(t.iloc[i])
    while(True):
        i+=1
        #print(t.iloc[i]['GDP'])
        if(t.iloc[i]['GDP']>t.iloc[i-1]['GDP'] and t.iloc[i-1]['GDP']>t.iloc[i-2]['GDP']):
            return t.iloc[i]['Quarter']
    return "ANSWER"
def get_recession_bottom():
    df = pd.ExcelFile('gdplev.xls')
    t = df.parse(usecols=[4,6],skiprows=7)
    t.columns=['Quarter','GDP']
    t = t.iloc[212:]
    t.reset_index(inplace=True)
    G = get_recession_start()
    H = get_recession_end()
    lowbound=t[t['Quarter']==G].index[0]
    upbound =t[t['Quarter']==H].index[0]
    #print(lowbound,upbound)
    mins=10**10
    for i in range(lowbound,upbound):
        if(t.iloc[i]['GDP']<mins):
            mins=t.iloc[i]['GDP']
            val= t.iloc[i]['Quarter']
    return val
