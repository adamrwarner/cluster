class GUIDialogboxObjParser(object):
	_XSI_NS = "GUIDialogBoxObj"
	_XSI_TYPE = "GUIDialogBoxObjectType"

	#attributes
	
	#elements
	box_caption = ""
	box_text = ""

	def __init__(self, box_caption, box_text):
		self.box_caption = box_caption
		self.box_text = box_text
	
	#return gui dialogbox object elements as a dictionary
	def get_elements(self):
		gui_dialogbox_ele_dict = {}
		gui_dialogbox_ele_dict['box_caption'] = self.box_caption
		gui_dialogbox_ele_dict['box_text'] = self.box_text		
		return gui_dialogbox_ele_dict		
	
	#return gui dialogbox object as a dictionary	
	def get_dict(self):
		gui_dialogbox_dict = {}
		gui_dialogbox_dict['box_caption'] = self.box_caption
		gui_dialogbox_dict['box_text'] = self.box_text	
		return gui_dialogbox_dict

