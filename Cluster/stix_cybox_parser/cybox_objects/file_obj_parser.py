class FileObjParser(object):
	_XSI_NS = "FileObj"
	_XSI_TYPE = "FileObjectType"

	#attributes
	is_packed = ""
	
	#elements
	file_name = ""
	file_path = ""
	device_path = ""
	full_path = ""
	file_extension = ""
	size_in_bytes = ""
	magic_number = ""
	file_format = ""
	hashes = ""
	digital_signature = ""
	modified_time = ""
	accessed_time = ""
	created_time = ""
	file_attributes_list = ""
	permissions = ""
	user_owner = ""
	packer_list = ""
	peak_entropy = ""
	sym_links = ""
	byte_runs = ""
	extracted_features = ""

	def __init__(self, file_name, file_path, device_path, full_path, file_extension,
					size_in_bytes, magic_number, file_format, hashes, digital_signature,
					modified_time, accessed_time, created_time, file_attributes_list,
					permissions, user_owner, packer_list, peak_entropy, sym_links
					byte_runs, extracted_features):
		self.file_name = file_name
		self.file_path = file_path
		self.device_path = device_path
		self.full_path = full_path
		self.file_extension = file_extension
		self.size_in_bytes = size_in_bytes
		self.magic_number = magic_number
		self.file_format = file_format
		self.hashes = hashes
		self.digital_signature = digital_signature
		self.modified_time = modified_time
		self.accessed_time = accessed_time
		self.created_time = created_time
		self.file_attributes_list = file_attributes_list
		self.permissions = permissions
		self.user_owner = user_owner
		self.packer_list = packer_list
		self.peak_entropy = peak_entropy
		self.sym_links = sym_links
		self.byte_runs = byte_runs
		self.extracted_features = extracted_features
		
	def set_attributes(self, is_packed):
		self.is_packed = is_packed
	
	#return file object attributes as a dictionary
	def get_attributes(self):
		file_attr_dict = {}
		file_attr_dict['is_packed'] = self.is_packed
		return file_attr_dict
	
	#return file object elements as a dictionary
	def get_elements(self):
		file_ele_dict = {}
		file_ele_dict['file_name'] = self.file_name
		file_ele_dict['file_path'] = self.file_path
		file_ele_dict['device_path'] = self.device_path
		file_ele_dict['full_path'] = self.full_path
		file_ele_dict['file_extension'] = self.file_extension
		file_ele_dict['size_in_bytes'] = self.size_in_bytes
		file_ele_dict['magic_number'] = self.magic_number
		file_ele_dict['file_format'] = self.file_format
		file_ele_dict['hashes'] = self.hashes
		file_ele_dict['digital_signature'] = self.digital_signature
		file_ele_dict['modified_time'] = self.modified_time
		file_ele_dict['accessed_time'] = self.accessed_time
		file_ele_dict['created_time'] = self.created_time
		file_ele_dict['file_attributes_list'] = self.file_attributes_list
		file_ele_dict['permissions'] = self.permissions
		file_ele_dict['user_owner'] = self.user_owner	
		file_ele_dict['packer_list'] = self.packer_list
		file_ele_dict['peak_entropy'] = self.peak_entropy
		file_ele_dict['sym_links'] = self.sym_links
		file_ele_dict['byte_runs'] = self.byte_runs
		file_ele_dict['extracted_features'] = self.extracted_features		
		return file_ele_dict		
	
	#return full file object as a dictionary	
	def get_dict(self):
		file_dict = {}
		file_dict['is_packed'] = self.is_packed
		file_dict['file_name'] = self.file_name
		file_dict['file_path'] = self.file_path
		file_dict['device_path'] = self.device_path
		file_dict['full_path'] = self.full_path
		file_dict['file_extension'] = self.file_extension
		file_dict['size_in_bytes'] = self.size_in_bytes
		file_dict['magic_number'] = self.magic_number
		file_dict['file_format'] = self.file_format
		file_dict['hashes'] = self.hashes
		file_dict['digital_signature'] = self.digital_signature
		file_dict['modified_time'] = self.modified_time
		file_dict['accessed_time'] = self.accessed_time
		file_dict['created_time'] = self.created_time
		file_dict['file_attributes_list'] = self.file_attributes_list
		file_dict['permissions'] = self.permissions
		file_dict['user_owner'] = self.user_owner	
		file_dict['packer_list'] = self.packer_list
		file_dict['peak_entropy'] = self.peak_entropy
		file_dict['sym_links'] = self.sym_links
		file_dict['byte_runs'] = self.byte_runs
		file_dict['extracted_features'] = self.extracted_features	
		return file_dict

