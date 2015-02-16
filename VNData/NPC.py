'''
Created on Feb 15, 2015

@author: Strag
'''

class NPC(object):
    '''
    classdocs
    '''


    def __init__(self, first_name, last_name, sex, hair_color, eye_color, height, weight, traits, hobbies, studies, start_affection):
        '''
        Constructor
        '''
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
    
    