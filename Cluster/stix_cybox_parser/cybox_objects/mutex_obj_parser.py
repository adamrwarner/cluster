class MutexObjParser(object):
	_XSI_NS = "MutexObj"
	_XSI_TYPE = "MutexObjectType"

	#attributes
	named = ""
	
	#elements
	name = ""

	def __init__(self, name):
		self.name = name
		
	def set_attributes(self, named):
		self.named = named
	
	#return mutex object attributes as a dictionary
	def get_attributes(self):
		mutex_attr_dict = {}
		mutex_attr_dict['named'] = self.named
		return mutex_attr_dict
	
	#return mutex object elements as a dictionary
	def get_elements(self):
		mutex_ele_dict = {}
		mutex_ele_dict['name'] = self.name
		return mutex_ele_dict		
	
	#return full mutex object as a dictionary	
	def get_dict(self):
		mutex_dict = {}
		mutex_dict['named'] = self.named
		mutex_dict['name'] = self.name
		return mutex_dict	

