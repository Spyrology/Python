import sqlite3 as lite
import pandas as pd

con = lite.connect('getting_started.db')

with con:    

    cur = con.cursor()    
    cur.execute("SELECT c.name, c.state FROM cities as c INNER JOIN weather as w ON c.name=w.city WHERE warm_month = 'July';")

    rows = cur.fetchall()
    df = pd.DataFrame(data=rows, index=None)
    myrows = []
    for index, row in df.iterrows():
    	myrows.append(', '.join(row))
    print "The cities that are warmest in July are: " + ', '.join(myrows)
    #print("The cities that are warmest in July are: " + (df.to_string(index=False)))