import sqlite3
import pandas as pd
import numpy as numpy
loc = pd.read_excel(r'C:\temp\loc_180910.xlsx')

print(loc)

con = sqlite3.connect(r'C:\temp\loc_post.db')
cursor = con.cursor()
loc.to_sql('position', con)

# cursor.execute("CREATE TABLE position(officeName text, addr text, latitude text, longitude text )")
# for i in loc:
#     cursor.execute("INSERT INTO position VALUES (loc.mgmtNum[i], loc.buildName[i], loc.addr[i], loc.latitude[i], loc.longitude[i])")

con.commit()
con.close()