import MySQLdb as mdb

con = mdb.connect('fintegro.ca', 'fintegro', 'fintegro2014', 'basilisk_db');

with con: 

    cur = con.cursor()
    cur.execute("SELECT * FROM university WHERE address = 'Zp'")
    
    rows = cur.fetchall()

    for row in rows:
        print row