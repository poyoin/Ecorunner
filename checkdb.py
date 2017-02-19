import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","reverse","mydata" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM Temperature"

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      temp = row[1]
      # Now print fetched result
      print "id=%s,temp=%s" % \
             (id, temp)
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()
