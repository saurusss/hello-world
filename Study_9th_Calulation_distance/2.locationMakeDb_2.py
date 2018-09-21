import sqlite3
import pandas as pd
import numpy as numpy
import os


dbPath = os.getenv('homedrive') + os.getenv('homepath') + r"\OneDrive\Documents\KOC\180807_우체국\작업관리정보\주소"
# dbpath = os.getenv('homedrive') + os.getenv('homepath') + r"\Documents\Github\hello-world\Study_9th_Calulation_distance"

# conn = sqlite3.connect(dbPath + r'\loc_post.db')

excelPath = os.getenv('homedrive') + os.getenv('homepath') + r"\OneDrive\Documents\KOC\180807_우체국\작업관리정보\주소"

loc = pd.read_excel(excelPath + r'\nrstBR_180921.xlsx')
# loc = pd.read_excel(r'C:\temp\loc_180826.xlsx')
# loc = pd.read_excel(r'C:\temp\loc_180825_2.xlsx')
# loc = pd.read_excel(r'C:\temp\loc_180825_1.xlsx')
# loc = pd.read_excel(r'C:\temp\loc_180825.xlsx')
print(loc)

conn = sqlite3.connect(dbPath + r'\loc_post.db')
cursor = conn.cursor()
loc.to_sql('position', conn)

# cursor.execute("CREATE TABLE position(officeName text, addr text, latitude text, longitude text )")
# for i in loc:
#     cursor.execute("INSERT INTO position VALUES (loc.mgmtNum[i], loc.buildName[i], loc.addr[i], loc.latitude[i], loc.longitude[i])")

conn.commit()
conn.close()