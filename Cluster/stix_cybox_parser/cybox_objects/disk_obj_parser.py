class DiskObjParser(object):
	_XSI_NS = "DiskObj"
	_XSI_TYPE = "DiskObjectType"
	
	#elements
	disk_name = ""
	disk_size = ""
	free_space = ""
	partition_list = ""
	type = ""

	def __init__(self, disk_name, disk_size, free_space, partition_list, type):
		self.disk_name = disk_name
		self.disk_size = disk_size
		self.free_space = free_space
		self.partition_list = partition_list
		self.type = type
		
	#return disk object elements as a dictionary
	def get_elements(self):
		disk_ele_dict = {}
		disk_ele_dict['disk_name'] = self.disk_name
		disk_ele_dict['disk_size'] = self.disk_size
		disk_ele_dict['free_space'] = self.free_space
		disk_ele_dict['partition_list'] = self.partition_list
		disk_ele_dict['type'] = self.type
		return disk_ele_dict		
	
	#return full disk object as a dictionary	
	def get_dict(self):
		disk_dict = {}
		disk_dict['disk_name'] = self.disk_name
		disk_dict['disk_size'] = self.disk_size
		disk_dict['free_space'] = self.free_space
		disk_dict['partition_list'] = self.partition_list
		disk_dict['type'] = self.type
		return disk_dict	

