import pandas as pd
import numpy as numpy
import sqlite3
 
conn = sqlite3.connect(r'C:\temp\loc_post.db')
cursor = conn.cursor()

PDB = cursor.execute("SELECT * FROM position where nearestBranch is null" )

rows = cursor.fetchall()
for row in rows:
        print(row)

conn.commit()
conn.close()