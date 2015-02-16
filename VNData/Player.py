'''
Created on Feb 15, 2015

@author: Strag
'''
class Player(object):
    
    def __init__(self):
        self.money = 200
        self.stress = 0
        self.skills = {
                       'organized' : 0,
                       'reflective' : 0,
                       'creative' : 0,
                       'active' : 0,
                       'rational' : 0
                       }
        