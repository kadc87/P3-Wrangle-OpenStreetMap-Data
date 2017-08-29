# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 16:13:14 2017

@author: Kaustubh
"""

import xml.etree.cElementTree as ET
import pprint
import re

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def key_type(element, keys):
    """ 
        Imports element and checks for match with one of the three regular expressions 
        
    """
    if element.tag == "tag":
        k = element.get('k')
        if re.search(lower, k):
            keys["lower"] += 1
        elif re.search(lower_colon, k):
            keys["lower_colon"] += 1
        elif re.search(problemchars, k):
            keys["problemchars"] += 1
            print k
        else:
            keys["other"] += 1
    return keys

def process_map(filename):
    """ 
        Parses document and feeds elements to the key_type function 
      
    """
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)
    pprint.pprint(keys)
    return keys

if __name__ == '__main__':
 	process_map('raleigh_north-carolina.osm')