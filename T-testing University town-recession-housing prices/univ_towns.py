import pandas as pd
def clean(string):
        rs = ''
        for i in string:
            if(i=='(' or i=='['):
                return rs.strip()
            else:
                rs = rs+i
        return rs.rstrip()
def checkstate(string):
    #print(string[-5:-1])
    if(string[-5:-1]=='edit'):
        return True
    else:
        return False
def get_list_of_university_towns():
    '''Cleans data and returns data in the form of ['state','region']'''
    df = pd.read_csv('university_towns.txt',sep='delimiter',header=None,engine='python')
    d=[]
    for i in df.values:
        if(checkstate(i[0])):
            state = clean(i[0])
            continue
        else:
            f=[state,clean(i[0])]
            d.append(f)
    t = pd.DataFrame(d,columns=['State','RegionName'])
    return t
