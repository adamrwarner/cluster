class APIObjParser(object):
	_XSI_NS = "APIObj"
	_XSI_TYPE = "APIObjectType"
	
	#elements
	description = ""
	function_name = ""
	normalized_function_name = ""
	address = ""
	
	def __init__(self, description, function_name, normalized_function_name, address):
		self.description = description
		self.function_name = function_name
		self.normalized_function_name = normalized_function_name
		self.address = address
	
	#return api object elements as a dictionary
	def get_ele_dict(self):
		api_dict = {}
		api_dict['description'] = self.description
		api_dict['function_name'] = self.function_name
		api_dict['normalized_function_name'] = self.normalized_function_name
		api_dict['address'] = self.address
		return api_dict
	
	#return api object as a dictionary
	def get_dict(self):
		api_dict = {}
		api_dict['description'] = self.description
		api_dict['function_name'] = self.function_name
		api_dict['normalized_function_name'] = self.normalized_function_name
		api_dict['address'] = self.address
		return api_dict
