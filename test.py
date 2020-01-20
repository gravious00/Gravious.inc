import sqlite3
import time
import datetime

conn = sqlite3.connect('/home/gravious/SIH/Gravious.inc/ANPR')
c = conn.cursor()

def read_from_db():
	c.execute('SELECT * FROM Residents WHERE name="chatak"')

c.close()
conn.close()