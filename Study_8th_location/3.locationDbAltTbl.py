import sqlite3
import pandas as pd
import numpy as numpy

con = sqlite3.connect(r'C:\Users\Administrator\Documents\Github\hello-world\Study_8th_location\loc_post.db')
cursor = con.cursor()
#최기 branch 검색결과 nearestBranch
cursor.execute("ALTER TABLE position Add nearestBranch TEXT NULL")
 
con.commit()
con.close()