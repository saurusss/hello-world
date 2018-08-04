import sqlite3
con = sqlite3.connect("c:/temp/kospi.db")
cursor = con.cursor()

cursor.execute("CREATE TABLE kakao(Date text, Open int, High int, Low int, Closing int, Volumn int)")
cursor.execute("INSERT INTO kakao VALUES('16.06.03', 97000, 98600, 96900, 98000, 321405)")
cursor.execute("INSERT INTO kakao VALUES('16.06.02', 99000, 99300, 96300, 97500, 556790)")

con.commit()
con.close()