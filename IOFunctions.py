import yaml

def load_yaml(file_path):
	f = open(file_path, "r")
	yaml_data = yaml.load(f)
	f.close()


def write_yaml(file_path,data):
	f = open(file_path,"a")
	yaml.dump(data,f,default_flow_style=False)
	f.close()
