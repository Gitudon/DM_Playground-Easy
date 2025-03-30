import random
import pygame
import time
import sys
import json
import pickle

#定数の設定
width=100
height=144
field=(1550,1000)
fieldcolor=(0,200,0)
upbase=(230, 155)
downbase=(920, 696)
base=(100,100)

def deck(screen,me,opposite):
    img = pygame.image.load("GUI/image/uramen/ura.jpg")
    if len(me)>0:
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, downbase)
    if len(opposite)>0:
        img2 = pygame.transform.rotate(img, 180)
        img2 = pygame.transform.scale(img2, (width, height))
        screen.blit(img2, upbase)

def dimension(screen,me,opposite):
    if len(me)>0:
        img = pygame.image.load("GUI/image/cards/"+me[0][0]+".jpg")
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, (downbase[0]+20+width*2,downbase[1]))
    if len(opposite)>0:
        img = pygame.image.load("GUI/image/cards/"+opposite[0][0]+".jpg")
        img2 = pygame.transform.rotate(img, 180)
        img2 = pygame.transform.scale(img2, (width, height))
        screen.blit(img2, (upbase[0]-20-width*2,upbase[1]))
    pygame.display.flip()

def grdeck(screen,me,opposite):
    img = pygame.image.load("GUI/image/uramen/grura.jpg")
    if len(me)>0:
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, (downbase[0]+20+width*2,downbase[1]+10+height))
    if len(opposite)>0:
        img2 = pygame.transform.rotate(img, 180)
        img2 = pygame.transform.scale(img2, (width, height))
        screen.blit(img2, (upbase[0]-20-width*2,upbase[1]-10-height))
    pygame.display.flip()

def manazone(screen,me,opposite):
    for i in range(len(me)):
        if me[i][2]:
            img = pygame.image.load("GUI/image/uramen/ura.jpg")
        else:
            img = pygame.image.load("GUI/image/cards/"+me[i][0][0]+".jpg")
        img = pygame.transform.scale(img, (width, height))
        if me[i][1]:
            img = pygame.transform.rotate(img, 270)
            screen.blit(img, (downbase[0]+width-22-50*i,downbase[1]+32+height))
        else:
            img1 = pygame.transform.rotate(img, 180)
            screen.blit(img1, (downbase[0]+width+10-50*i,downbase[1]+10+height))
    for i in range(len(opposite)):
        if opposite[i][2]:
            img = pygame.image.load("GUI/image/uramen/ura.jpg")
        else:
            img = pygame.image.load("GUI/image/cards/"+opposite[i][0][0]+".jpg")
        img = pygame.transform.scale(img, (width, height))
        if opposite[i][1]:
            img = pygame.transform.rotate(img, 90)
            screen.blit(img, (upbase[0]-width-22+50*i,upbase[1]+12-height))
        else:
            screen.blit(img, (upbase[0]-width-10+50*i,upbase[1]-10-height))
    pygame.display.flip()
    return

def battlezone(screen,me,opposite):
    for i in range(len(me)):
        if me[i][2]:
            img = pygame.image.load("GUI/image/uramen/ura.jpg")
        else:
            img = pygame.image.load("GUI/image/cards/"+me[i][0][0]+".jpg")
        img = pygame.transform.scale(img, (width, height))
        if any(substring in me[i][0][0] for substring in ["_d2f_", "_df_", "_drf_", "_dgf_", "_sf_", "_skf_", "_kf_", "_dmf", "_hf", "_dsf_", "_mf_", "_t2f_", "_ff_", "_lf_", "_zc_"]):
            img = pygame.transform.rotate(img, 90)
            if any(substring in me[i][0][0] for substring in ["_d2f_", "_sf_"]):
                if me[i][5]:
                    img = pygame.transform.rotate(img, 180)
            screen.blit(img, (upbase[0]-32-width*2+(10+width)*i,downbase[1]-(height+10)+22))
        else:
            if me[i][1]:
                img = pygame.transform.rotate(img, 270)
                screen.blit(img, (upbase[0]-32-width*2+(10+width)*i,downbase[1]-(height+10)+22))
            else:
                screen.blit(img, (upbase[0]-20-width*2+(10+width)*i,downbase[1]-(height+10)))
    for i in range(len(opposite)):
        if opposite[i][2]:
            img = pygame.image.load("GUI/image/uramen/ura.jpg")
        else:
            img = pygame.image.load("GUI/image/cards/"+opposite[i][0][0]+".jpg")
        img = pygame.transform.scale(img, (width, height))
        if any(substring in opposite[i][0][0] for substring in ["_d2f_", "_df_", "_drf_", "_dgf_", "_sf_", "_skf_", "_kf_", "_dmf", "_hf", "_dsf_", "_mf_", "_t2f_", "_ff_", "_lf_", "_ds_"]):
            img= pygame.transform.rotate(img, 270)
            if any(substring in opposite[i][0][0] for substring in ["_d2f_", "_sf_"]):
                if opposite[i][5]:
                    img = pygame.transform.rotate(img, 180)
            screen.blit(img, (upbase[0]-32-width*2+(10+width)*i,upbase[1]+(height+10)+22))
        else:
            img = pygame.transform.scale(img, (width, height))
            if opposite[i][1]:
                img = pygame.transform.rotate(img, 90)
                screen.blit(img, (upbase[0]-32-width*2+(10+width)*i,upbase[1]+(height+10)+22))
            else:
                img = pygame.transform.rotate(img, 180)
                screen.blit(img, (upbase[0]-20-width*2+(10+width)*i,upbase[1]+(height+10)))
    pygame.display.flip()
    return

def graveyard(screen,me,opposite):
    if len(me)>0:
        img = pygame.image.load("GUI/image/cards/"+me[0][0]+".jpg")
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, (downbase[0]+10+width,downbase[1]))
    if len(opposite)>0:
        img = pygame.image.load("GUI/image/cards/"+opposite[0][0]+".jpg")
        img2 = pygame.transform.rotate(img, 180)
        img2 = pygame.transform.scale(img2, (width, height))
        screen.blit(img2, (upbase[0]-10-width,upbase[1]))
    pygame.display.flip()
    return

def emenu(screen):
    font = pygame.font.SysFont("msgothic", 30)
    pygame.draw.rect(screen, (192,192,192), pygame.Rect(field[0]-300,0,300,field[1]))
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,10,280,50))
    gTxt = font.render("手札を確認する", True, (255,255,255))
    screen.blit(gTxt, [1265, 20])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,70,280,50))
    gTxt = font.render("デッキの上を見る", True, (255,255,255))
    screen.blit(gTxt, [1265, 80])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,130,280,50))
    gTxt = font.render("デッキを確認する", True, (255,255,255))
    screen.blit(gTxt, [1265, 140])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,190,280,50))
    gTxt = font.render("1枚ドロー", True, (255,255,255))
    screen.blit(gTxt, [1265, 200])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,250,280,50))
    gTxt = font.render("マナチャージする", True, (255,255,255))
    screen.blit(gTxt, [1265, 260])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,310,280,50))
    gTxt = font.render("山上を墓地送り", True, (255,255,255))
    screen.blit(gTxt, [1265, 320])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,370,280,50))
    gTxt = font.render("シールド追加", True, (255,255,255))
    screen.blit(gTxt, [1265, 380])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,430,280,50))
    gTxt = font.render("GR召喚", True, (255,255,255))
    screen.blit(gTxt, [1265, 440])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,490,280,50))
    gTxt = font.render("デッキをシャッフル", True, (255,255,255))
    screen.blit(gTxt, [1265, 500])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,550,280,50))
    gTxt = font.render("視点切り替え", True, (255,255,255))
    screen.blit(gTxt, [1265, 560])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,610,280,50))
    gTxt = font.render("ターンエンド", True, (255,255,255))
    screen.blit(gTxt, [1265, 620])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,670,280,50))
    gTxt = font.render("追加ターン", True, (255,255,255))
    screen.blit(gTxt, [1265, 680])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,730,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 740])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,790,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 800])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,850,280,50))
    gTxt = font.render("ゲームをリセット", True, (255,255,255))
    screen.blit(gTxt, [1265, 860])
    pygame.draw.rect(screen, (226,4,27), pygame.Rect(1260,910,280,50))
    gTxt = font.render("ゲームを終了", True, (255,255,255))
    screen.blit(gTxt, [1265, 920])
    pygame.display.flip()

def menu(screen):
    font = pygame.font.SysFont("msgothic", 30)
    pygame.draw.rect(screen, (192,192,192), pygame.Rect(field[0]-300,0,300,field[1]))
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,10,280,50))
    gTxt = font.render("手札を確認する", True, (255,255,255))
    screen.blit(gTxt, [1265, 20])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,70,280,50))
    gTxt = font.render("手札をシャッフル", True, (255,255,255))
    screen.blit(gTxt, [1265, 80])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,130,280,50))
    gTxt = font.render("ターンエンド", True, (255,255,255))
    screen.blit(gTxt, [1265, 140])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,190,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 200])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,250,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 260])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,310,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 320])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,370,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 380])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,430,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 440])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,490,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 500])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,550,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 560])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,610,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 620])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,670,280,50))
    gTxt = font.render("デバッグメニュー", True, (255,255,255))
    screen.blit(gTxt, [1265, 680])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,730,280,50))
    gTxt = font.render("ヘルプを表示", True, (255,255,255))
    screen.blit(gTxt, [1265, 740])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,790,280,50))
    gTxt = font.render("ゲームをリセット", True, (255,255,255))
    screen.blit(gTxt, [1265, 800])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,850,280,50))
    gTxt = font.render("ログを表示", True, (255,255,255))
    screen.blit(gTxt, [1265, 860])
    pygame.draw.rect(screen, (226,4,27), pygame.Rect(1260,910,280,50))
    gTxt = font.render("ゲームを終了", True, (255,255,255))
    screen.blit(gTxt, [1265, 920])
    pygame.display.flip()

