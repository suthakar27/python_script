#!/usr/bin/python


'''
	startswith   - checks if string starts with mentioned value
        endswith     - checks if string ends with mentioned value	
	isalpha      - checks all the character on the string is alphapetics. 
	isnumeric    - checks  all the character on the string is numeric
        isupper        - checks  all the character on the string is upper
        islower        - checks  all the character on the string is upper

We have multiple params like below

['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

'''

var1="Python Scripting"

print(var1.startswith('Py'))
print(var1.endswith('ing'))
print(var1.istitle())
print(var1.isupper())
print(var1.islower())
