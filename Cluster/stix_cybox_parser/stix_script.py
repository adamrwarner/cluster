#!/usr/bin/python
# STIX Indicator Parsing Example
# Parses each Indicator in a STIX Package and Pulls out its Objects
import io
from pprint import pprint

from stix.core import STIXPackage
from stix.indicator import Indicator
import stix.bindings.stix_core as stix_core_binding
import cybox.objects

def main():
	# Parse the input XML file
	#input_file = '/home/gowens/Desktop/stix_v1.0_samples_20130408/STIX_Domain_Watchlist.xml'
	input_file = '/home/gowens/Desktop/stix_v1.0_samples_20130408/STIX_FileHash_Watchlist.xml'
	(stix_package, stix_package_binding_obj) = STIXPackage.from_xml(input_file)

	# Iterate through each STIX Indicator in the Package
	for indicator in stix_package.indicators:
		# Test to make sure the Indicator has Observable(s)
		#print indicator
		if indicator.observables:
			for observable in indicator.observables:
				#print observable
				# If so, extract its CybOX Object
				cybox_object = observable.object_
				obj_ns = cybox_object.properties._XSI_NS
				obj_type = cybox_object.properties._XSI_TYPE
				
				print cybox_object.properties.file_name
				print cybox_object.properties.file_path
				print cybox_object.properties.device_path
				print cybox_object.properties.full_path
				print cybox_object.properties.file_extension
				print cybox_object.properties.size_in_bytes
				print cybox_object.properties.magic_number
				print cybox_object.properties.file_format
				print cybox_object.properties.hashes
				
				#print cybox_object.properties.to_dict()
				
	#for ttp in stix_paciage.ttps:
	#	print ttp
				
def parseDict():
	for key, item in cybox_obj_dict.items():
		print key
		
		for property, value in cybox_obj_dict[key].items():
			print property
		
if __name__ == "__main__":
	#parseDict()
	main()