#いい感じに変更する
def debugmenu(screen):
    font = pygame.font.SysFont("msgothic", 30)
    pygame.draw.rect(screen, (192,192,192), pygame.Rect(field[0]-300,0,300,field[1]))
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,10,280,50))
    gTxt = font.render("手札を確認する", True, (255,255,255))
    screen.blit(gTxt, [1265, 20])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,70,280,50))
    gTxt = font.render("手札をソートする", True, (255,255,255))
    screen.blit(gTxt, [1265, 80])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,130,280,50))
    gTxt = font.render("1枚ドロー", True, (255,255,255))
    screen.blit(gTxt, [1265, 140])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,190,280,50))
    gTxt = font.render("シールド確認", True, (255,255,255))
    screen.blit(gTxt, [1265, 200])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,250,280,50))
    gTxt = font.render("視点切り替え", True, (255,255,255))
    screen.blit(gTxt, [1265, 260])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,310,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 320])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,370,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 380])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,430,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 440])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,490,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 500])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,550,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 560])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,610,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 620])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,670,280,50))
    gTxt = font.render("通常メニュー", True, (255,255,255))
    screen.blit(gTxt, [1265, 680])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,730,280,50))
    gTxt = font.render("ヘルプを表示", True, (255,255,255))
    screen.blit(gTxt, [1265, 740])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,790,280,50))
    gTxt = font.render("ゲームをリセット", True, (255,255,255))
    screen.blit(gTxt, [1265, 800])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,850,280,50))
    gTxt = font.render("ログを表示", True, (255,255,255))
    screen.blit(gTxt, [1265, 860])
    pygame.draw.rect(screen, (226,4,27), pygame.Rect(1260,910,280,50))
    gTxt = font.render("ゲームを終了", True, (255,255,255))
    screen.blit(gTxt, [1265, 920])
    pygame.display.flip()

def move(a,b,i):
    b.append(a[i])
    a.remove(a[i])
    return [a,b]

def Shuffle(a):
    sh=[]
    while len(a)!=0:
        b=random.choice(a)
        sh.append(b)
        a.remove(b)
    return sh

