class GUIObjParser(object):
	_XSI_NS = "GUIBoxObj"
	_XSI_TYPE = "GUIObjectType"

	#attributes
	
	#elements
	height = ""
	width = ""

	def __init__(self, height, width):
		self.height = height
		self.width = width
	
	#return gui dialogbox object elements as a dictionary
	def get_elements(self):
		gui_ele_dict = {}
		gui_ele_dict['height'] = self.height
		gui_ele_dict['width'] = self.width		
		return gui_ele_dict		
	
	#return gui dialogbox object as a dictionary	
	def get_dict(self):
		gui_dict = {}
		gui_dict['height'] = self.height
		gui_dict['width'] = self.width	
		return gui_dict

