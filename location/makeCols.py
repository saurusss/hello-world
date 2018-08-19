import pandas as pd
import numpy as numpy
import math
loc = pd.read_excel(r'C:\Users\sauru\Documents\GitHub\hello-world\location\loc_180818.xlsx')
print(loc)

addDf = pd.DataFrema()

for i in range(5):
    print(loc.mgmtNum[i], loc.latitude[i], loc.longitude[i])
    loc['D'+loc.mgmtNum[i]] = 0.0
    for j in range(5):
        distY = abs(loc.latitude[i] - loc.latitude[j])
        distX = abs(loc.longitude[i]-loc.longitude[j])
        dist = math.sqrt(distX**2 + distY**2)
        loc.loc[j].'D'+ mgmtNum[i] = dist

        print(add_col)
   
    # print(add_col)
    # loc[loc.mgmtNum[i]] = add_col