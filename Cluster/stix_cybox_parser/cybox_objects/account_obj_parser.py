class AccountObjParser(object):
	_XSI_NS = "AccountObj"
	_XSI_TYPE = "AccountObjectType"
	
	#attributes
	disabled = ""
	locked_out = ""
	
	#elements
	description = ""
	domain = ""
	
	def __init__(self, disabled, locked_out, description, domain):
		self.description = description
		self.domain = domain
		
	def set_attributes(self, disabled, locked_out):
		self.disabled = disabled
		self.locked_out = locked_out
	
	#return account object attributes as a dictionary
	def get_attributes(self):
		account_attr_dict = {}
		account_attr_dict['disabled'] = self.disabled
		account_attr_dict['locked_out'] = self.locked_out
		return account_attr_dict
	
	#return account object elements as a dictionary
	def get_elements(self):
		account_ele_dict = {}
		account_ele_dict['description'] = self.description
		account_ele_dict['domain'] = self.domain
		return account_ele_dict
	
	#return full account object as a dictionary
	def get_dict(self):
		account_dict = {}
		account_dict['disabled'] = self.disabled
		account_dict['locked_out'] = self.locked_out		
		account_dict['description'] = self.description
		account_dict['domain'] = self.domain
		return account_dict
