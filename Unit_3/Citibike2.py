import time
from dateutil.parser import parse
import collections
import sqlite3 as lite
import requests
import datetime

con = lite.connect('citi_bike.db')
cur = con.cursor()
cur.execute("delete from available_bikes")

for i in range(60):
		print("Requesting data...")
		r = requests.get('http://www.citibikenyc.com/stations/json')
		exec_time = parse(r.json()['executionTime'])
		# time_stamp = (exec_time - datetime.datetime(1970,1,1)).total_seconds()

		cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time,))

		for station in r.json()['stationBeanList']:
			cur.execute("UPDATE available_bikes SET _" + str(station['id']) + " = ? WHERE execution_time = ?", (station['availableBikes'], exec_time))
		con.commit()

		print("Done.")
		time.sleep(60)

con.close() #close the database connection when done