class NetworkRouteEntryObjParser(object):
	_XSI_NS = "NetworkRouteEntryObj"
	_XSI_TYPE = "NetworkRouteEntryObjectType"

	#attributes
	is_ipv6 = ""
	is_autoconfigure_address = ""
	is_immortal= ""
	is_loopback = ""
	is_publish = ""
	
	#elements
	destination_address = ""
	origin = ""
	netmask = ""

	def __init__(self, creation_time, layer3_protocol, layer4_protocol, 
					layer7_protocol, source_socket_address, source_tcp_state, 
					destination_socket_address, destination_tcp_state, 
					layer7_connections):
		self.creation_time = creation_time 
		self.layer3_protocol = layer3_protocol
		self.layer4_protocol = layer4_protocol
		self.layer7_protocol = layer7_protocol
		self.source_socket_address = source_socket_address
		self.source_tcp_state = source_tcp_state
		self.destination_socket_address = destination_socket_address
		self.destination_tcp_state = destination_tcp_state
		self.layer7_connections = layer7_connections
		
	def set_attributes(self, tls_used):
		self.tls_used = tls_used
	
	#return network connection object attributes as a dictionary
	def get_attributes(self):
		network_connection_attr_dict = {}
		network_connection_attr_dict['tls_used'] = self.is_injected
		return network_connection_attr_dict
	
	#return network connection object elements as a dictionary
	def get_elements(self):
		network_connection_ele_dict = {}
		network_connection_ele_dict['creation_time'] = self.creation_time
		network_connection_ele_dict['layer3_protocol'] = self.layer3_protocol
		network_connection_ele_dict['layer4_protocol'] = self.layer4_protocol
		network_connection_ele_dict['layer7_protocol'] = self.layer7_protocol
		network_connection_ele_dict['source_socket_address'] = self.source_socket_address
		network_connection_ele_dict['source_tcp_state'] = self.layer3_protocol
		network_connection_ele_dict['destination_socket_address'] = self.layer4_protocol
		network_connection_ele_dict['destination_tcp_state'] = self.layer7_protocol
		network_connection_ele_dict['layer7_connections'] = self.source_socket_address		
		return network_connection_ele_dict		
	
	#return full network connection object as a dictionary	
	def get_dict(self):
		network_connection_dict = {}
		network_connection_dict['tls_used'] = self.is_injected		
		network_connection_dict['creation_time'] = self.creation_time
		network_connection_dict['layer3_protocol'] = self.layer3_protocol
		network_connection_dict['layer4_protocol'] = self.layer4_protocol
		network_connection_dict['layer7_protocol'] = self.layer7_protocol
		network_connection_dict['source_socket_address'] = self.source_socket_address
		network_connection_dict['source_tcp_state'] = self.layer3_protocol
		network_connection_dict['destination_socket_address'] = self.layer4_protocol
		network_connection_dict['destination_tcp_state'] = self.layer7_protocol
		network_connection_dict['layer7_connections'] = self.source_socket_address		
		return network_connection_dict	

