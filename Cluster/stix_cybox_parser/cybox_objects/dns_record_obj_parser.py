class DNSQueryObjParser(object):
	_XSI_NS = "DNSRecordObj"
	_XSI_TYPE = "DNSRecordObjectType"

	#elements
	description = ""
	domain_name = ""
	ip_address = ""
	address_class = ""
	entry_type = ""
	record_name = ""
	record_type = ""
	ttl = ""
	flags = ""
	data_length = ""
	record_data = ""

	def __init__(self, description, domain_name, ip_address, address_class
					entry_type, record_name, record_type, ttl, flags
					data_length, record_data):
		self.description = description
		self.domain_name = domain_name
		self.ip_address = ip_address
		self.address_class = address_class
		self.entry_type = entry_type
		self.record_name = record_name
		self.record_type = record_type
		self.ttl = ttl
		self.flags = flags
		self.data_length = data_length
		self.record_data = record_data
	
	#return dns query object elements as a dictionary
	def get_elements(self):
		dns_record_ele_dict = {}
		dns_record_ele_dict['description'] = self.description
		dns_record_ele_dict['domain_name'] = self.domain_name
		dns_record_ele_dict['ip_address'] = self.ip_address
		dns_record_ele_dict['address_class'] = self.address_class
		dns_record_ele_dict['entry_type'] = self.entry_type
		dns_record_ele_dict['record_name'] = self.record_name
		dns_record_ele_dict['record_type'] = self.record_type
		dns_record_ele_dict['ttl'] = self.ttl
		dns_record_ele_dict['flags'] = self.flags
		dns_record_ele_dict['data_length'] = self.data_length
		dns_record_ele_dict['record_data'] = self.record_data
		return dns_record_ele_dict		
	
	#return full dns query object as a dictionary	
	def get_dict(self):
		dns_record_dict = {}
		dns_record_dict['description'] = self.description
		dns_record_dict['domain_name'] = self.domain_name
		dns_record_dict['ip_address'] = self.ip_address
		dns_record_dict['address_class'] = self.address_class
		dns_record_dict['entry_type'] = self.entry_type
		dns_record_dict['record_name'] = self.record_name
		dns_record_dict['record_type'] = self.record_type
		dns_record_dict['ttl'] = self.ttl
		dns_record_dict['flags'] = self.flags
		dns_record_dict['data_length'] = self.data_length
		dns_record_dict['record_data'] = self.record_data
		return dns_record_dict

