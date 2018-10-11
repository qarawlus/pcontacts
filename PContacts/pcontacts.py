# Python Contacts using YAML
# Developed by Haydar Qarawlus 
# V1.0dev
# Main executable file 
###########################################

# Import of the Argument Parser and Contact module

import argparse
import PContacts.IOFunctions as PContacts


if __name__ == '__main__':
  
  # YAML File 
	file = "../data/contacts.yaml"
  
  # Initilization of Argument Parser and setting up arguments 
	parser = argparse.ArgumentParser(description="Python YAML Address Book")
	parser.add_argument("--show", "-s", help="Show details for a contact")
	parser.add_argument("--add", "-a", help="Add a new contact")
	parser.add_argument("--number", "-n", help="Phone number")
	parser.add_argument("--email", "-e", help="Email address")
	parser.add_argument("--list", "-l", help="List all contacts", action="store_true")
	parser.add_argument("--file", "-f", help="Use a different YAML file")
	args = parser.parse_args()
  
  # Loading the yaml file
	contacts = PContacts.load_yaml(file)
  
  
  # Setting actions and output based on user input
	if args.file!=None:
		file = args.file

	if args.list==True:
		print PContacts.list(contacts)
	
	elif args.add!=None and args.number!=None and args.email!=None and args.show==None:
		PContacts.add(args.add,args.number,args.email,file)
		print("Contact was added successfully!")
	
	elif args.show!=None: 
		print PContacts.show(args.show,contacts)
	else: 
		print ("Python YAML Address Book.\r\nIncorrect use, for options, run PContacts -h or --help.")
