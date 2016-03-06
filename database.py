import sqlite3 as lite
import pandas as pd

con = lite.connect('getting_started.db')

with con:    

    cur = con.cursor()    
    cur.execute("SELECT name FROM cities INNER JOIN weather ON name=city WHERE warm_month = 'July';")

    rows = cur.fetchall()
    df = pd.DataFrame(data=rows, index=None)
    print("The cities that are warmest in July are: " + (df.to_string(index=False)))