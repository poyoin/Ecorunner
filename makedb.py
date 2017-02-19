import MySQLdb

#Connect to database
db = MySQLdb.connect("localhost","root","reverse", "mydata")	
cursor = db.cursor()
db.autocommit(True)

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS Temperature")

#Make a table in the database
sql = """CREATE TABLE Temperature (
         TIME INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
         TEMP INT(6) )"""

cursor.execute(sql)

cursor.execute("INSERT INTO Temperature (TEMP) VALUES (4)")
cursor.execute("INSERT INTO Temperature (TEMP) VALUES (5)")
