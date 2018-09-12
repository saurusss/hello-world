#%matplotlib tk
#%matplotlib qt5
#%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sqlite3

print("*"*10, "start of job", "*"*11)
conn = sqlite3.connect(r'C:\Temp\loc_post.db')

# zone = "서울지방우정청\'  or Department = \'경인지방우정청"
# zoneName = "Seoul + Kyeongki-Incheon"
zone = "서울지방우정청"
zoneName = "Seoul"
# zone = "경인지방우정청"
# zoneName = "Kyeongki-Incheon"
# zone = "충청지방우정청"
# zoneName = "Chungcheong"
# zone = "강원지방우정청"
# zoneName = "Kangweon"
# zone = "우정공무원교육원"
# zoneName = "Education"

sqlQuery  = "select officeName, latitude, longitude from position \
            where Department = \'"+ zone  + "\'"      
     
            
df = pd.read_sql_query(sqlQuery, conn)
# df = pd.read_sql_query("select officeName, latitude, longitude from position", conn)
 
df = df.set_index('officeName')


plt.title(zoneName)
plt.scatter(df.longitude, df.latitude,  marker ='.', c='r')
plt.ylabel('Latitude')
plt.xlabel('Longitude')
#plt.legend()
plt.grid(True)
plt.show()
print("*"*10, "end   of job", "*"*11)