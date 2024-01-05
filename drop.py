import sqlite3

con = sqlite3.connect("myfarm.db")
print("OK")
cur = con.cursor()
paper = input("what to toss in the bin?")
bin = f"DROP TABLE {paper};"
cur.execute(bin)