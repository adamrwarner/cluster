class ArtifactObjParser(object):
	_XSI_NS = "ArtifactObj"
	_XSI_TYPE = "ArtifactObjectType"

	#attributes
	type = ""
	content_type = ""
	content_type_version = ""
	suspected_malicious = ""
	
	#elements
	hashes = ""
	packaging = ""

	def __init__(self, hashes, packaging):
		self.hashes = hashes
		self.packaging = packaging
		
	def set_attributes(self, type, content_type, content_type_version, suspected_malicious):
		self.type = type
		self.content_type = content_type
		self.content_type_version = content_type_version
		self.suspected_malicious = suspected_malicious
	
	#return artifact object attributes as a dictionary
	def get_attributes(self):
		artifact_attr_dict = {}
		artifact_attr_dict['hashes'] = self.hashes
		artifact_attr_dict['packaging'] = self.packaging
		return artifact_attr_dict
	
	#return artifact object elements as a dictionary
	def get_elements(self):
		artifact_ele_dict = {}
		artifact_ele_dict['type'] = self.type
		artifact_ele_dict['content_type'] = self.content_type
		artifact_ele_dict['content_type_version'] = self.content_type_version
		artifact_ele_dict['suspected_malicious'] = self.suspected_malicious
		return artifact_ele_dict		
	
	#return full artifact object as a dictionary	
	def get_dict(self):
		artifact_dict = {}
		artifact_dict['hashes'] = self.hashes
		artifact_dict['packaging'] = self.packaging
		artifact_dict['type'] = self.type
		artifact_dict['content_type'] = self.content_type
		artifact_dict['content_type_version'] = self.content_type_version
		artifact_dict['suspected_malicious'] = self.suspected_malicious
		return artifact_dict

