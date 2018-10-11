# Import of PyYAML Package
import yaml

# Loading YAML Data File, file mode is "R"
def load_yaml(file_path):
	f = open(file_path, "r")
	yaml_data = yaml.load(f)
	f.close()
	return yaml_data
# Writing to YAML file, file mode is "A" to append to, and not erase the file
def write_yaml(file_path,data):
	f = open(file_path,"a")
	yaml.dump(data,f,default_flow_style=False)
	f.close()

# Show the details of a contact in a formatted ouput
def show(name,data):
	if name in data.keys():
		output = "Name: "+name+"\n\rEmail: "+data[name]['EMAIL']+"\r\nPhone: "+data[name]['PHONE']
	else:
		output = "Contact not found!"

	return output

# Add a contact to the YAML file
def add(name,number,email,file):
	contact = {name:{"PHONE": number, "EMAIL": email}}
	write_yaml(file,contact)

# Show all contacts in a formatted output
def list(data):
	counter = 1
	output = ""
	if data!=None:
		for contact,details in data.items():
			output+="Contact #"+str(counter)+":\r\n\tName:"+contact+"\r\n\tEmail: "+details['EMAIL']+"\r\n\tPhone Number: "+details['PHONE']+"\r\n"
			counter+=1
	else:
		output="There are no contacts available."

	return output
