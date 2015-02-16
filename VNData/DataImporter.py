'''
Created on Feb 15, 2015

@author: Strag
'''



import xml.etree.ElementTree as ET

import EyeColor,HairColor


hair_colors = {}
eye_colors = {}

# load XML file
tree = ET.parse('colors.xml')
root = tree.getroot()


# import hair colors into dictionary keyed by color name
for color in root.findall("./hair_colors/color"):
    hair_colors[color.get('name')] = HairColor.HairColor(color.get('name'), color.find('base').text, color.find('highlight').text)

# import eye colors into dictionary keyed by color name
for color in root.findall("./eye_colors/color"):
    eye_colors[color.get('name')] = EyeColor.EyeColor(color.get('name'), color.find('base').text, color.find('shade').text)


