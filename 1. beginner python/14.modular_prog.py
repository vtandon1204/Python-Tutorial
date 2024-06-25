# Modular Programming: we can use multiple files together to create one program

import math
# import pygame # for game dev by python
import os # for file pass, import images, import transitive things/files in python
print(math.sqrt(144))
print(math.pi)
print(math.degrees(math.pi))

import calendar
june2024 = calendar.month(2024,6)
print(june2024)

print(calendar.isleap(2024))

import myModule
print(myModule.myFunc(5))
print(myModule.Func2(500))

# if the file is not in the same directory then:-
# import modules.myModule 

# if the file is placed somewhere else then:-
# import sys
# sys.path('path of folder in which file is present')
# import myModule

