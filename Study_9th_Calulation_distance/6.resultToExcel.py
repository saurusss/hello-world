import pandas as pd
import numpy as np
import sqlite3
import math

print("*"*10, "start of job", "*"*10)
conn = sqlite3.connect(r'C:\Temp\loc_post.db')
df = pd.read_sql_query("select * from position ", conn)

df.to_csv('c:\\TEMP\\nrstBR_180912.csv', mode='w')
print("*"*10, " end of job ", "*"*10)