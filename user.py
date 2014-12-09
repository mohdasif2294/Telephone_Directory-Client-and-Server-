import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:1994/",allow_none=True)

while 1 :
	print "\n======Telephone Directory Admin Database=======\n"
	print "1.Insert an Entry"
	print "2.Delete an Entry"
	print "3.Search in telephone Database"
	print "4.Update an Entry"
	print "5.Exit"
	print "Choose one option :"
	n = raw_input()

	if(n=="1"):
		print "Enter first name :"
		fname =raw_input()
		print "Enter last name :"
		lname =raw_input()
		print "Enter phone number :"
		pno =raw_input()
		print "Enter email id :"
		email =raw_input()
		print "Enter city :"
		city =raw_input()
		print "Enter state :"
		state =raw_input()
		string = proxy.insert_entry(fname,lname,pno,email,city,state)
		if(string=="s"):
			print "Insertion into Telephone Database successful\n"
		else:
			print "Redundant Entry, Unable to process.... try again \n"

	elif(n=="2"):
		print "Enter Phone number"
		pno = raw_input()
		string = proxy.delete_entry(pno)
		if(string=="s"):
			print "Deletion successful .....\n"
		else:
			print "Entry not found... Check details... Try again..\n"

	elif(n=="3"):
		print "Enter first name or telephone you are searching for :"
		key =raw_input()
		results = proxy.search_entry(key)
		if(results=="null"):
			print "No record exist for this first name or telephone !\n"
		else :
			for row in results:
				print "%s %s\t%s\t%s\t%s\t%s"%(row[0],row[1],row[2],row[3],row[4],row[5])

	elif(n=="4"):
		print "Enter telephone number for which update is required :"
		key =raw_input()
		results = proxy.search_entry1(key)
		if(results=="null"):
			print "No such telephone number exist..........! Try again\n"
		else :
			print "Enter first name :"
			fname =raw_input()
			print "Enter last name :"
			lname =raw_input()
			print "Enter email id :"
			email =raw_input()
			print "Enter city :"
			city =raw_input()
			print "Enter state :"
			state =raw_input()
			results=proxy.update_entry(key,fname,lname,email,city,state)
			if results :
				print "Update Done............!\n"
			else :
				print "Error..! Try again.............\n"
				

	elif(n=="5"):
		exit()
	else :
		print "Wrong choice......\n"