'''
Created on Feb 15, 2015
@author: Strag
'''

import random
import xml.etree.ElementTree as ET

#data files for npc generation
eye_colors_file = 'eye_colors.xml'
hair_colors_file = 'hair_colors.xml'
names_file = 'names.xml'

#statistical values for npc generation
min_female_weight = 45
max_female_weight = 55
min_female_height = 140
max_female_height = 175

min_male_weight = 55
max_male_weight = 65
min_male_height = 155
max_male_height = 190

min_base_affection = 0
max_base_affection = 30

#weighting towards female for npc generation
sex_weight = 0.7

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
  
class NPC(object):

  def __init__(self, first_name, last_name, sex, hair_color, eye_color, height, weight, traits, hobbies, studies, start_affection):
    self.name = first_name
    self.last_name = last_name
    self.sex = sex
    self.hair_color = hair_color
    self.eye_color = eye_color
    self.height = height
    self.weight = weight
    self.traits = traits
    self.hobbies = hobbies
    self.studies = studies
    self.affection = start_affection
    
  def __repr__(self):
    retvalue = ""
    retvalue += "Name: %s %s\n" % (self.name, self.last_name)
    retvalue += "Sex: %s\n" % (self.sex)
    retvalue += "Hair: %s\n" % (self.hair_color)
    retvalue += "Eyes: %s\n" % (self.eye_color)
    retvalue += "Height: %s cm\n" % (self.height)
    retvalue += "Weight: %s kg\n" % (self.weight)
    retvalue += "Affection: %s\n\n" % (self.affection)
    return retvalue
    
  def getName(self):
    return self.first_name + " " + self.last_namenm
      
def generate():
  
  names = RandomNames(names_file)
  hair = HairColor(hair_colors_file)
  eyes = EyeColor(eye_colors_file)
  
  if random.random() > sex_weight:
    sex = 'male'
    first_name = names.get_male()
    height = random.randint(min_male_height, max_male_height)
    weight = random.randint(min_male_weight, max_male_weight)
  else:
    sex = 'female'
    first_name = names.get_female()
    height = random.randint(min_female_height, max_female_height)
    weight = random.randint(min_female_weight, max_female_weight)
  
  last_name = names.get_last()
  hair_color = hair.pick_random()
  eye_color = eyes.pick_random()
  traits = []
  hobbies = []
  studies = []
  affection = random.randint(min_base_affection, max_base_affection)
  
  return NPC(first_name, last_name, sex, hair_color, eye_color, height, weight, traits, hobbies, studies, affection)