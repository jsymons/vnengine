'''
Created on Feb 15, 2015

@author: Strag
'''

from VNData import Player
from VNData import NPC
from VNData import EyeColor
from VNData import HairColor
from VNData import RandomNames
import random

class WorldStatus(object):
    
    def __init__(self):
        self.player = Player.Player()
        self.npcs = []
        self.week = 0
        

def generate_world():
  world = WorldStatus()
  num_npcs = input("Number of NPCs to generate: ")
  names = RandomNames.RandomNames("names.xml")
  hair = HairColor.HairColor("hair_colors.xml")
  eyes = EyeColor.EyeColor("eye_colors.xml")
    
  #weighting towards female for random character generation
  sex_weight = 0.7
    
  for x in range(int(num_npcs)):
    if random.random() > sex_weight:
      #is male npc
      first_name = names.get_male()
      sex = "male"
      height = random.randint(155,190)
      weight = random.randint(55,65)
    else:
      #is female npc
      first_name = names.get_female()
      sex = "female"
      height = random.randint(140,175)
      weight = random.randint(45,55)
    
    last_name = names.get_last()
    hair_color = hair.pick_random()
    eye_color = eyes.pick_random()
    traits = []
    hobbies = []
    studies = []
    affection = random.randint(0,30)
    
    world.npcs.append(NPC.NPC(first_name, last_name, sex, hair_color, eye_color, height, weight, traits, hobbies, studies, affection))
    
  for npc in world.npcs:
    print(npc)
  
generate_world()