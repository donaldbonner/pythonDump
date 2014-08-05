#!/usr/bin/env python3

import sqlite3

host     = '209.114.51.205'
user     = 'development'
passwd   = 'Fqrb4jDARGwp7Y'
dbName   = 'vw_dev'
output   = dbName + '.xls'

print( '%s database will be saved to %s.' % ( dbName, output ) )

conn = pymssql.connect( host = host, user = user, password = passwd, database = dbName )
cur = conn.cursor()
cur.execute( 'SELECT * FROM wifi' )
table = cur.fetchall()
for row in table:
	print row
conn.close()