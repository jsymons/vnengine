'''
Created on Feb 15, 2015

@author: Strag
'''
import xml.etree.ElementTree as ET
import random

class HairColor(object):
    
    def __init__(self, xmlfile):
        self.colors = {}
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        
        #populate colors into dictionary of arrays in format key : [base color, highlight]
        for name in root.findall('color'):
            self.colors[name.get('name')] = [name.find('base').text, name.find('highlight').text]
        
    def pick_random(self):
        return random.choice(list(self.colors.keys()))
    
    def get_base(self, color):
        return self.colors[color][0]
    
    def get_highlight(self, color):
        return self.colors[color][1]