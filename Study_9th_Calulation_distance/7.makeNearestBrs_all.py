# 전체 관내점 작업 수행
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

#단위당 거리(미터)
baseLat = 110979.309    # 검증 필요
baseLon = 88907.949     # 검증 필요

cnt = 0

for i in df.index:
        cnt += 1
        # 작업용 DF 설정
        wdf =  pd.DataFrame(columns=['officeName','dist']).set_index('officeName')
        wofficeName = df.loc[i].name
        wlat = df.loc[wofficeName]['latitude']
        wlon = df.loc[wofficeName]['longitude']
        # print(wofficeName, wlat, wlon)

        for j in df.index:
                wdf.loc[j] = math.sqrt(  (abs(df.loc[j]['latitude'] - wlat)*baseLat)**2 + \
                 (abs(df.loc[j]['longitude'] - wlon)*baseLon)**2  )
                # wdf = df.sort_index(ascending=False)
                wdf = wdf.sort_values(by='dist')

                
        selectedBr = []
        selectedDist = []
        
        for k in wdf.index[1:4]:
                selectedBr.append(k)
                selectedDist.append(int(wdf.loc[k]['dist']))


        conn = sqlite3.connect(r'C:\Temp\loc_post.db')
        cursor = conn.cursor()
        # sql_updBr = 'nBr' + str(cntt)
        # sql_updDist = 'nDist' + str(cntt)
        
        sql_update = "UPDATE position SET  nBr1 = ?, nDist1 = ?, nBr2 = ?, nDist2 = ?, nBr3 = ?, nDist3 = ? \
                        where officeName = ?"
        cursor.execute(sql_update, (selectedBr[0], selectedDist[0], selectedBr[1], selectedDist[1], selectedBr[2], selectedDist[2], wofficeName) )
        print( cnt,'\t*** 관내국:', wofficeName, 
                        '\t1st', selectedBr[0], format(round((selectedDist[0]/1000),2),','),'Km',
                        '\t2nd', selectedBr[1], format(round((selectedDist[1]/1000),2),','),'Km', 
                        '\t3rd', selectedBr[2], format(round((selectedDist[2]/1000),2),','),'Km'  
                        '\t===', datetime.datetime.now().isoformat() ) 
        conn.commit()   
                
conn.close()
print("*"*10, "end of job", "*"*10)