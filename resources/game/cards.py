import random
import pygame
import time
import sys
import json
import pickle
from game import func
from game import auto

#定数の設定
width=100
height=144
field=(1550,900)
fieldcolor=(0,200,0)
upbase=(230, 155)
downbase=(920, 602)

def r_c_001():
    return

def r_c_002(save,flag):
    return

def r_c_003():
    return

def r_c_004():
    return

def r_c_005(save,flag,mode,screen):
    if mode=="cip":
        # バトル効果
        battle=func.choose(screen,"バトル効果を発動しますか？")
        return

def r_c_006():
    # auto.gachinko_judge()
    return

def r_c_010(save,flag,mode):
    if mode=="cip":
        if flag:
            for i in range(len(save[8])):
                save[8][i][1]=False
        else:
            for i in range(len(save[9])):
                save[9][i][1]=False
        return save

def g_s_001(save,flag):
    return func.addmana(1,save,flag)

def b_s_001(save,flag):
    return func.draw(2,save,flag)

def gb_c_001(save,flag,mode):
    if mode=="cip":
        return func.draw(2,save,flag)

def b_s_002(save,flag):
    return func.draw(1,save,flag)

def b_c_003(save,flag):
    if flag:
        temp=save[0]+save[10]
        save[0]=func.shuffle(temp)
        save[10]=[]
    else:
        temp=save[1]+save[11]
        save[1]=func.shuffle(temp)
        save[11]=[]
    return save

def b_c_001(save,flag,screen):
    if flag:
        if len(save[0])>5:
            temp=save[0][:5]
        else:
            temp=save[0]
        func.showcards(temp,screen,True)
    else:
        if len(save[1])>5:
            temp=save[1][:5]
        else:
            temp=save[1]
        func.showcards(temp,screen,False)
    return save

def b_cs_001(flag,mode):
    return

def b_s_002(save,flag):
    save=func.draw(1,save,flag)
    return save

def d_c_001(save,flag,mode):
    if mode=="cip":
        return func.bochiokuri(1,save,flag)

def d_c_004(save,flag,mode):
    if mode=="cip":
        a=True
        if a:
            if flag:
                tmp=func.shuffle(save[11])
                save[11]=[]
                save[1]+=tmp
                return save
            else:
                tmp=func.shuffle(save[10])
                save[10]=[]
                save[0]+=tmp
                return save
        else:
            return func.bochiokuri(2,save,flag)

def d_c_005(save,flag,mode):
    if mode=="cip":
        a=True
        if a:
            save=func.bochiokuri(3,save,flag)
        return save

def d_c_006(save,flag,mode):
    return save

def d_mr_001(save,flag,mode):
    return save

def d_s_001(save,flag):
    save=func.bochiokuri(4,save,flag)
    return save

def d_tc_001(save,flag,mode):
    if mode=="cip":
        a=True
        if a:
            save=func.bochiokuri(2,save,flag)
        return save

def rg_c_001(save,flag,mode):
    if mode=="cip":
        save=func.addmana(1,save,flag)
        if flag:
            save[6][-1][6]=True
            if 'ドラゴン' in save[6][-1][2]:
                save=func.addmana(1,save,flag)
                save[6][-1][6]=True
        else:
            save[7][-1][6]=True
            if 'ドラゴン' in save[7][-1][2]:
                save=func.addmana(1,save,flag)
                save[7][-1][6]=True
        return save

def rg_c_004(save,flag,mode):
    if mode=="cip":
        if flag:
            for i in range(len(save[6])):
                save[6][i][1]=False
        else:
            for i in range(len(save[7])):
                save[7][i][1]=False
        return save

def rg_s_001(save,flag):
    if flag:
        one=save[0][0]
        two=save[0][1]
        save[0]=save[0][2:]
        if 'ドラゴン' in one[2]:
            one[6]=True
            save[6].append(one)
        else:
            save[10].append(one)
        if 'ドラゴン' in two[2]:
            two[6]=True
            save[6].append(two)
        else:
            save[10].append(two)
    else:
        one=save[1][0]
        two=save[1][1]
        save[1]=save[1][2:]
        if 'ドラゴン' in one[2]:
            one[6]=True
            save[7].append(one)
        else:
            save[11].append(one)
        if 'ドラゴン' in two[2]:
            two[6]=True
            save[7].append(two)
        else:
            save[11].append(two)
    return save

def bw_cs_001(save,flag):
    return func.draw(3,save,flag)

def gbd_c_002(save,flag,mode):
    if mode=="cip":
        a=True
        if a:
            save=func.draw(2,save,flag)
        return save