def swap(save):
    for i in range(len(save)//2):
        tmp=(save[2*i+1])
        save[2*i+1]=save[2*i]
        save[2*i]=tmp
    return save

def check(a):
    b=sorted(a)
    return len(b)

def put(save,card,flag):
    tmp=[card,False,False,[card],[],-1,1,0]
    if flag:
        save[8].append(tmp)
    else:
        save[9].append(tmp)
    return save

def expand(save,card,flag):
    tmp=[card,False,False,[card],[],False]
    if flag:
        save[8].append(tmp)
    else:
        save[9].append(tmp)
    return save

def summon(save,card,flag):
    return put(save,flag,card)

def grsummon(n,save,flag,screen,debug):
    for _ in range(n):
        if flag:
            if len(save[14])==0:
                return save
            card=save[14][0]
            save[14]=save[14][1:]
        else:
            if len(save[15])==0:
                return save
            card=save[15][0]
            save[15]=save[15][1:]
        save=put(save,card,flag)
    recover(save,screen,debug)
    return save

def gotodeck(save,card,flag,up):
    if flag:
        if up:
            save[0]=[card]+save[0]
        else:
            save[0].append(card)
    else:
        if up:
            save[1]=[card]+save[1]
        else:
            save[1].append(card)
    return save

def bounce(save,card,flag):
    if flag:
        if "_grc_" in card[0]:
            save[14].append(card)
        elif any(substring in card[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
            save[12].append(card)
        else:
            save[4].append(card)
    else:
        if "_grc_" in card[0]:
            save[15].append(card)
        elif any(substring in card[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
            save[13].append(card)
        else:
            save[5].append(card)
    return save

def draw(n,save,flag):
    if flag:
        for _ in range(n):
            if save[0]!=[]:
                save=bounce(save,save[0][0],flag)
                save[0] = save[0][1:]
            else:
                print("You can't draw a card.")
    else:
        for _ in range(n):
            if save[1]!=[]:
                save=bounce(save,save[1][0],flag)
                save[1] = save[1][1:]
            else:
                print("You can't draw a card.")
    return save

def putgrave(save,card,flag):
    if flag:
        if "_grc_" in card[0]:
                save[14].append(card)
        elif any(substring in card[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
            save[12].append(card)
        else:
            save[10]=[card]+save[10]
    else:
        if "_grc_" in card[0]:
            save[15].append(card)
        elif any(substring in card[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
            save[13].append(card)
        else:
            save[11]=[card]+save[11]
    return save

def bochiokuri(n,save,flag,screen,debug):
    if flag:
        for _ in range(n):
            if save[0]!=[]:
                save=putgrave(save,save[0][0],flag)
                save[0] = save[0][1:]
                recover(save,screen,debug)
            else:
                print("You can't put a card.")
    else:
        for _ in range(n):
            if save[1]!=[]:
                save=putgrave(save,save[1][0],flag)
                save[1] = save[1][1:]
                recover(save,screen,debug)
            else:
                print("You can't put a card.")
    return save

def putmana(save,card,flag,crystal,zone):
    if flag:
        if "_grc_" in card[0]:
            save[14].append(card)
        elif any(substring in card[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
            save[12].append(card)
        else:
            tmp=[card,False,False]
            tap=0
            #zone:バトルゾーンからマナ送りか
            if zone:
                if any(substring in card[0] for substring in ["_cs_", "_ncs_", "_ss_"]):
                    tap=max(len(card[6][0]),len(card[6][1]))
                else:
                    tap=len(card[6])
            else:
                if any(substring in card[0] for substring in ["_cs_", "_ncs_", "_ss_"]):
                    buf=[]
                    for a in card[6][0]:
                        buf.append(a)
                    for b in card[6][1]:
                        buf.append(b)
                    u_buf=list(set(buf))
                    tap=len(u_buf)
                else:
                    tap=len(card[6])
            if tap>=2:
                tmp[1]=True
            if crystal:
                tmp[2]=True
            save[6].append(tmp)
    else:
        if "_grc_" in card[0]:
            save[15].append(card)
        elif any(substring in card[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
            save[13].append(card)
        else:
            tmp=[card,False,False]
            tap=0
            if zone:
                if any(substring in card[0] for substring in ["_cs_", "_ncs_", "_ss_"]):
                    tap=len(card[6][0])
                else:
                    tap=len(card[6])
            else:
                if any(substring in card[0] for substring in ["_cs_", "_ncs_", "_ss_"]):
                    buf=[]
                    for a in card[6][0]:
                        buf.append(a)
                    for b in card[6][1]:
                        buf.append(b)
                    u_buf=list(set(buf))
                    tap=len(u_buf)
                else:
                    tap=len(card[6])
            if tap>=2:
                tmp[1]=True
            if crystal:
                tmp[2]=True
            save[7].append(tmp)
    return save

def addmana(n,save,flag,crystal,screen,debug):
    if flag:
        for _ in range(n):
            if save[0]!=[]:
                save=putmana(save,save[0][0],flag,crystal,False)
                save[0] = save[0][1:]
                recover(save,screen,debug)
            else:
                print("You can't put a card.")
    else:
        for _ in range(n):
            if save[1]!=[]:
                save=putmana(save,save[1][0],flag,crystal,False)
                save[1] = save[1][1:]
                recover(save,screen,debug)
            else:
                print("You can't put a card.")
    return save

def putshield(save,card,flag,mode):
    if flag:
        if "_grc_" in card[0]:
            save[14].append(card)
        elif any(substring in card[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
            save[12].append(card)
        else:
            tmp=[card,mode,[]]
            save[2].append(tmp)
    else:
        if "_grc_" in card[0]:
            save[15].append(card)
        elif any(substring in card[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
            save[13].append(card)
        else:
            tmp=[card,mode,[]]
            save[3].append(tmp)
    return save

def shieldplus(n,save,flag,screen,debug,mode1,mode2):
    if flag:
        for _ in range(n):
            if save[0]!=[]:
                save=putshield(save,save[0][0],flag,mode2)
                save[0] = save[0][1:]
            else:
                print("You can't add a shield.")
    else:
        for _ in range(n):
            if save[1]!=[]:
                save=putshield(save,save[1][0],flag,mode2)
                save[1] = save[1][1:]
            else:
                print("You can't add a shield.")
    if mode1:
        recover(save,screen,debug)
    return save

def putdimension(save,card,flag):
    if flag:
        if "_grc_" in card[0]:
            save[14].append(card)
        else:
            save[12].append(card)
    else:
        if "_grc_" in card[0]:
            save[15].append(card)
        else:
            save[13].append(card)
    return save

def seal(save,flag,key):
    if flag:
        tmp=save[0][0]
        save[0]=save[0][1:]
        save[8][key][2]=True
        save[8][key][4]=[tmp]+save[8][key][4]
    else:
        tmp=save[1][0]
        save[1]=save[1][1:]
        save[9][key][2]=True
        save[9][key][4]=[tmp]+save[9][key][4]
    return save

def overlap(save,flag,key,tmp,up):
    if flag:
        if up:
            save[8][key][3]=[tmp]+save[8][key][3]
            save[8][key][0]=tmp
        else:
            save[8][key][3].append(tmp)
    else:
        if up:
            save[9][key][3]=[tmp]+save[9][key][3]
            save[9][key][0]=tmp
        else:
            save[9][key][3].append(tmp)
    return save

def overlap2(save,flag,key,tmp,up,surface):
    if flag:
        if up:
            save[2][key][2]=[tmp]+save[2][key][2]
            save[2][key][0]=tmp
        else:
            save[2][key][2].append(tmp)
        save[2][key][1]=surface
    else:
        if up:
            save[3][key][2]=[tmp]+save[3][key][2]
            save[3][key][0]=tmp
        else:
            save[3][key][2].append(tmp)
        save[3][key][1]=surface
    return save

def showcard(screen,card,flag,key):
    if flag==1:
        tmp= pygame.image.load("GUI/image/uramen/ura.jpg")
    elif flag==2:
        tmp=pygame.image.load("GUI/image/cards/"+card[0][0]+".jpg")
        pixels = pygame.PixelArray(tmp)
        for y in range(tmp.get_height()):
            for x in range(tmp.get_width()):
                r, g, b, _ = screen.unmap_rgb(pixels[x][y])
                gray = int((r + g + b) / 3)
                pixels[x][y] = (gray, gray, gray)
        del pixels
    elif flag==3:
        tmp=pygame.image.load("GUI/image/uramen/ura.jpg")
        pixels = pygame.PixelArray(tmp)
        for y in range(tmp.get_height()):
            for x in range(tmp.get_width()):
                r, g, b, _ = screen.unmap_rgb(pixels[x][y])
                gray = int((r + g + b) / 3)
                pixels[x][y] = (gray, gray, gray)
        del pixels
    else:
        if key in [2,3,6,7,8,9,20,21]:
            tmp=pygame.image.load("GUI/image/cards/"+card[0][0]+".jpg")
        else:
            tmp=pygame.image.load("GUI/image/cards/"+card[0]+".jpg")
    tmp=pygame.transform.scale(tmp, (500, 720))
    screen.blit(tmp, (110,140))
    pygame.display.flip()
    return

def cardmenu(screen,key):
    font = pygame.font.SysFont("msgothic", 50)
    #デッキのリスト01、シールドのリスト23、手札のリスト45、マナのリスト67、バトルゾーンのリスト89、墓地のリスト1011、超次元ゾーンのリスト1213、GRゾーンのリスト1415、構成カード1617見てるカード1819封印カード2021
    mode=[7,7,7,7,7,7,8,8,9,9,6,6,6,6,0,0,6,6,7,7,6,6]
    n=mode[key]
    if key in [0,1]:
        txts=["バトルゾーンに出す","手札に加える","マナゾーンに置く","墓地に置く","重ねる","超次元ゾーンに置く","シールドゾーンに置く"]
    elif key in [2,3]:
        txts=["手札に加える","裏返す","墓地に置く","マナゾーンに置く","山札に送る","バトルゾーンに出す","構成カードを表示する"]
    elif key in [4,5]:
        txts=["バトルゾーンに出す","マナゾーンに置く","墓地に置く","山札に送る","重ねる","超次元ゾーンに置く","シールドゾーンに置く"]
    elif key in [6,7]:
        txts=["タップ/アンタップする","バトルゾーンに出す","手札に加える","墓地に置く","山札に送る","裏返す","重ねる","シールドゾーンに置く"]
    elif key in [8,9]:
        txts=["位相を変える","手札に加える","マナゾーンに置く","墓地に置く","山札に送る","構成カードを表示する","封印する","超次元ゾーンに置く","シールドゾーンに置く"]
    elif key in [10,11]:
        txts=["バトルゾーンに出す","手札に加える","マナゾーンに置く","山札に送る","重ねる","シールドゾーンに置く"]
    elif key in [12,13]:
        txts=["バトルゾーンに出す","手札に加える","マナゾーンに置く","墓地に置く","山札に送る","重ねる"]
    elif key in [16,17]:
        txts=["バトルゾーンを移動する","手札に加える","マナゾーンに置く","墓地に置く","山札に送る","シールドゾーンに置く"]
    elif key in [18,19]:
        txts=["バトルゾーンに出す","手札に加える","マナゾーンに置く","墓地に置く","山札に送る","重ねる","シールドゾーンに置く"]
    elif key in [20,21]:
        txts=["手札に加える","マナゾーンに置く","墓地に置く","山札に送る","シールドゾーンに置く","見る"]
    for i in range(n):
        txt=txts[i]
        pygame.draw.rect(screen, (0,191,255), pygame.Rect(630,145+80*i,780,70))
        gTxt = font.render(txt, True, (255,255,255))
        screen.blit(gTxt, [640,155+80*i])
    pygame.display.flip()
    return

def lr(screen):
    font = pygame.font.SysFont("msgothic", 50)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(1370,280,70,300))
    gTxt = font.render("→", True, (255,255,255))
    screen.blit(gTxt, [1380,405])
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(1370,590,70,300))
    gTxt = font.render("←", True, (255,255,255))
    screen.blit(gTxt, [1380,715])
    pygame.display.flip()
    return

def rect(screen,flag):
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(base[0],base[1],field[0]-200,field[1]-200))
    if flag:
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(1420,110,20,20))
        font = pygame.font.SysFont("msgothic", 25)
        gTxt = font.render("×", True, (255,255,255))
        screen.blit(gTxt, [1417,107])
    pygame.display.flip()
    return

def cardinfo2(card,screen):
    rect(screen,True)
    showcard(screen,card,4,-1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 1420<=x<=1440 and 110<=y<=130:
                    return

def cardinfo(cardkey,save,screen,debug,tmp,current,end,flag,cards,flag2,key,index):
    #ここで範囲外参照が発生している。原因調査中
    #暫定的に、範囲外参照を防ぐことで対処
    if cardkey>=len(cards):
        return
    rect(screen,True)
    cardmenu(screen,key)
    card=cards[cardkey]
    if key in [2,3]:
        if card[1]:
            showcard(screen,card,1,key)
        else:
            showcard(screen,card,0,key)
    elif key in [6,7]:
        if card[1]:
            if card[2]:
                showcard(screen,card,3,key)
            else:
                showcard(screen,card,2,key)
        else:
            showcard(screen,card,0,key)
    elif key in [8,9]:
        if card[1]:
            showcard(screen,card,2,key)
        else:
            showcard(screen,card,0,key)
    elif key in [20,21]:
        if card[1]:
            showcard(screen,card,1,key)
        else:
            showcard(screen,card,0,key)
    else:
        showcard(screen,card,0,key)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 1420<=x<=1440 and 110<=y<=130:
                    rect(screen,True)
                    printcards(tmp[current],screen,flag,cards,flag2)
                    if key in [18,19]:
                        page2(save,screen,debug,tmp,current,end,flag,cards,flag2,key,index)
                    else:
                        page(save,screen,debug,tmp,current,end,flag,cards,flag2,key,index)
                    return
                #ここから下、個別処理
                if 630<=x<=1410:
                    if key%2==0:
                        player=True
                    else:
                        player=False
                    if key in [0,1]:
                        for i in range(7):
                            if 145+80*i<=y<=215+80*i:
                                if i==0:
                                    #バトルゾーンに出す
                                    if any(substring in card[0] for substring in ["_d2f_", "_df_", "_drf_", "_dgf_", "_sf_", "_skf_", "_kf_", "_dmf", "_hf", "_dsf_", "_mf_", "_t2f_", "_ff_", "_lf_","_k_"]):
                                        save=expand(save,card,player)
                                    else:
                                        save=put(save,card,player)
                                elif i==1:
                                    #手札に加える
                                    save=bounce(save,card,player)
                                elif i==2:
                                    #マナゾーンに置く
                                    crystal=False
                                    #crystal=choose(screen,"水晶マナにしますか？")
                                    save=putmana(save,card,player,crystal,False)
                                elif i==3:
                                    #墓地に置く
                                    save=putgrave(save,card,True)
                                elif i==4:
                                    #重ねる
                                    cards2=save[key+8]
                                    tmp2=tmpmake(cards2,2)
                                    current2=0
                                    printcards(tmp2[current2],screen,3,cards2,flag2)
                                    key2=selectcard(tmp2,current2,screen,3,cards2,flag2)
                                    up=choose(screen,"上に重ねますか？")
                                    save=overlap(save,player,key2,card,up)
                                elif i==5:
                                    #超次元ゾーンに置く
                                    save=putdimension(save,card,player)
                                elif i==6:
                                    #シールドゾーンに置く
                                    over=choose(screen,"重ねますか？")
                                    if over:
                                        cards2=save[key-2]
                                        tmp2=tmpmake(cards2,3)
                                        current2=0
                                        printcards(tmp2[current2],screen,4,cards2,flag2)
                                        key2=selectcard(tmp2,current2,screen,4,cards2,flag2)
                                        up=choose(screen,"上に重ねますか？")
                                        if up:
                                            surface=choose(screen,"裏向きですか？")
                                        else:
                                            surface=True
                                        save=overlap2(save,player,key2,card,up,surface)
                                    else:
                                        surface=choose(screen,"裏向きですか？")
                                        save=putshield(save,card,player,surface)
                                del save[key][cardkey]
                                cards=save[key]
                                tmp=tmpmake(cards,0)
                                rect(screen,True)
                                printcards(tmp[current],screen,flag,cards,flag2)
                                page(save,screen,debug,tmp,current,end,flag,save[key],flag2,key,index)
                                return
                    elif key in [2,3]:
                        for i in range(7):
                            if 145+80*i<=y<=215+80*i:
                                if i==0:
                                    #手札に加える
                                    save=bounce(save,card[0],player)
                                    del save[key][cardkey]
                                elif i==1:
                                    #裏返す
                                    save[key][cardkey][1]=not(save[key][cardkey][1])
                                elif i==2:
                                    #墓地に置く
                                    save=putgrave(save,card[0],player)
                                    del save[key][cardkey]
                                elif i==3:
                                    #マナゾーンに置く
                                    crystal=False
                                    #crystal=choose(screen,"水晶マナにしますか？")
                                    save=putmana(save,card[0],player,crystal,False)
                                    del save[key][cardkey]
                                elif i==4:
                                    #山札に送る
                                    up=choose(screen,"デッキの上に置きますか？")
                                    save=gotodeck(save,card[0],player,up)
                                    del save[key][cardkey]
                                elif i==5:
                                    #バトルゾーンに出す
                                    if any(substring in card[0][0] for substring in ["_d2f_", "_df_", "_drf_", "_dgf_", "_sf_", "_skf_", "_kf_", "_dmf", "_hf", "_dsf_", "_mf_", "_t2f_", "_ff_", "_lf_","_k_"]):
                                        save=expand(save,card[0],player)
                                    else:
                                        save=put(save,card[0],player)
                                    del save[key][cardkey]
                                elif i==6:
                                    #構成カードを表示する
                                    if len(card[2])>=2:
                                        rect(screen,True)
                                        cards2=card[2]
                                        tmp2=tmpmake(cards2,0)
                                        current2=0
                                        nflag=4
                                        key2=key+14
                                        printcards(tmp2[current2],screen,nflag,cards2,flag2)
                                        page(save,screen,debug,tmp2,current2,end,nflag,cards2,flag2,key2,cardkey)
                                cards=save[key]
                                tmp=tmpmake(cards,3)
                                rect(screen,True)
                                printcards(tmp[current],screen,flag,cards,flag2)
                                page(save,screen,debug,tmp,current,end,flag,save[key],flag2,key,index)
                                return
                    if key in [4,5]:
                        for i in range(7):
                            if 145+80*i<=y<=215+80*i:
                                if i==0:
                                    if any(substring in card[0] for substring in ["_d2f_", "_df_", "_drf_", "_dgf_", "_sf_", "_skf_", "_kf_", "_dmf", "_hf", "_dsf_", "_mf_", "_t2f_", "_ff_", "_lf_","_k_"]):
                                        save=expand(save,card,player)
                                    else:
                                        save=put(save,card,player)
                                elif i==1:
                                    #マナゾーンに置く
                                    crystal=False
                                    #crystal=choose(screen,"水晶マナにしますか？")
                                    save=putmana(save,card,player,crystal,False)
                                elif i==2:
                                    #墓地に置く
                                    save=putgrave(save,card,True)
                                elif i==3:
                                    #山札に送る
                                    up=choose(screen,"デッキの上に置きますか？")
                                    save=gotodeck(save,card,player,up)
                                elif i==4:
                                    #重ねる
                                    cards2=save[key+4]
                                    tmp2=tmpmake(cards2,2)
                                    current2=0
                                    printcards(tmp2[current2],screen,3,cards2,flag2)
                                    key2=selectcard(tmp2,current2,screen,3,cards2,flag2)
                                    up=choose(screen,"上に重ねますか？")
                                    save=overlap(save,player,key2,card,up)
                                elif i==5:
                                    #超次元ゾーンに置く
                                    save=putdimension(save,card,player)
                                elif i==6:
                                    #シールドゾーンに置く
                                    over=choose(screen,"重ねますか？")
                                    if over:
                                        cards2=save[key-2]
                                        tmp2=tmpmake(cards2,3)
                                        current2=0
                                        printcards(tmp2[current2],screen,4,cards2,flag2)
                                        key2=selectcard(tmp2,current2,screen,4,cards2,flag2)
                                        up=choose(screen,"上に重ねますか？")
                                        if up:
                                            surface=choose(screen,"裏向きですか？")
                                        else:
                                            surface=True
                                        save=overlap2(save,player,key2,card,up,surface)
                                    else:
                                        surface=choose(screen,"裏向きですか？")
                                        save=putshield(save,card,player,surface)
                                del save[key][cardkey]
                                cards=save[key]
                                tmp=tmpmake(cards,0)
                                rect(screen,True)
                                printcards(tmp[current],screen,flag,cards,flag2)
                                page(save,screen,debug,tmp,current,end,flag,save[key],flag2,key,index)
                                return
                    if key in [6,7]:
                        for i in range(8):
                            if 145+80*i<=y<=215+80*i:
                                if i==0:
                                    #タップ/アンタップする
                                    save[key][cardkey][1]=not(save[key][cardkey][1])
                                elif i==1:
                                    #バトルゾーンに出す
                                    if any(substring in card[0][0] for substring in ["_d2f_", "_df_", "_drf_", "_dgf_", "_sf_", "_skf_", "_kf_", "_dmf", "_hf", "_dsf_", "_mf_", "_t2f_", "_ff_", "_lf_","_k_"]):
                                        save=expand(save,card[0],player)
                                    else:
                                        save=put(save,card[0],player)
                                    del save[key][cardkey]
                                elif i==2:
                                    #手札に加える
                                    save=bounce(save,card[0],player)
                                    del save[key][cardkey]
                                elif i==3:
                                    #墓地に置く
                                    save=putgrave(save,card[0],player)
                                    del save[key][cardkey]
                                elif i==4:
                                    #山札に送る
                                    up=choose(screen,"デッキの上に置きますか？")
                                    save=gotodeck(save,card[0],player,up)
                                    del save[key][cardkey]
                                elif i==5:
                                    #裏返す
                                    save[key][cardkey][2]=not(save[key][cardkey][2])
                                elif i==6:
                                    #重ねる
                                    cards2=save[key+2]
                                    tmp2=tmpmake(cards2,2)
                                    current2=0
                                    printcards(tmp2[current2],screen,3,cards2,flag2)
                                    key2=selectcard(tmp2,current2,screen,3,cards2,flag2)
                                    up=choose(screen,"上に重ねますか？")
                                    save=overlap(save,player,key2,card[0],up)
                                    del save[key][cardkey]
                                elif i==7:
                                    #シールドゾーンに置く
                                    over=choose(screen,"重ねますか？")
                                    if over:
                                        cards2=save[key-4]
                                        tmp2=tmpmake(cards2,3)
                                        current2=0
                                        printcards(tmp2[current2],screen,4,cards2,flag2)
                                        key2=selectcard(tmp2,current2,screen,4,cards2,flag2)
                                        up=choose(screen,"上に重ねますか？")
                                        if up:
                                            surface=choose(screen,"裏向きですか？")
                                        else:
                                            surface=True
                                        save=overlap2(save,player,key2,card[0],up,surface)
                                    else:
                                        surface=choose(screen,"裏向きですか？")
                                        save=putshield(save,card[0],player,surface)
                                    del save[key][cardkey]
                                cards=save[key]
                                tmp=tmpmake(cards,1)
                                rect(screen,True)
                                printcards(tmp[current],screen,flag,cards,flag2)
                                page(save,screen,debug,tmp,current,end,flag,save[key],flag2,key,index)
                                return     
                    if key in [8,9]:
                        for i in range(9):
                            if 145+80*i<=y<=215+80*i:
                                if i==0:
                                    #位相を変える
                                    if any(substring in save[key][cardkey][0][0] for substring in ["_d2f_",  "_sf_"]):
                                        save[key][cardkey][5]=not(save[key][cardkey][5])
                                    else:
                                        save[key][cardkey][1]=not(save[key][cardkey][1])
                                elif i==1:
                                    #手札に加える
                                    for i in range(len(card[3])):
                                        save=bounce(save,card[3][i],player)
                                    del save[key][cardkey]
                                elif i==2:
                                    #マナゾーンに置く
                                    for i in range(len(card[3])):
                                        crystal=False
                                        #crystal=choose(screen,"水晶マナにしますか？")
                                        save=putmana(save,card[3][i],player,crystal,True)
                                    del save[key][cardkey]
                                elif i==3:
                                    #墓地に置く
                                    for i in range(len(card[3])):
                                        save=putgrave(save,card[3][i],player)
                                    del save[key][cardkey]
                                elif i==4:
                                    #山札に送る
                                    for i in range(len(card[3])):
                                        up=choose(screen,"デッキの上に置きますか？"+"("+str(i+1)+"枚目)")
                                        save=gotodeck(save,card[3][i],player,up)
                                    del save[key][cardkey]
                                elif i==5:
                                    #構成カードを表示する
                                    if len(card[3])+len(card[4])>=2:
                                        up_or_down=choose(screen,"封印カードの中を見ますか？")
                                        rect(screen,True)
                                        if up_or_down:
                                            cards2=[]
                                            for c in card[4]:
                                                cards2.append([c,True])
                                            tmp2=tmpmake(cards2,3)
                                            current2=0
                                            nflag=4
                                            key2=key+12
                                        else:
                                            cards2=card[3]
                                            tmp2=tmpmake(cards2,0)
                                            current2=0
                                            nflag=4
                                            key2=key+8
                                        printcards(tmp2[current2],screen,nflag,cards2,flag2)
                                        page(save,screen,debug,tmp2,current2,end,nflag,cards2,flag2,key2,cardkey)
                                elif i==6:
                                    #封印する
                                    save=seal(save,player,cardkey)
                                elif i==7:
                                    #超次元ゾーンに置く
                                    for i in range(len(card[3])):
                                        save=putdimension(save,card[3][i],player)
                                    del save[key][cardkey]
                                elif i==8:
                                    #シールドゾーンに置く
                                    for i in range(len(card[3])):
                                        over=choose(screen,"重ねますか？"+"("+str(i+1)+"枚目)")
                                        if over:
                                            cards2=save[key-6]
                                            tmp2=tmpmake(cards2,3)
                                            current2=0
                                            printcards(tmp2[current2],screen,4,cards2,flag2)
                                            key2=selectcard(tmp2,current2,screen,4,cards2,flag2)
                                            up=choose(screen,"上に重ねますか？"+"("+str(i+1)+"枚目)")
                                            if up:
                                                surface=choose(screen,"裏向きですか？")
                                            else:
                                                surface=True
                                            save=overlap2(save,player,key2,card[3][i],up,surface)
                                        else:
                                            surface=choose("裏向きですか？"+"("+str(i+1)+"枚目)")
                                            save=putshield(save,card[3][i],player,surface)
                                    del save[key][cardkey]
                                cards=save[key]
                                tmp=tmpmake(cards,2)
                                printcards(tmp[current],screen,flag,cards,flag2)
                                page(save,screen,debug,tmp,current,end,flag,save[key],flag2,key,index)
                                return
                    if key in [10,11]:
                        for i in range(6):
                            if 145+80*i<=y<=215+80*i:
                                if i==0:
                                    #バトルゾーンに出す
                                    if any(substring in card[0] for substring in ["_d2f_", "_df_", "_drf_", "_dgf_", "_sf_", "_skf_", "_kf_", "_dmf", "_hf", "_dsf_", "_mf_", "_t2f_", "_ff_", "_lf_","_k_"]):
                                        save=expand(save,card,player)
                                    else:
                                        save=put(save,card,player)
                                elif i==1:
                                    #手札に加える
                                    save=bounce(save,card,player)
                                elif i==2:
                                    #マナゾーンに置く
                                    crystal=False
                                    #crystal=choose(screen,"水晶マナにしますか？")
                                    save=putmana(save,card,player,crystal,False)
                                elif i==3:
                                    #山札に送る
                                    up=choose(screen,"デッキの上に置きますか？")
                                    save=gotodeck(save,card,player,up)
                                elif i==4:
                                    #重ねる
                                    cards2=save[key-2]
                                    tmp2=tmpmake(cards2,2)
                                    current2=0
                                    printcards(tmp2[current2],screen,3,cards2,flag2)
                                    key2=selectcard(tmp2,current2,screen,3,cards2,flag2)
                                    up=choose(screen,"上に重ねますか？")
                                    save=overlap(save,player,key2,card,up)
                                elif i==5:
                                    #シールドゾーンに置く
                                    over=choose(screen,"重ねますか？")
                                    if over:
                                        cards2=save[key-8]
                                        tmp2=tmpmake(cards2,3)
                                        current2=0
                                        printcards(tmp2[current2],screen,4,cards2,flag2)
                                        key2=selectcard(tmp2,current2,screen,4,cards2,flag2)
                                        up=choose(screen,"上に重ねますか？")
                                        if up:
                                            surface=choose(screen,"裏向きですか？")
                                        else:
                                            surface=True
                                        save=overlap2(save,player,key2,card,up,surface)
                                    else:
                                        surface=choose(screen,"裏向きですか？")
                                        save=putshield(save,card,player,surface)
                                del save[key][cardkey]
                                cards=save[key]
                                tmp=tmpmake(cards,0)
                                printcards(tmp[current],screen,flag,cards,flag2)
                                page(save,screen,debug,tmp,current,end,flag,save[key],flag2,key,index)
                                return
                    if key in [12,13]:
                        for i in range(6):
                            if 145+80*i<=y<=215+80*i:
                                if i==0:
                                    #バトルゾーンに出す
                                    if any(substring in card[0] for substring in ["_d2f_", "_df_", "_drf_", "_dgf_", "_sf_", "_skf_", "_kf_", "_dmf", "_hf", "_dsf_", "_mf_", "_t2f_", "_ff_", "_lf_","_k_"]):
                                        save=expand(save,card,player)
                                    else:
                                        save=put(save,card,player)
                                elif i==1:
                                    #手札に加える
                                    save=bounce(save,card,player)
                                elif i==2:
                                    #マナゾーンに置く
                                    crystal=False
                                    #crystal=choose(screen,"水晶マナにしますか？")
                                    save=putmana(save,card,player,crystal,False)
                                elif i==3:
                                    #墓地に置く
                                    save=putgrave(save,card,True)
                                elif i==4:
                                    #山札に送る
                                    up=choose(screen,"デッキの上に置きますか？")
                                    save=gotodeck(save,card,player,up)
                                elif i==5:
                                    #重ねる
                                    cards2=save[key-4]
                                    tmp2=tmpmake(cards2,2)
                                    current2=0
                                    printcards(tmp2[current2],screen,4,cards2,flag2)
                                    key2=selectcard(tmp2,current2,screen,4,cards2,flag2)
                                    up=choose(screen,"上に重ねますか？")
                                    save=overlap(save,player,key2,card,up)
                                del save[key][cardkey]
                                cards=save[key]
                                tmp=tmpmake(cards,0)
                                printcards(tmp[current],screen,flag,cards,flag2)
                                page(save,screen,debug,tmp,current,end,flag,save[key],flag2,key,index)
                                return
                    if key in [16,17]:
                        key3=key-8
                        for i in range(6):
                            if 145+80*i<=y<=215+80*i:
                                if i==0:
                                    #バトルゾーンを移動する
                                    cards2=save[key3]
                                    tmp2=tmpmake(cards2,2)
                                    current2=0
                                    printcards(tmp2[current2],screen,3,cards2,flag2)
                                    key2=selectcard(tmp2,current2,screen,3,cards2,flag2)
                                    up=choose(screen,"上に重ねますか？")
                                    save=overlap(save,player,key2,card,up)
                                elif i==1:
                                    #手札に加える
                                    save=bounce(save,card,player)
                                elif i==2:
                                    #敵の構成カードをマナ送りにしたときにバグる
                                    #マナゾーンに置く
                                    crystal=False
                                    #crystal=choose(screen,"水晶マナにしますか？")
                                    save=putmana(save,card,player,crystal,True)
                                elif i==3:
                                    #墓地に置く
                                    save=putgrave(save,card,player)
                                elif i==4:
                                    #山札に送る
                                    up=choose(screen,"デッキの上に置きますか？")
                                    save=gotodeck(save,card,player,up)
                                elif i==5:
                                    #シールドゾーンに置く
                                    over=choose(screen,"重ねますか？")
                                    if over:
                                        cards2=save[key-14]
                                        tmp2=tmpmake(cards2,3)
                                        current2=0
                                        printcards(tmp2[current2],screen,4,cards2,flag2)
                                        key2=selectcard(tmp2,current2,screen,4,cards2,flag2)
                                        up=choose(screen,"上に重ねますか？")
                                        if up:
                                            surface=choose(screen,"裏向きですか？")
                                        else:
                                            surface=True
                                        save=overlap2(save,player,key2,card,up,surface)
                                    else:
                                        surface=choose(screen,"裏向きですか？")
                                        save=putshield(save,card,player,surface)
                                del save[key3][index][3][cardkey]
                                #退化
                                if cardkey==0 and len(save[key3][index][3])>0:
                                    save[key3][index][0]=save[key3][index][3][0]
                                #零龍卍誕
                                if save[key3][index][0][0]=="d_zg_001":
                                    if len(save[key3][index][3])==5:
                                        zeronbantan(save,player)
                                        del save[key3][index]
                                return
                    if key in [18,19]:
                        for i in range(7):
                            if 145+80*i<=y<=215+80*i:
                                if i==0:
                                    #バトルゾーンに出す
                                    if any(substring in card[0] for substring in ["_d2f_", "_df_", "_drf_", "_dgf_", "_sf_", "_skf_", "_kf_", "_dmf", "_hf", "_dsf_", "_mf_", "_t2f_", "_ff_", "_lf_","_k_"]):
                                        save=expand(save,card,player)
                                    else:
                                        save=put(save,card,player)
                                elif i==1:
                                    #手札に加える
                                    save=bounce(save,card,player)
                                elif i==2:
                                    #マナゾーンに置く
                                    crystal=False
                                    #crystal=choose(screen,"水晶マナにしますか？")
                                    save=putmana(save,card,player,crystal,False)
                                elif i==3:
                                    #墓地に置く
                                    save=putgrave(save,card,True)
                                elif i==4:
                                    #山札に送る
                                    up=choose(screen,"デッキの上に置きますか？")
                                    save=gotodeck(save,card,player,up)
                                elif i==5:
                                    #重ねる
                                    cards2=save[key-10]
                                    tmp2=tmpmake(cards2,2)
                                    current2=0
                                    printcards(tmp2[current2],screen,3,cards2,flag2)
                                    key2=selectcard(tmp2,current2,screen,3,cards2,flag2)
                                    up=choose(screen,"上に重ねますか？")
                                    save=overlap(save,player,key2,card,up)
                                elif i==6:
                                    #シールドゾーンに置く
                                    over=choose(screen,"重ねますか？")
                                    if over:
                                        cards2=save[key-16]
                                        tmp2=tmpmake(cards2,3)
                                        current2=0
                                        printcards(tmp2[current2],screen,4,cards2,flag2)
                                        key2=selectcard(tmp2,current2,screen,4,cards2,flag2)
                                        up=choose(screen,"上に重ねますか？")
                                        if up:
                                            surface=choose(screen,"裏向きですか？")
                                        else:
                                            surface=True
                                        save=overlap2(save,player,key2,card,up,surface)
                                    else:
                                        surface=choose(screen,"裏向きですか？")
                                        save=putshield(save,card,player,surface)
                                del cards[cardkey]
                                tmp=tmpmake(cards,0)
                                printcards(tmp[current],screen,flag,cards,flag2)
                                page2(save,screen,debug,tmp,current,end,flag,cards,flag2,key,index)
                                return
                    if key in [20,21]:
                        key3=key-12
                        for i in range(6):
                            if 145+80*i<=y<=215+80*i:
                                if i==0:
                                    #手札に加える
                                    save=bounce(save,card[0],player)
                                elif i==1:
                                    #マナゾーンに置く
                                    crystal=False
                                    #crystal=choose(screen,"水晶マナにしますか？")
                                    save=putmana(save,card[0],player,crystal,False)
                                elif i==2:
                                    #墓地に置く
                                    save=putgrave(save,card[0],True)
                                elif i==3:
                                    #山札に送る
                                    up=choose(screen,"デッキの上に置きますか？")
                                    save=gotodeck(save,card[0],player,up)
                                elif i==4:
                                    #シールドゾーンに置く
                                    over=choose(screen,"重ねますか？")
                                    if over:
                                        cards2=save[key-16]
                                        tmp2=tmpmake(cards2,3)
                                        current2=0
                                        printcards(tmp2[current2],screen,4,cards2,flag2)
                                        key2=selectcard(tmp2,current2,screen,4,cards2,flag2)
                                        up=choose(screen,"上に重ねますか？")
                                        if up:
                                            surface=choose(screen,"裏向きですか？")
                                        else:
                                            surface=True
                                        save=overlap2(save,player,key2,card[0],up,surface)
                                    else:
                                        surface=choose(screen,"裏向きですか？")
                                        save=putshield(save,card[0],player,surface)
                                elif i==5:
                                    #見る
                                    wcard=save[key3][index][4][cardkey]
                                    cardinfo2(wcard,screen)
                                    return
                                del save[key3][index][4][cardkey]
                                #封印解除
                                if len(save[key3][index][4])==0:
                                    save[key3][index][2]=False
                                    if save[key3][index][0][0]=="r_k_001":
                                        del save[key3][index]
                                        kndn=['r_kc_001', '伝説の禁断 ドキンダムX', [], 99, None, 99999, ['r'], False, True, False, True, False, 'kc', ['T-Breaker'], False, False]
                                        save=put(save,kndn,player)
                                    elif  save[key3][index][0][0]=="rg_skf_001":
                                        del save[key3][index]
                                        save=kndnbigbun(save,player)
                                return

def printcards(tmp,screen,mode,cards,flag):
    w=200
    h=288
    #Dスイッチの処理→カードの状態？
    #mode:1-showcards,2-showmanazone,3-showbattlezone,4-showshield
    rect(screen,flag)
    t=[0]*len(tmp)
    for i in range(len(tmp)):
        flg=False
        t[i]=pygame.image.load(tmp[i])
        t[i]=pygame.transform.scale(t[i], (w, h))
        if mode==1:
            if cards[i][11]:
                t[i]=pygame.transform.rotate(t[i], 270)
                flg=True
        elif mode==2:
            if cards[i][1]:
                t[i]=pygame.transform.rotate(t[i], 270)
                flg=True
        elif mode==3:
            if cards[i][1]:
                t[i]=pygame.transform.rotate(t[i], 270)
                flg=True
        if i<=5:
            if flg:
                screen.blit(t[i], (base[0]+10*(i+1)+w*i,base[1]+54))
            else:
                screen.blit(t[i], (base[0]+10*(i+1)+w*i,base[1]+10))
        elif 6<=i<=11:
            if flg:
                screen.blit(t[i], (base[0]+10*(i%6+1)+w*(i%6),base[1]+64+height))
            else:
                screen.blit(t[i], (base[0]+10*(i%6+1)+w*(i%6),base[1]+20+height))
        elif 12<=i<=17:
            if flg:
                screen.blit(t[i], (base[0]+10*(i%6+1)+w*(i%6),base[1]+74+height*2))
            else:
                screen.blit(t[i], (base[0]+10*(i%6+1)+w*(i%6),base[1]+30+height*2))
        elif 18<=i<=23:
            if flg:
                screen.blit(t[i], (base[0]+10*(i%6+1)+w*(i%6),base[1]+84+height*3))
            else:
                screen.blit(t[i], (base[0]+10*(i%6+1)+w*(i%6),base[1]+40+height*3))
    pygame.display.flip()
    return

def info(save,screen,debug):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 1420<=x<=1440 and 110<=y<=130:
                    recover(save,screen,debug)
                    return

def selectcard(tmp,current,screen,flag,cards,flag2):
    lr(screen)
    end=len(tmp[current])//6
    if len(tmp[current])%6==0:
        end-=1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 1370<=x<=1440:
                    if 280<=y<=580:
                        current+=1
                        if current==4 or len(tmp[current])==0:
                            current=0
                        end=len(tmp[current])//6
                        if len(tmp[current])%6==0:
                            end-=1
                        printcards(tmp[current],screen,flag,cards,flag2)
                        selectcard(tmp,current,screen,flag,cards,flag2)
                        return
                    elif 590<=y<=890:
                        current-=1
                        if current==-1:
                            current=3
                            while len(tmp[current])==0:
                                current-=1
                        end=len(tmp[current])//6
                        if len(tmp[current])%6==0:
                            end-=1
                        printcards(tmp[current],screen,flag,cards,flag2)
                        selectcard(tmp,current,screen,flag,cards,flag2)
                        return
                for i in range(end+1):
                    if i==end:
                        if 110+144*i<=y<=398+144*i:
                            edge=len(tmp[current])%6-1
                            if edge==-1:
                                edge=6
                            for j in range(edge+1):
                                if 110+210*j<=x<=310+210*j:
                                    return 24*current+6*i+j
                    else:
                        if 110+144*i<=y<=254+144*i:
                            for j in range(6):
                                if 110+210*j<=x<=310+210*j:
                                    return 24*current+6*i+j

def page(save,screen,debug,tmp,current,end,flag,cards,flag2,key,index):
    lr(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 1420<=x<=1440 and 110<=y<=130:
                    recover(save,screen,debug)
                    return
                if 1370<=x<=1440:
                    if 280<=y<=580:
                        current+=1
                        if current==4 or len(tmp[current])==0:
                            current=0
                        end=len(tmp[current])//6
                        if len(tmp[current])%6==0:
                            end-=1
                        printcards(tmp[current],screen,flag,cards,flag2)
                        page(save,screen,debug,tmp,current,end,flag,cards,flag2,key,index)
                        return
                    elif 590<=y<=890:
                        current-=1
                        if current==-1:
                            current=3
                            while len(tmp[current])==0:
                                current-=1
                        end=len(tmp[current])//6
                        if len(tmp[current])%6==0:
                            end-=1
                        printcards(tmp[current],screen,flag,cards,flag2)
                        page(save,screen,debug,tmp,current,end,flag,cards,flag2,key,index)
                        return
                for i in range(end+1):
                    if i==end:
                        if 110+144*i<=y<=398+144*i:
                            edge=len(tmp[current])%6-1
                            if edge==-1:
                                edge=5
                            for j in range(edge+1):
                                if 110+210*j<=x<=310+210*j:
                                    cardkey=24*current+6*i+j
                                    cardinfo(cardkey,save,screen,debug,tmp,current,end,flag,cards,flag2,key,index)
                                    return
                    else:
                        if 110+144*i<=y<=254+144*i:
                            for j in range(6):
                                if 110+210*j<=x<=310+210*j:
                                    cardkey=24*current+6*i+j
                                    cardinfo(cardkey,save,screen,debug,tmp,current,end,flag,cards,flag2,key,index)
                                    return

def page2(save,screen,debug,tmp,current,end,flag,cards,flag2,key,index):
    lr(screen)
    while True:
        if len(cards)==0:
            recover(save,screen,debug)
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 1370<=x<=1440:
                    if 280<=y<=580:
                        current+=1
                        if current==4 or len(tmp[current])==0:
                            current=0
                        end=len(tmp[current])//6
                        if len(tmp[current])%6==0:
                            end-=1
                        printcards(tmp[current],screen,flag,cards,flag2)
                        page2(save,screen,debug,tmp,current,end,flag,cards,flag2,key,index)
                        return
                    elif 590<=y<=890:
                        current-=1
                        if current==-1:
                            current=3
                            while len(tmp[current])==0:
                                current-=1
                        end=len(tmp[current])//6
                        if len(tmp[current])%6==0:
                            end-=1
                        printcards(tmp[current],screen,flag,cards,flag2)
                        page2(save,screen,debug,tmp,current,end,flag,cards,flag2,key,index)
                        return
                for i in range(end+1):
                    if i==end:
                        if 110+144*i<=y<=398+144*i:
                            edge=len(tmp[current])%6-1
                            if edge==-1:
                                edge=5
                            for j in range(edge+1):
                                if 110+210*j<=x<=310+210*j:
                                    cardkey=24*current+6*i+j
                                    cardinfo(cardkey,save,screen,debug,tmp,current,end,flag,cards,flag2,key,index)
                                    return
                    else:
                        if 110+144*i<=y<=254+144*i:
                            for j in range(6):
                                if 110+210*j<=x<=310+210*j:
                                    cardkey=24*current+6*i+j
                                    cardinfo(cardkey,save,screen,debug,tmp,current,end,flag,cards,flag2,key,index)
                                    return

def tmpmake(cards,mode):
    tmp=[[],[],[],[]]
    #mode:0-showcards,1-showmanazone,2-showbattlezone,3-showshield
    for i in range(len(cards)):
        if mode==0:
            buf="cards/"+cards[i][0]
        elif mode in [1,2]:
            if cards[i][2]:
                buf="uramen/ura"
            else:
                buf="cards/"+cards[i][0][0]
        elif mode==3:
            if cards[i][1]:
                buf="uramen/ura"
            else:
                buf="cards/"+cards[i][0][0]
        if i<=23:
            tmp[0].append("GUI/image/"+buf+".jpg")
        elif i<=47:
            tmp[1].append("GUI/image/"+buf+".jpg")
        elif i<=71:
            tmp[2].append("GUI/image/"+buf+".jpg")
        else:
            tmp[3].append("GUI/image/"+buf+".jpg")
    return tmp

def showcards(save,screen,flag,key,debug):
    cards=save[key]
    tmp=tmpmake(cards,0)
    current=0
    end=len(tmp[current])//6
    if len(tmp[current])%6==0:
        end-=1
    printcards(tmp[current],screen,1,cards,flag)
    page(save,screen,debug,tmp,current,end,1,cards,flag,key,-1)
    return

def showmanazone(save,screen,flag,key,debug):
    cards=save[key]
    tmp=tmpmake(cards,1)
    current=0
    end=len(tmp[current])//6
    if len(tmp[current])%6==0:
        end-=1
    printcards(tmp[current],screen,2,cards,flag)
    page(save,screen,debug,tmp,current,end,2,cards,flag,key,-1)
    return

def showbattlezone(save,screen,flag,key,debug):
    cards=save[key]
    tmp=tmpmake(cards,2)
    current=0
    end=len(tmp[current])//6
    if len(tmp[current])%6==0:
        end-=1
    printcards(tmp[current],screen,3,cards,flag)
    page(save,screen,debug,tmp,current,end,3,cards,flag,key,-1)
    return

def showshield(save,screen,flag,key,debug):
    cards=save[key]
    tmp=tmpmake(cards,3)
    current=0
    end=len(tmp[current])//6
    if len(tmp[current])%6==0:
        end-=1
    printcards(tmp[current],screen,4,cards,flag)
    page(save,screen,debug,tmp,current,end,4,cards,flag,key,-1)
    return

def sshield(screen):
    for i in range(5):
        img = pygame.image.load("GUI/image/uramen/ura.jpg")
        img = pygame.transform.scale(img, (width, height))
        img2 = pygame.transform.rotate(img, 180)
        img2 = pygame.transform.scale(img2, (width, height))
        screen.blit(img, ((downbase[0]-110)-width*i, downbase[1]))
        screen.blit(img2, ((upbase[0]+110)+width*i, upbase[1]))
        pygame.display.flip()
        time.sleep(0.5)

#表向きカードが考慮されていませんよ
def shield(screen,flag,save):
    img = pygame.image.load("GUI/image/uramen/ura.jpg")
    if flag:
        for i in range(len(save[2])): 
            img = pygame.transform.scale(img, (width, height))
            screen.blit(img, ((downbase[0]-110)-width*i, downbase[1]))
    else:
        img2 = pygame.transform.rotate(img, 180)
        for i in range(len(save[3])):
            img2 = pygame.transform.scale(img2, (width, height))
            screen.blit(img2, ((upbase[0]+110)+width*i, upbase[1]))
    pygame.display.flip()

def recover(save,screen,flag):
    screen.fill(fieldcolor)
    deck(screen,save[0],save[1])
    dimension(screen,save[12],save[13])
    grdeck(screen,save[14],save[15])
    shield(screen,True,save)
    shield(screen,False,save)
    manazone(screen,save[6],save[7])
    battlezone(screen,save[8],save[9])
    graveyard(screen,save[10],save[11])
    if flag==1:
        debugmenu(screen)
    elif flag==2:
        menu(screen)
    else:
        emenu(screen)
    pygame.display.flip()
    return

def deckinfo(save,flag,screen,debug):
    font = pygame.font.SysFont("msgothic", 30)
    if flag:
        pygame.draw.rect(screen, (0,191,255), pygame.Rect(downbase[0]-10,downbase[1]+100,120,50))
        gTxt = font.render(str(len(save[0]))+"枚", True, (255,255,255))
        screen.blit(gTxt, [downbase[0]+10,downbase[1]+110])
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(downbase[0]+80,downbase[1]+110,20,20))
        font = pygame.font.SysFont("msgothic", 25)
        gTxt = font.render("×", True, (255,255,255))
        screen.blit(gTxt, [downbase[0]+77,downbase[1]+107])
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if (downbase[0]+80<=x<=downbase[0]+100 and downbase[1]+110<=y<=downbase[1]+130):
                        recover(save,screen,debug)
                        return
    else:
        pygame.draw.rect(screen, (0,191,255), pygame.Rect(upbase[0]-10,upbase[1]+100,120,50))
        gTxt = font.render(str(len(save[1]))+"枚", True, (255,255,255))
        screen.blit(gTxt, [upbase[0]+10,upbase[1]+110])
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(upbase[0]+80,upbase[1]+110,20,20))
        font = pygame.font.SysFont("msgothic", 25)
        gTxt = font.render("×", True, (255,255,255))
        screen.blit(gTxt, [upbase[0]+77,upbase[1]+107])
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if (upbase[0]+80<=x<=upbase[0]+100 and upbase[1]+110<=y<=upbase[1]+130):
                        recover(save,screen,debug)
                        return

def grdeckinfo(save,flag,screen,debug):
    font = pygame.font.SysFont("msgothic", 30)
    if flag:
        pygame.draw.rect(screen, (0,191,255), pygame.Rect(downbase[0]+2*width+10,downbase[1]+110+height,120,50))
        gTxt = font.render(str(len(save[14]))+"枚", True, (255,255,255))
        screen.blit(gTxt, [downbase[0]+2*width+30,downbase[1]+120+height])
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(downbase[0]+2*width+100,downbase[1]+120+height,20,20))
        font = pygame.font.SysFont("msgothic", 25)
        gTxt = font.render("×", True, (255,255,255))
        screen.blit(gTxt, [downbase[0]+2*width+97,downbase[1]+117+height])
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if (downbase[0]+2*width+100<=x<=downbase[0]+2*width+120 and downbase[1]+120+height<=y<=downbase[1]+140+height):
                        recover(save,screen,debug)
                        return
    else:
        pygame.draw.rect(screen, (0,191,255), pygame.Rect(upbase[0]-30-2*width,upbase[1]-height+90,120,50))
        gTxt = font.render(str(len(save[15]))+"枚", True, (255,255,255))
        screen.blit(gTxt, [upbase[0]-10-2*width,upbase[1]-height+100])
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(upbase[0]+60-2*width,upbase[1]-height+100,20,20))
        font = pygame.font.SysFont("msgothic", 25)
        gTxt = font.render("×", True, (255,255,255))
        screen.blit(gTxt, [upbase[0]+57-2*width,upbase[1]-height+97])
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if (upbase[0]+60-2*width<=x<=upbase[0]+80-2*width and upbase[1]-height+100<=y<=upbase[1]-height+120):
                        recover(save,screen,debug)
                        return

def decklist(screen,flag,advance,deckimg):
    #size=(500, 620)
    #リスト追加したら更新して
    kirikae=100
    if advance:
        card=(50,72)
        div=10
        max=5
    else:
        card=(62.5,124)
        div=8
        max=23
    font = pygame.font.SysFont("msgothic", 50)
    rect(screen,False)
    if flag:
        gTxt = font.render("自分のデッキを選択", True, (255,255,255))
    else:
        gTxt = font.render("相手のデッキを選択", True, (255,255,255))
    screen.blit(gTxt, (550,110))
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(100,810,(field[0]-200)//2,90))
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(100+(field[0]-200)//2,810,(field[0]-200)//2,90))
    gTxt = font.render("←", True, (255,255,255))
    screen.blit(gTxt, (412,830))
    gTxt = font.render("→", True, (255,255,255))
    screen.blit(gTxt, (412+(field[0]-200)//2,830))
    num=1
    #なおす
    RootPass="GUI/image/cards/"
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(200,180,500,620))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(850,180,500,620))
    for i in range(len(deckimg[num-1])):
        cardpass=deckimg[num-1][i]
        Pass=RootPass+cardpass+".jpg"
        img = pygame.image.load(Pass)
        img = pygame.transform.scale(img, card)
        screen.blit(img, (200+card[0]*(i%div), 180+card[1]*(i//div)))
    for i in range(len(deckimg[num])):
        cardpass=deckimg[num][i]
        Pass=RootPass+cardpass+".jpg"
        img = pygame.image.load(Pass)
        img = pygame.transform.scale(img, card)
        screen.blit(img, (850+card[0]*(i%div), 180+card[1]*(i//div)))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 110<=y<=730:
                    if 200<=x<=700:
                        if advance:
                            num+=kirikae
                        return "deck"+str(num-1)
                    elif 850<=x<=1350:
                        if advance:
                            num+=kirikae
                        return "deck"+str(num)
                elif 750<=y<=900:
                    if 100<=x<=100+(field[0]-200)//2:
                        if num==1:
                            num=max
                        else:
                            num-=2
                    elif 100+(field[0]-200)//2<x<=field[0]-100:
                        if num==max:
                            num=1
                        else:
                            num+=2
                    #なおす
                    pygame.draw.rect(screen, (255,255,255), pygame.Rect(200,180,500,620))
                    pygame.draw.rect(screen, (255,255,255), pygame.Rect(850,180,500,620))
                    for i in range(len(deckimg[num-1])):
                        cardpass=deckimg[num-1][i]
                        Pass=RootPass+cardpass+".jpg"
                        img = pygame.image.load(Pass)
                        img = pygame.transform.scale(img, card)
                        screen.blit(img, (200+card[0]*(i%div), 180+card[1]*(i//div)))
                    for i in range(len(deckimg[num])):
                        cardpass=deckimg[num][i]
                        Pass=RootPass+cardpass+".jpg"
                        img = pygame.image.load(Pass)
                        img = pygame.transform.scale(img, card)
                        screen.blit(img, (850+card[0]*(i%div), 180+card[1]*(i//div)))
                    pygame.display.flip()

def choose(screen,message):
    rect(screen,False)
    font = pygame.font.SysFont("msgothic", 100)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(base[0],base[1]+600,(field[0]-200)//2,200))
    gTxt = font.render("は　い", True, (255,255,255))
    screen.blit(gTxt, [base[0]+187,base[1]+650])
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(base[0]+(field[0]-200)//2,base[1]+600,(field[0]-200)//2,200))
    gTxt = font.render("いいえ", True, (255,255,255))
    screen.blit(gTxt, [base[0]+(field[0]-200)//2+187,base[1]+650])
    #messageを適切な長さで分割して複数行で表示する
    tmp=[]
    point=0
    current=""
    while len(message)>0:
        c=message[0]
        current+=c
        if len(c)==len(c.encode()):
            point+=0.5
        else:
            point+=1
        message=message[1:]
        if point>25 or c=="。" or c=="？":
            tmp.append(current)
            point=0
            current=""
    if current!="":
        tmp.append(current)
    font = pygame.font.SysFont("msgothic", 50)
    for i in range(len(tmp)):
        gTxt = font.render(tmp[i], True, (255,255,255))
        screen.blit(gTxt, [base[0]+20,base[1]+10*(i+1)+50*i])
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if base[1]+600<=y<=base[1]+800:
                        if base[0]<=x<=base[0]+(field[0]-200)//2:
                            return True
                        elif base[0]+(field[0]-200)//2<x<=field[0]-100:
                            return False

def number(screen,message):
    #数字を聞く ∞はとりあえず-1とする
    n=0
    rect(screen,False)
    font = pygame.font.SysFont("msgothic", 100)
    font2 = pygame.font.SysFont("msgothic", 50)
    #この辺数字仕様にする
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(base[0]+20,base[1]+420,120,120))
    gTxt = font.render("1", True, (255,255,255))
    screen.blit(gTxt, [base[0]+50,base[1]+430])
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(base[0]+140,base[1]+420,120,120))
    gTxt = font.render("2", True, (255,255,255))
    screen.blit(gTxt, [base[0]+170,base[1]+430])
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(base[0]+260,base[1]+420,120,120))
    gTxt = font.render("3", True, (255,255,255))
    screen.blit(gTxt, [base[0]+290,base[1]+430])
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(base[0]+380,base[1]+420,120,120))
    gTxt = font.render("0", True, (255,255,255))
    screen.blit(gTxt, [base[0]+410,base[1]+430])
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(base[0]+500,base[1]+420,140,120))
    gTxt = font2.render("Reset", True, (255,255,255))
    screen.blit(gTxt, [base[0]+510,base[1]+455])
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(base[0]+20,base[1]+540,120,120))
    gTxt = font.render("4", True, (255,255,255))
    screen.blit(gTxt, [base[0]+50,base[1]+550])
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(base[0]+140,base[1]+540,120,120))
    gTxt = font.render("5", True, (255,255,255))
    screen.blit(gTxt, [base[0]+170,base[1]+550])
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(base[0]+260,base[1]+540,120,120))
    gTxt = font.render("6", True, (255,255,255))
    screen.blit(gTxt, [base[0]+290,base[1]+550])
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(base[0]+380,base[1]+540,120,120))
    gTxt = font.render("∞", True, (255,255,255))
    screen.blit(gTxt, [base[0]+390,base[1]+550])
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(base[0]+500,base[1]+540,140,120))
    gTxt = font2.render("Rand", True, (255,255,255))
    screen.blit(gTxt, [base[0]+510,base[1]+575])
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(base[0]+20,base[1]+660,120,120))
    gTxt = font.render("7", True, (255,255,255))
    screen.blit(gTxt, [base[0]+50,base[1]+670])
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(base[0]+140,base[1]+660,120,120))
    gTxt = font.render("8", True, (255,255,255))
    screen.blit(gTxt, [base[0]+170,base[1]+670])
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(base[0]+260,base[1]+660,120,120))
    gTxt = font.render("9", True, (255,255,255))
    screen.blit(gTxt, [base[0]+290,base[1]+670])
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(base[0]+380,base[1]+660,120,120))
    gTxt = font.render("←", True, (255,255,255))
    screen.blit(gTxt, [base[0]+390,base[1]+670])
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(base[0]+500,base[1]+660,140,120))
    gTxt = font2.render("End", True, (255,255,255))
    screen.blit(gTxt, [base[0]+510,base[1]+695])
    pygame.draw.rect(screen, (0,255,0), pygame.Rect(base[0]+650,base[1]+660,680,120))
    gTxt = font.render(str(n), True, (255,255,255))
    screen.blit(gTxt, [base[0]+660,base[1]+670])
    #messageを適切な長さで分割して複数行で表示する
    tmp=[]
    point=0
    current=""
    while len(message)>0:
        c=message[0]
        current+=c
        if len(c)==len(c.encode()):
            point+=0.5
        else:
            point+=1
        message=message[1:]
        if point>25 or c=="。" or c=="？":
            tmp.append(current)
            point=0
            current=""
    if current!="":
        tmp.append(current)
    font = pygame.font.SysFont("msgothic", 50)
    for i in range(len(tmp)):
        gTxt = font.render(tmp[i], True, (255,255,255))
        screen.blit(gTxt, [base[0]+20,base[1]+10*(i+1)+50*i])
    pygame.display.flip()
    font = pygame.font.SysFont("msgothic", 100)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if base[1]+420<=y<=base[1]+540:
                    if base[0]+20<=x<=base[0]+140:
                        if n!=-1:
                            n=n*10+1
                            pygame.draw.rect(screen, (0,255,0), pygame.Rect(base[0]+650,base[1]+660,680,120))
                            gTxt = font.render(str(n), True, (255,255,255))
                            screen.blit(gTxt, [base[0]+660,base[1]+670])
                            pygame.display.flip()
                    if base[0]+140<x<=base[0]+260:
                        if n!=-1:
                            n=n*10+2
                            pygame.draw.rect(screen, (0,255,0), pygame.Rect(base[0]+650,base[1]+660,680,120))
                            gTxt = font.render(str(n), True, (255,255,255))
                            screen.blit(gTxt, [base[0]+660,base[1]+670])
                            pygame.display.flip()
                    if base[0]+260<x<=base[0]+380:
                        if n!=-1:
                            n=n*10+3
                            pygame.draw.rect(screen, (0,255,0), pygame.Rect(base[0]+650,base[1]+660,680,120))
                            gTxt = font.render(str(n), True, (255,255,255))
                            screen.blit(gTxt, [base[0]+660,base[1]+670])
                            pygame.display.flip()
                    if base[0]+380<x<=base[0]+500:
                        if n!=-1:
                            n=n*10+0
                            pygame.draw.rect(screen, (0,255,0), pygame.Rect(base[0]+650,base[1]+660,680,120))
                            gTxt = font.render(str(n), True, (255,255,255))
                            screen.blit(gTxt, [base[0]+660,base[1]+670])
                            pygame.display.flip()
                    if base[0]+500<x<=base[0]+640:
                        n=0
                        pygame.draw.rect(screen, (0,255,0), pygame.Rect(base[0]+650,base[1]+660,680,120))
                        gTxt = font.render(str(n), True, (255,255,255))
                        screen.blit(gTxt, [base[0]+660,base[1]+670])
                        pygame.display.flip()
                if base[1]+540<y<=base[1]+660:
                    if base[0]+20<=x<=base[0]+140:
                        if n!=-1:
                            n=n*10+4
                            pygame.draw.rect(screen, (0,255,0), pygame.Rect(base[0]+650,base[1]+660,680,120))
                            gTxt = font.render(str(n), True, (255,255,255))
                            screen.blit(gTxt, [base[0]+660,base[1]+670])
                            pygame.display.flip()
                    if base[0]+140<x<=base[0]+260:
                        if n!=-1:
                            n=n*10+5
                            pygame.draw.rect(screen, (0,255,0), pygame.Rect(base[0]+650,base[1]+660,680,120))
                            gTxt = font.render(str(n), True, (255,255,255))
                            screen.blit(gTxt, [base[0]+660,base[1]+670])
                            pygame.display.flip()
                    if base[0]+260<x<=base[0]+380:
                        if n!=-1:
                            n=n*10+6
                            pygame.draw.rect(screen, (0,255,0), pygame.Rect(base[0]+650,base[1]+660,680,120))
                            gTxt = font.render(str(n), True, (255,255,255))
                            screen.blit(gTxt, [base[0]+660,base[1]+670])
                            pygame.display.flip()
                    if base[0]+380<x<=base[0]+500:
                        n=-1
                        pygame.draw.rect(screen, (0,255,0), pygame.Rect(base[0]+650,base[1]+660,680,120))
                        gTxt = font.render("∞", True, (255,255,255))
                        screen.blit(gTxt, [base[0]+660,base[1]+670])
                        pygame.display.flip()
                    if base[0]+500<x<=base[0]+640:
                        n=random.randint(0,1000000)
                        pygame.draw.rect(screen, (0,255,0), pygame.Rect(base[0]+650,base[1]+660,680,120))
                        gTxt = font.render(str(n), True, (255,255,255))
                        screen.blit(gTxt, [base[0]+660,base[1]+670])
                        pygame.display.flip()
                if base[1]+660<y<=base[1]+780:
                    if base[0]+20<=x<=base[0]+140:
                        if n!=-1:
                            n=n*10+7
                            pygame.draw.rect(screen, (0,255,0), pygame.Rect(base[0]+650,base[1]+660,680,120))
                            gTxt = font.render(str(n), True, (255,255,255))
                            screen.blit(gTxt, [base[0]+660,base[1]+670])
                            pygame.display.flip()
                    if base[0]+140<x<=base[0]+260:
                        if n!=-1:
                            n=n*10+8
                            pygame.draw.rect(screen, (0,255,0), pygame.Rect(base[0]+650,base[1]+660,680,120))
                            gTxt = font.render(str(n), True, (255,255,255))
                            screen.blit(gTxt, [base[0]+660,base[1]+670])
                            pygame.display.flip()
                    if base[0]+260<x<=base[0]+380:
                        if n!=-1:
                            n=n*10+9
                            pygame.draw.rect(screen, (0,255,0), pygame.Rect(base[0]+650,base[1]+660,680,120))
                            gTxt = font.render(str(n), True, (255,255,255))
                            screen.blit(gTxt, [base[0]+660,base[1]+670])
                            pygame.display.flip()
                    if base[0]+380<x<=base[0]+500:
                        if n!=-1:
                            pygame.draw.rect(screen, (0,255,0), pygame.Rect(base[0]+650,base[1]+660,680,120))
                            gTxt = font.render(str(n), True, (255,255,255))
                            screen.blit(gTxt, [base[0]+660,base[1]+670])
                            pygame.display.flip()
                    if base[0]+500<x<=base[0]+640:
                        return n

def miru(save,screen,flag,key,debug,n):
    cards=[]
    if n>len(save[key]):
        n=len(save[key])
    for _ in range(n):
        cards.append(save[key][0])
        save[key]=save[key][1:]
    tmp=tmpmake(cards,0)
    current=0
    end=len(tmp[current])//6
    if len(tmp[current])%6==0:
        end-=1
    printcards(tmp[current],screen,0,cards,flag)
    if key%2==0:
        key2=18
    else:
        key2=19
    page2(save,screen,debug,tmp,current,end,0,cards,flag,key2,-1)
    return

#説明書を表示する。画像でいいのではないでしょうか。
def dmphelp(screen,save,debug):
    rect(screen,True)
    info(save,screen,debug)
    return

def kndnbigbun(save,flag):
    card=['rd_skc_001', '終焉の禁断 ドルマゲドンX', [], 999, None, 999999, ['r','d'], False, True, False, True, False, 'skc', ['T-Breaker'], False, False]
    #禁断コアが未実装
    tmp=[card,False,False,[card],[],-1,1,0]
    if flag:
        save[8].append(tmp)
    else:
        save[9].append(tmp)
    return save

def zeronbantan(save,flag):
    card=['d_zc_001', '零龍', ['マスター・ドラゴンZ'], 0, None, 0, ['d'], False, True, False, True, False, 'zc', ['World-Breaker'], False, False]
    tmp=[card,False,False,[card],[],-1,1,0]
    if flag:
        save[8].append(tmp)
    else:
        save[9].append(tmp)
    return save