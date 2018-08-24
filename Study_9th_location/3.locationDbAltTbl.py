import sqlite3
import pandas as pd
import numpy as numpy

conn = sqlite3.connect(r'C:\temp\loc_post.db')
cursor = conn.cursor()
#최기 branch 검색결과 nearestBranch
cursor.execute("ALTER TABLE position Add nearestBranch TEXT NULL")
 
conn.commit()
conn.close()