class MemoryObjParser(object):
	_XSI_NS = "MemoryObj"
	_XSI_TYPE = "MemoryObjectType"

	#attributes
	is_injected = ""
	is_mapped = ""
	is_protected = ""
	
	#elements
	hashes = ""
	name = ""
	region_size = ""
	region_start_address = ""
	extracted_features = ""	

	def __init__(self, hashes, name, region_size, region_start_address, 
					extracted_features):
		self.hashes = hashes
		self.name = name
		self.region_size = region_size
		self.region_start_address = region_start_address
		self.extracted_features = extracted_features		
		
	def set_attributes(self, is_injected, is_mapped, is_protected):
		self.is_injected = is_injected
		self.is_mapped = is_mapped
		self.is_protected = is_protected
	
	#return memory object attributes as a dictionary
	def get_attributes(self):
		memory_attr_dict = {}
		memory_attr_dict['is_injected'] = self.is_injected
		memory_attr_dict['is_mapped'] = self.is_mapped
		memory_attr_dict['is_protected'] = self.is_protected
		return memory_attr_dict
	
	#return memory object elements as a dictionary
	def get_elements(self):
		memory_ele_dict = {}
		memory_ele_dict['hashes'] = self.hashes
		memory_ele_dict['name'] = self.name
		memory_ele_dict['region_size'] = self.region_size
		memory_ele_dict['region_start_address'] = self.region_start_address
		memory_ele_dict['extracted_features'] = self.extracted_features
		return memory_ele_dict		
	
	#return full memory object as a dictionary	
	def get_dict(self):
		memory_dict = {}
		memory_dict['is_injected'] = self.is_injected
		memory_dict['is_mapped'] = self.is_mapped
		memory_dict['is_protected'] = self.is_protected		
		memory_dict['hashes'] = self.hashes
		memory_dict['name'] = self.name
		memory_dict['region_size'] = self.region_size
		memory_dict['region_start_address'] = self.region_start_address
		memory_dict['extracted_features'] = self.extracted_features
		return memory_dict	

