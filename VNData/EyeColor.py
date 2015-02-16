'''
Created on Feb 15, 2015

@author: Strag
'''
import xml.etree.ElementTree as ET
import random

class EyeColor(object):
    
    def __init__(self, xmlfile):
        self.colors = {}
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        
        #populate colors into dictionary of arrays in format key : [base color, shade]
        for name in root.findall('color'):
            self.colors[name.get('name')] = [name.find('base').text, name.find('shade').text]
        
    def pick_random(self):
        return random.choice(list(self.colors.keys()))
    
    def get_base(self, color):
        return self.colors[color][0]
    
    def get_shade(self, color):
        return self.colors[color][1]