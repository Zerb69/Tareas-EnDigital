import MySQLdb

db=MySQLdb.connect(password="", db="hospital")
c=db.cursor()
c.execute("SELECT * FROM pacientes")
c.close()
db.close()
