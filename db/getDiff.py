import sqlite3

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

conn = sqlite3.connect(os.path.join( dir_path,'database.db'))

file1 = open(os.path.join( dir_path,'diff.txt'), 'r', encoding='utf8')
Lines = file1.readlines()

index=0
for line in Lines:
	line = line.replace("\n","")
	if " Pin " not in line:
		parts=line.split(", ")
		firstname=parts[1].strip()
		lastname=parts[0].strip()
		cur = conn.cursor()
		cur.execute("SELECT * FROM pupil where firstname=? AND lastname=? AND inschool=1",(firstname,lastname))
		row = cur.fetchone()
		if row is None:
			print(index,":",firstname,lastname,":",row)
		index=index+1