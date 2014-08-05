#!/usr/bin/env python3

import sqlite3

host     = raw_input('host:')
user     = raw_input('user:')
passwd   = raw_input('passwd:')
dbName   = raw_input('dbName:')
output   = dbName + '.xls'

print( '%s database will be saved to %s.' % ( dbName, output ) )

conn = pymssql.connect( host = host, user = user, password = passwd, database = dbName )
cur = conn.cursor()
cur.execute( 'SELECT * FROM wifi' )
table = cur.fetchall()
for row in table:
	print row
conn.close()
