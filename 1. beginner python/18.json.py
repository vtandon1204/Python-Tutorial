# JSON - Java Script Object Notation
# it is a exchange format similar to XML
# more lightweighted as compared to XML

record={}
record['oggy'] = {
    'name': 'oggy',
    'address': '1 purple house',
    'phone': 235235
}
record['jack'] = {
    'name': 'jack',
    'address': '1 green house',
    'phone': 345452
}

import json
s=json.dumps(record) # taking dictionary object 'record' as input and dumping it as a string
