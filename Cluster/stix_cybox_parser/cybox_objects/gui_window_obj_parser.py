class GUIWindowObjParser(object):
	_XSI_NS = "GUIWindowBoxObj"
	_XSI_TYPE = "GUIWindowObjectType"

	#attributes
	
	#elements
	owner_window = ""
	parent_window = ""
	window_display_name = ""

	def __init__(self, owner_window, parent_window):
		self.owner_window = owner_window
		self.parent_window = parent_window
		self.window_display_name = window_display_name
	
	#return gui window object elements as a dictionary
	def get_elements(self):
		gui_dialogbox_ele_dict = {}
		gui_dialogbox_ele_dict['owner_window'] = self.owner_window
		gui_dialogbox_ele_dict['parent_window'] = self.parent_window	
		gui_dialogbox_ele_dict['window_display_name'] = self.window_display_name		
		return gui_dialogbox_ele_dict		
	
	#return gui window object as a dictionary	
	def get_dict(self):
		gui_window_dict = {}
		gui_window_dict['owner_window'] = self.owner_window
		gui_window_dict['parent_window'] = self.parent_window
		gui_window_dict['window_display_name'] = self.window_display_name		
		return gui_window_dict

