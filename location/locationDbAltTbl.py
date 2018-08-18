import sqlite3
import pandas as pd
import numpy as numpy

con = sqlite3.connect(r'C:\Users\sauru\Documents\GitHub\hello-world\location\location.db')
cursor = con.cursor()
cursor.execute("ALTER TABLE position Add nearestBranch TEXT NULL")
 
con.commit()
con.close()