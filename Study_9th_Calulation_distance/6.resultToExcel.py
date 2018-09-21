import pandas as pd
import numpy as np
import sqlite3
import math
import os

print("*"*10, "start of job", "*"*10)

dbPath = os.getenv('homedrive') + os.getenv('homepath') + r"\OneDrive\Documents\KOC\180807_우체국\작업관리정보\주소"
conn = sqlite3.connect(dbPath + r'\loc_post.db')
# conn = sqlite3.connect(r'C:\Temp\loc_post.db')

df = pd.read_sql_query("select * from position ", conn)

df.to_csv(dbPath + r'\nrstBR_180921.csv', mode='w')
# df.to_csv('c:\\TEMP\\nrstBR_180912.csv', mode='w')

print("*"*10, " end of job ", "*"*10)