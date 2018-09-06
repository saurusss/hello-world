import sqlite3
import pandas as pd
import numpy as numpy
loc = pd.read_excel(r'C:\temp\2018년_작업점포_좌표_강원충청_180906.xlsx')
#loc = pd.read_excel(r'C:\temp\2018년_작업점포_좌표_서울경기강원충청_180906.xlsx')
#loc = pd.read_excel(r'C:\temp\loc_180826.xlsx')
# loc = pd.read_excel(r'C:\temp\loc_180825_2.xlsx')
# loc = pd.read_excel(r'C:\temp\loc_180825_1.xlsx')
# loc = pd.read_excel(r'C:\temp\loc_180825.xlsx')
print(loc)

con = sqlite3.connect(r'C:\temp\loc_post.db')
cursor = con.cursor()
loc.to_sql('position', con)

# cursor.execute("CREATE TABLE position(officeName text, addr text, latitude text, longitude text )")
# for i in loc:
#     cursor.execute("INSERT INTO position VALUES (loc.mgmtNum[i], loc.buildName[i], loc.addr[i], loc.latitude[i], loc.longitude[i])")

con.commit()
con.close()