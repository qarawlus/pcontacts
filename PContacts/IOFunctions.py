import yaml

def load_yaml(file_path):
	f = open(file_path, "r")
	yaml_data = yaml.load(f)
	f.close()
	return yaml_data

def write_yaml(file_path,data):
	f = open(file_path,"a")
	yaml.dump(data,f,default_flow_style=False)
	f.close()

def show(name,data):
	if name in data.keys():
		output = "Name: "+name+"\n\rEmail: "+data[name]['EMAIL']+"\r\nPhone: "+data[name]['PHONE']
	else:
		output = "Contact not found!"

	return output


def add(name,number,email,file):
	contact = {name:{"PHONE": number, "EMAIL": email}}
	write_yaml(file,contact)


def list(data):
	counter = 1
	output = ""
	for contact,details in data.items():
		output+="Contact #"+str(counter)+":\r\n\tName:"+contact+"\r\n\tEmail: "+details['EMAIL']+"\r\n\tPhone Number: "+details['PHONE']+"\r\n"
		counter+=1
	return output
