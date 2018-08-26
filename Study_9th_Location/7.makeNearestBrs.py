import pandas as pd
import numpy as np
import sqlite3
import math
import datetime
 

print("*"*10, "start of job", "*"*10)
conn = sqlite3.connect(r'C:\Temp\loc_post.db')
df = pd.read_sql_query("select * from position", conn)
conn.close()


# 입력 정보 정리
del df['index']
df = df.set_index('officeName')
# df = df.sort_index(ascending=False)
# df = df.sort_values(by='address',ascending=False)

#단위당 거리(미터)
baseLat = 110979.309    # 검증 필요
baseLon = 88907.949     # 검증 필요

for i in range(0, len(df)):
        # 작업용 DF 설정
        wdf =  pd.DataFrame(columns=['officeName','dist']).set_index('officeName')
        wofficeName = df.index[i]
        wlat = df.loc[wofficeName]['latitude']
        wlon = df.loc[wofficeName]['longitude']
        # print(wofficeName, wlat, wlon)


        for j in df.index:
                wdf.loc[j] = math.sqrt(  (abs(df.loc[j]['latitude'] - wlat)*baseLat)**2 + (abs(df.loc[j]['longitude'] - wlon)*baseLon)**2  )
                wdf = wdf.sort_values(by='dist')

                conn = sqlite3.connect(r'C:\Temp\loc_post.db')
                cursor = conn.cursor()
                cntt = 0
                for k in wdf.index[1:4]:
                        cntt += 1
                        sql_updBr = 'nBr' + str(cntt)
                        sql_updDist = 'nDist' + str(cntt)
                        sql_update = "UPDATE position SET  ? = ?, ? = ? where officeName = ?"
                        cursor.execute(sql_update, (str(sql_updBr), k, str(sql_updDist), int(wdf.loc[k]['dist']), wofficeName) )
                        print( '관내국:', wofficeName, '\t'+sql_updBr+':', k, '\t'+sql_updDist+':', format(round((wdf.loc[k]['dist']/1000),2),','),'Km',"\t==  ", datetime.datetime.now().isoformat() )
                conn.commit()   
                
conn.close()
print("*"*10, "end of job", "*"*10)