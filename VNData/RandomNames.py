import xml.etree.ElementTree as ET
import random

class RandomNames(object):
    def __init__(self, xml_file):
        self.female = []
        self.male = []
        self.last = []
        
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        for name in root.findall("./first_names/name"):
            if name.get("sex") == "f":
                self.female.append(name.text)
            elif name.get("sex") == "m":
                self.male.append(name.text)
        
        for name in root.findall("./last_names/name"):
            self.last.append(name.text)
            
    def get_female(self):
        return random.choice(self.female)
    
    def get_male(self):
        return random.choice(self.male)
    
    def get_last(self):
        return random.choice(self.last)
