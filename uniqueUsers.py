import xml.etree.cElementTree as ET

def get_user(element) :
    if 'uid' in element.attrib :
        user = element.get('uid')
        return user
        
        
def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        user = get_user(element)
        if user != None:
            users.add(user)
    return users
    
users = process_map('raleigh_north-carolina.osm')

print(len(users))