import sqlite3
import pandas as pd
import numpy as numpy

con = sqlite3.connect(r'C:\Users\sauru\Documents\GitHub\hello-world\location\location.db')
cursor = con.cursor()
#최기 branch 검색결과 nearestBranch
cursor.execute("ALTER TABLE position Add nearestBranch TEXT NULL")
 
con.commit()
con.close()