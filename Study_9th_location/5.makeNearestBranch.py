import pandas as pd
import numpy as numpy
import sqlite3
import math
 
conn = sqlite3.connect(r'C:\Temp\loc_post.db')
cursor = conn.cursor()

df = pd.read_sql_query("select * from position where nearestBranch is null", conn)
df = df.set_index('index')

startP = df[:1]
for i in df[1:]:
        distY = abs(startP['latitude'] - i['latitude'])
        distX = abx(startP['longitue'] - i['longitude'])
        dist = math.sqrt(distX**2 - distY**2)
        print(dist)

# rows = cursor.fetchall()
# for row in rows:
#         print(row)

conn.commit()
conn.close()