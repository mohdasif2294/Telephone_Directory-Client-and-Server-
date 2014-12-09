import MySQLdb
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

db = MySQLdb.connect("localhost","root","","phonebook" )
cursor = db.cursor()

def insert_entry(fname,lname,pno,email,city,state) :
	sql = """insert into Phonebook
			 values ('%s','%s','%s','%s','%s','%s');"""%(fname,lname,pno,email,city,state)
	try :
		cursor.execute(sql)
		db.commit()
		return "s"
	except :
		db.rollback()
		return "u"

def delete_entry(pno) :
	sql = """select fname from Phonebook where pno='%s';"""%(pno)

	cursor.execute(sql)
	results = cursor.fetchall()
	
	if results :
 		sql = """delete from Phonebook
		where pno='%s';"""%(pno)
		try :
			cursor.execute(sql)
			db.commit()
			return "s"
		except :
			db.rollback()
	    	return "u"
	else :
		return "f"		

	

def search_entry(string) :
	sql = """select * from Phonebook
			 where fname = '%s' or pno = '%s';"""%(string,string)
	try :
		cursor.execute(sql)
		results = cursor.fetchall()

		if results :
			return results
		else :
			return "null"	
	except :
		return "null"

def search_entry1(string) :
	sql = """select * from Phonebook where pno = '%s';"""%(string)
	
	try:
		cursor.execute(sql)
		results = cursor.fetchall()		

		if results :
			return results
			
		else :
			return "null"	
	except :
		return null

def update_entry(key,fname,lname,email,city,state) :
	sql = """select * from Phonebook
			 where pno = '%s';"""%(key)
	try :

		cursor.execute(sql)
		results = cursor.fetchall()

		if results :
			sql = """update Phonebook set fname='%s' , lname='%s', email='%s', city='%s', state='%s' where pno = '%s';"""%(fname,lname,email,city,state,key)
			cursor.execute(sql)
			db.commit()
			return "s"
		else :
			return "null"	
	except :
		db.rollback()
		return "null"

server = SimpleXMLRPCServer(("localhost", 1994),
                            allow_none=True)
server.register_function(insert_entry)
server.register_function(delete_entry)
server.register_function(search_entry)
server.register_function(search_entry1)
server.register_function(update_entry)
server.serve_forever()