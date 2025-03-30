from game.func import *
import random
import pygame
import time
import sys

# updateをflipにするとどうなるだろうか

class creature:
    def __init__(self,name,power,skills):
        self.name=name
        self.power=power
        self.skills=skills

class battle_with_power:
    def __init__(self,creature1,creature2,power1,power2):
        self.creature1=creature1
        self.creature2=creature2
        self.power1=power1
        self.power2=power2
    def judge(self):
        if self.power1>self.power2:
            print(self.creature1.name+"の勝ち")
        elif self.power1<self.power2:
            print(self.creature2.name+"の勝ち")
        else:
            print("引き分け")