class AddressObjParser(object):
    _XSI_NS = 'AddressObj'
    _XSI_TYPE = 'AddressObjectType'

	#attributes
	category = ""
    is_destination = ""
    is_source = ""
	
	#elements
    address_value = ""
    vlan_name = ""
    vlan_num = ""

    def __init__(self, address_value, vlan_name, vlan_num):
		self.address_value = address_value
		self.vlan_name = vlan_name
		self.vlan_num = vlan_num
		
	def set_attributes(self, category, is_destination, is_source):
		self.category = category
		self.is_destination = is_destination
		self.is_source = is_source
	
	#return address object attributes as a dictionary
	def get_attributes(self):
		address_attr_dict = {}
		address_attr_dict['category'] = self.category
		address_attr_dict['is_destination'] = self.is_destination
		address_attr_dict['is_source'] = self.is_source
		return address_attr_dict
	
	#return address object elements as a dictionary
	def get_elements(self):
		address_ele_dict = {}
		address_ele_dict['address_value'] = self.address_value
		address_ele_dict['vlan_name'] = self.vlan_name
		address_ele_dict['vlan_num'] = self.vlan_num
		return address_ele_dict		
	
	#return full address object as a dictionary	
	def get_dict(self):
		address_dict = {}
		address_dict['address_value'] = self.address_value
		address_dict['category'] = self.category
		address_dict['is_destination'] = self.is_destination
		address_dict['is_source'] = self.is_source
		address_dict['vlan_name'] = self.vlan_name
		address_dict['vlan_num'] = self.vlan_num
		return address_dict
