import random
import pygame
import time
import sys
import json
import pickle
from game.func import *
from game.cards import *

#定数の設定
width=100
height=144
field=(1550,1000)
fieldcolor=(0,200,0)
upbase=(230, 155)
downbase=(920, 696)
base=(100,100)

#メッセージを表示するコンソールをメニューから見れるようにする
#各アクションの実行後、ログを残す
def showlog(screen,log,save,debug):
    rect(screen,True)
    info(save,screen,debug)
    return

def mekureid(save,n,flag,key):
    return save