

import xml.etree.cElementTree as ET
import pprint

osm_file = open("raleigh_north-carolina.osm", "r")

def count_tags(file):
	""" 
		Parses through tags and adds tags to the dictionary 
		after calling the add_tag function 
		
	"""
	tag_names = {}
	for event, elem in ET.iterparse(file, events=("start",)):
		add_tag(elem.tag, tag_names)
	return tag_names

def add_tag(tag, tag_names):
	""" 
		Either adds tag to dictionary or adds a count to existing tag 
		
	"""
	if tag not in tag_names:
		tag_names[tag] = 1
	else:
		tag_names[tag] += 1

tags = count_tags(osm_file)
pprint.pprint(tags)