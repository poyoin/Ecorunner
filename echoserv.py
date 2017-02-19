#!/usr/bin/env python

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
import MySQLdb

### Protocol Implementation

# This is just about the simplest possible protocol
class Echo(Protocol):

    def dataReceived(self, data):
	db = MySQLdb.connect("localhost","root","reverse", "mydata")	
	cursor = db.cursor()
	db.autocommit(True)
	
        """
        As soon as any data is received, write it back.
        """
        self.transport.write(data)

	datastring = str(data)
	print datastring 
	cursor.execute("INSERT INTO Temperature (TEMP) VALUES (%s)", ([datastring]))

	
def makeTable():
	#Connect to database
	db = MySQLdb.connect("localhost","root","reverse", "mydata")	
	cursor = db.cursor()
	db.autocommit(True)

	# Drop table if it already exist using execute() method.
	cursor.execute("DROP TABLE IF EXISTS Temperature")

	#Make a table in the database
	sql = """CREATE TABLE Temperature (
         TIME INT(6) AUTO_INCREMENT PRIMARY KEY,
         TEMP VARCHAR(20) )"""

	cursor.execute(sql)
 
def main():
	makeTable()
	f = Factory()
	f.protocol = Echo
	reactor.listenTCP(12345, f)
	reactor.run()

if __name__ == '__main__':
	main()
