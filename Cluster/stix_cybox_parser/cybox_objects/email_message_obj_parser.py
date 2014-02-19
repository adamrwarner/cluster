class EmailMessageObjParser(object):
	_XSI_NS = "EmailMessageObj"
	_XSI_TYPE = "EmailMessageObjectType"

	#elements
	header = ""
	email_server = ""
	raw_body = ""
	raw_header = ""
	attachments = ""
	links = ""

	def __init__(self, header, email_server, raw_body, raw_header
					attachments, links):
		self.header = header
		self.email_server = email_server
		self.raw_body = raw_body
		self.raw_header = raw_header
		self.attachments = attachments
		self.links = links
	
	#return email message object elements as a dictionary
	def get_elements(self):
		email_message_ele_dict = {}
		email_message_ele_dict['header'] = self.header
		email_message_ele_dict['email_server'] = self.email_server
		email_message_ele_dict['raw_body'] = self.raw_body
		email_message_ele_dict['raw_header'] = self.raw_header
		email_message_ele_dict['attachments'] = self.attachments
		email_message_ele_dict['links'] = self.links
		return email_message_ele_dict		
	
	#return full email message object as a dictionary	
	def get_dict(self):
		email_message_dict = {}
		email_message_dict['header'] = self.header
		email_message_dict['email_server'] = self.email_server
		email_message_dict['raw_body'] = self.raw_body
		email_message_dict['raw_header'] = self.raw_header
		email_message_dict['attachments'] = self.attachments
		email_message_dict['links'] = self.links
		return email_message_dict	

