class DNSQueryObjParser(object):
	_XSI_NS = "DNSQueryObj"
	_XSI_TYPE = "DNSQueryObjectType"

	#attributes
	successful = ""

	#elements
	question = ""
	answer_resource_records = ""
	authority_resource_records = ""
	additional_records = ""
	date_ran = ""
	service_used = ""

	def __init__(self, question, answer_resource_records, 
				authority_resource_records, additional_records
				date_ran, service_used):
		self.question = question
		self.answer_resource_records = answer_resource_records
		self.authority_resource_records = authority_resource_records
		self.additional_records = additional_records
		self.date_ran = date_ran
		self.service_used = service_used
		
	def set_attributes(self, successful):
		self.successful = successful
	
	#return dns query object attributes as a dictionary
	def get_attributes(self):
		dns_query_attr_dict = {}
		dns_query_attr_dict['successful'] = self.successful
		return dns_query_attr_dict
	
	#return dns query object elements as a dictionary
	def get_elements(self):
		dns_query_ele_dict = {}
		dns_query_ele_dict['question'] = self.question
		dns_query_ele_dict['answer_resource_records'] = self.answer_resource_records
		dns_query_ele_dict['authority_resource_records'] = self.authority_resource_records
		dns_query_ele_dict['additional_records'] = self.additional_records
		dns_query_ele_dict['date_ran'] = self.date_ran
		dns_query_ele_dict['service_used'] = self.service_used
		return dns_query_ele_dict		
	
	#return full dns query object as a dictionary	
	def get_dict(self):
		dns_query_dict = {}
		dns_query_dict['successful'] = self.successful
		dns_query_dict['question'] = self.question
		dns_query_dict['answer_resource_records'] = self.answer_resource_records
		dns_query_dict['authority_resource_records'] = self.authority_resource_records
		dns_query_dict['additional_records'] = self.additional_records
		dns_query_dict['date_ran'] = self.date_ran
		dns_query_dict['service_used'] = self.service_used
		return dns_query_dict	

