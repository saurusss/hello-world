import pandas as pd
import numpy as np
import sqlite3
import math
import datetime
 

print("*"*10, "start of job", "*"*10)
conn = sqlite3.connect(r'C:\Temp\loc_post.db')
df = pd.read_sql_query("select * from position where nearestBranch is null", conn)
cnt = len(df)

while cnt > 1:

        conn = sqlite3.connect(r'C:\Temp\loc_post.db')
        cursor = conn.cursor()

        df = pd.read_sql_query("select * from position where nearestBranch is null", conn)
        cnt = len(df)
        cnt -= 1

        conn.close()

        del df['index']
        df = df.set_index('officeName')
        # df = df.sort_index(ascending=False)
        df = df.sort_values(by='address',ascending=False)

        df_c = pd.DataFrame(columns=['officeName','dist'])
        df_c = df_c.set_index('officeName')

        wofficeName = df.index[0]
        wlat = df.loc[wofficeName]['latitude']
        wlon = df.loc[wofficeName]['longitude']
        df = df.drop(wofficeName)

        #단위당 거리(미터)
        baseLat = 110979.309
        baseLon = 88907.949
        for i in df.index:
                df_c.loc[i] =  math.sqrt(  (abs(df.loc[i]['latitude'] - wlat)*baseLat)**2 + (abs(df.loc[i]['longitude'] - wlon)*baseLon)**2  )

        minDist = df_c.min()
        select_indices = list(np.where(df_c['dist'] == minDist[0]))
        # print(select_indices[0])
        # print(select_indices)
        minDistOffice = df_c.index[select_indices[0]]
        # minDistOffice = --> .name을 이용하여 변경
        print(cnt, '관내국 : ', wofficeName, '\t최기관내국 : ', minDistOffice[0], '\t거리 : ', format(round((minDist[0]/1000),2),','),'Km', "\t==", datetime.datetime.now().isoformat() )
        # print(wofficeName)
        # print(minDist[0])
        # print(minDistOffice[0])

        conn = sqlite3.connect(r'C:\Temp\loc_post.db')
        cursor = conn.cursor()
        sql_update = "UPDATE position SET ? = ?, ? = ? where officeName = ?"
        cursor.execute(sql_update, (str('nearestBranch'),  minDistOffice[0], str('nrstBrDist'), int(minDist[0]), wofficeName ) )
        # sql_update = "UPDATE position SET nearestBranch = ?, nrstBrDist = ? where officeName = ?"
        # cursor.execute(sql_update,(minDistOffice[0], int(minDist[0]), wofficeName))
        conn.commit()
        # update 결과 조회
        # sql = "select * from position where officeName = '이천모가(취)' or officeName = '가남우체국'"
        # cursor.execute(sql)
        # print(cursor.fetchall())


conn.close()
print("*"*10, "end of job", "*"*10)