import sqlite3
import time
import datetime
import requests
import simplejson

'''conn = sqlite3.connect('/home/gravious/SIH/Gravious.inc/ANPR')
c = conn.cursor()

def read_from_db():
	c.execute('SELECT * FROM Residents WHERE name="chatak"')

c.close()
conn.close()'''

URL= 'http://127.0.0.1:8000/api/'
r = requests.get(url = URL) 
data=r.json
print (data)