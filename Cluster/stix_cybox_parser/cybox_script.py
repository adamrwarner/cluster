#!/usr/bin/python

import io
import sys
import os.path
from lxml import etree
from pprint import pprint
from stix.core import stix_package
from stix.indicator import indicator
import stix.bindings.stix_core as stix_core_binding

#def parse(xml_file):
    #observables_obj = cybox_core_binding.parse(xml_file)
    #observed = observables_obj.get_Observable()
    #return observed

def main():
	if len(sys.argv) != 2:
		usage()
	
	xml_file = sys.argv[-1]
	if not os.path.isfile(xml_file):
		print("Error: Didn't provide a file")
		usage()
		
	tree = etree.parse(xml_file)

	root = tree.getroot()
	objects = root.findall(".//cybox:Object",
		namespaces={"xsi": "http://www.w3.org/2001/XMLSchema-instance",
					"stix": "http://stix.mitre.org/stix-1",
					"indicator": "http://stix.mitre.org/Indicator-2",
					"cybox": "http://cybox.mitre.org/cybox-2",
					"URIObject": "http://cybox.mitre.org/objects#URIObject-2",
					"cyboxVocabs": "http://cybox.mitre.org/default_vocabularies-2",
					"stixVocabs": "http://stix.mitre.org/default_vocabularies-1"
		}
	)
	
	for object in objects:
		for property in object:
			print property.tag
			#print property.attrib
			for key in property.attrib.values():
				print key
			
		
		
def usage():
	print("Usage: python cybox_script.py <xml_filename>");
	exit(1);

if __name__ == "__main__":
    main()
