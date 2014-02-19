class DiskPartitionlObjParser(object):
	_XSI_NS = "DiskPartitionObj"
	_XSI_TYPE = "DiskPartitionObjectType"
	
	#elements
	created = ""
	device_name = ""
	mount_point = ""
	partition_id = ""
	partition_length = ""
	partition_offset = ""
	space_left = ""
	space_used = ""
	total_space = ""
	type = ""

	def __init__(self, created, device_name, mount_point, partition_id, 
				partition_length, parition_offset, space_left, space_used, 
				total_space, type):
		self.created = created
		self.device_name = device_name
		self.mount_point = mount_point
		self.partition_id = partition_id
		self.partition_length = partition_length
		self.parition_offset = parition_offset
		self.space_left = space_left
		self.space_used = space_used
		self.total_space = total_space
		self.type = type
		
	#return disk partition object elements as a dictionary
	def get_elements(self):
		disk_partition_ele_dict = {}
		disk_partition_ele_dict['created'] = self.created
		disk_partition_ele_dict['device_name'] = self.device_name
		disk_partition_ele_dict['mount_point'] = self.mount_point
		disk_partition_ele_dict['partition_id'] = self.partition_id
		disk_partition_ele_dict['partition_length'] = self.partition_length
		disk_partition_ele_dict['parition_offset'] = self.parition_offset
		disk_partition_ele_dict['space_left'] = self.space_left
		disk_partition_ele_dict['space_used'] = self.space_used	
		disk_partition_ele_dict['total_space'] = self.total_space
		disk_partition_ele_dict['type'] = self.type			
		return disk_partition_ele_dict		
	
	#return full disk partition object as a dictionary	
	def get_dict(self):
		disk_partition_dict = {}
		disk_partition_dict['created'] = self.created
		disk_partition_dict['device_name'] = self.device_name
		disk_partition_dict['mount_point'] = self.mount_point
		disk_partition_dict['partition_id'] = self.partition_id
		disk_partition_dict['partition_length'] = self.partition_length
		disk_partition_dict['parition_offset'] = self.parition_offset
		disk_partition_dict['space_left'] = self.space_left
		disk_partition_dict['space_used'] = self.space_used		
		disk_partition_dict['total_space'] = self.total_space
		disk_partition_dict['type'] = self.type	
		return disk_partition_dict	

