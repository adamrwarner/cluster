class LibraryObjParser(object):
	_XSI_NS = "LibraryObj"
	_XSI_TYPE = "LibraryObjectType"

	#attributes
	
	#elements
	name = ""
	path = ""
	size = ""
	type = ""
	version = ""
	base_address = ""
	extracted_features = ""

	def __init__(self, name, path, size, type, version, base_address, extracted_features):
		self.name = name
		self.path = path
		self.size = size
		self.type = type
		self.version = version
		self.base_address = base_address
		self.extracted_features = extracted_features		
	
	#return library object elements as a dictionary
	def get_elements(self):
		library_ele_dict = {}
		library_ele_dict['name'] = self.name
		library_ele_dict['path'] = self.path
		library_ele_dict['size'] = self.size
		library_ele_dict['type'] = self.type
		library_ele_dict['version'] = self.version
		library_ele_dict['base_address'] = self.base_address
		library_ele_dict['extracted_features'] = self.extracted_features
		return library_ele_dict		
	
	#return full library object as a dictionary	
	def get_dict(self):
		library_dict = {}
		library_dict['name'] = self.name
		library_dict['path'] = self.path
		library_dict['size'] = self.size
		library_dict['type'] = self.type
		library_dict['version'] = self.version
		library_dict['base_address'] = self.base_address
		library_dict['extracted_features'] = self.extracted_features
		return library_dict

