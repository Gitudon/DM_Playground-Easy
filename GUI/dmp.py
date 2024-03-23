import pygame
import sys
import time
import json
import pickle
import copy
import codecs
from game.func import Shuffle,showcards,draw,recover,deck,menu,showcard,sshield,shieldplus,grdeck,dimension,deckinfo,debugmenu,dmphelp,decklist,emenu,swap,grdeckinfo,choose,showlog,showmanazone,showbattlezone,put,expand
from game import carddic
from game import deckdic
from game import deckbuild

#定数の設定
width=100
height=144
field=(1550,1000)
fieldcolor=(0,200,0)
upbase=(230, 155)
downbase=(920, 696)
#動的に指定するための辞書
card=carddic.card
Deck=deckdic.Deck
#実行ログのパス
logpath='GUI/etc/log.txt'

#タイトル画面
def main():
    #登録されたデッキリストから選びたい
    #自分で空きスロットに登録できるようにもしたい
    #テキストファイルをもととしたデッキのビルド
    for i in range(30):
        path='GUI/decks/deck'+str(i)+'.txt'
        name='deck'+str(i)
        Deck[name]=deckbuild.build(path)
    initalize()

def initalize():
    log=[]
    #初期設定
    pygame.init() 
    screen = pygame.display.set_mode(field)
    pygame.display.set_caption("Duel Masters")
    #デッキのリスト01、シールドのリスト23、手札のリスト45、マナのリスト67、バトルゾーンのリスト89、墓地のリスト1011、超次元ゾーンのリスト1213、GRゾーンのリスト1415
    save=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    screen.fill(fieldcolor)
    pygame.display.update()
    #アドバンス/オリジナルの選択
    advance=choose(screen,"フォーマットはアドバンスにしますか？")
    screen.fill(fieldcolor)
    pygame.display.update()
    #実行モード切り替え
    mode=choose(screen,"簡易モードで実行しますか？")
    screen.fill(fieldcolor)
    pygame.display.update()
    #デッキ選択
    choosing=True
    num=1
    decklist(screen,num)
    pygame.display.update()
    while choosing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 210<=x<=720 and 110<=y<=730:
                    deckname1="deck"+str(num-1)
                    choosing=False
                elif 830<=x<=1340 and 110<=y<=730:
                    deckname1="deck"+str(num)
                    choosing=False
    choosing=True
    num=1
    decklist(screen,num)
    while choosing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 110<=x<=770 and 110<=y<=730:
                    deckname2="deck"+str(num-1)
                    choosing=False
                elif 780<=x<=1440 and 110<=y<=730:
                    deckname2="deck"+str(num)
                    choosing=False
    tmp1=copy.deepcopy(Deck.get(deckname1))
    tmp2=copy.deepcopy(Deck.get(deckname2))
    #アドバンスかオリジナルだったりもするのでそれも判定する。
    if advance:
        for cards in tmp1:
            if any(substring in cards[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
                save[12].append(cards)
            elif "_grc_" in cards[0]:
                save[14].append(cards)
            elif any(substring in cards[0] for substring in ["_k_", "_kf_","_z_","_zs_"]):
                expand(save,cards,True)
            else:
                save[0].append(cards)
        for cards in tmp2:
            if any(substring in cards[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
                save[13].append(cards)
            elif "_grc_" in cards[0]:
                save[15].append(cards)
            elif any(substring in cards[0] for substring in ["_k_", "_kf_", "_z_","_zs_"]):
                expand(save,cards,False)
            else:
                save[1].append(cards)
    save[0]=Shuffle(save[0])
    save[1]=Shuffle(save[1])
    if advance:
        save[14]=Shuffle(save[14])
        save[15]=Shuffle(save[15])
    print(save,file=codecs.open('GUI/etc/output.txt','w','utf-8'))
    #シールド展開
    screen.fill(fieldcolor)
    pygame.display.update()
    deck(screen,save[0],save[1])
    pygame.display.update()
    time.sleep(1)
    dimension(screen,save[12],save[13])
    if len(save[12])>0 or len(save[13])>0:
        time.sleep(1)
    grdeck(screen,save[14],save[15])
    if len(save[14])>0 or len(save[15])>0:
        time.sleep(1)
    #ここにアドバンスの処理
    if advance:
        if "d_z_001" in save[8]:
            save=draw(1,save,True)
        if "d_z_001" in save[9]:
            save=draw(1,save,False)
    
    #シールド展開
    sshield(screen)
    save=shieldplus(5,save,True)
    save=shieldplus(5,save,False)
    #最初のドロー
    save=draw(5,save,True)
    save=draw(5,save,False)
    if mode==True:
        Easy(save,screen,log)
    else:
        Duel(save,screen,log)

#簡易版デュエル実行
def Easy(save,screen,log):
    #temp=[save,screen]
    emenu(screen)
    debug=3
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #ボタン操作
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            #クリック操作
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 1260<=x<=1540:
                    if 10<=y<=60:
                        showcards(save,screen,True,4,debug)
                    elif 70<=y<=120:
                        save[4]=sorted(save[4])
                    elif 130<=y<=180:
                        save[4]=Shuffle(save[4])
                    elif 190<=y<=240:
                        save=swap(save)
                        recover(save,screen,debug)
                    elif 250<=y<=300:
                        a="b_s_002"
                        save=card[a](save,True)
                    elif 310<=y<=360:
                        showcards(save,screen,True,0,debug)
                    elif 370<=y<=420:
                        save[0]=Shuffle(save[0])
                    elif 430<=y<=480:
                        showcards(save,screen,True,2,debug)
                    elif 730<=y<=780:
                        dmphelp(screen)
                    elif 790<=y<=840:
                        initalize()
                    elif 850<=y<=900:
                        showlog(screen,log)
                    elif 910<=y<=960:
                        pygame.quit()
                        sys.exit()
                elif downbase[1]<=y<=downbase[1]+height:
                    #自分側デッキ
                    if downbase[0]<=x<=downbase[0]+width:
                        deckinfo(save,True,screen,debug)
                    #自分側墓地
                    elif downbase[0]+10+width<=x<=downbase[0]+2*width+10:
                        showcards(save,screen,True,10,debug)
                    #自分側超次元
                    elif downbase[0]+20+2*width<=x<=downbase[0]+3*width+20:
                        showcards(save,screen,True,12,debug)
                elif downbase[1]+height+10<=y<=downbase[1]+2*height+10:
                    #自分側GRデッキ
                    if downbase[0]+20+2*width<=x<=downbase[0]+3*width+20:
                        grdeckinfo(save,True,screen,debug)
                    #自分側マナゾーン
                    elif upbase[0]-20-2*width<=x<=downbase[0]+10+2*width:
                        showmanazone(save,screen,True,6,debug)
                elif upbase[0]-2*(width+10)<=x<=downbase[0]+20+3*width:
                    if downbase[1]-10-height<=y<=downbase[1]-10:
                        #自分側バトルゾーン
                        showbattlezone(save,screen,True,8,debug)
                    elif upbase[1]+10+height<=y<=upbase[1]+10+2*height:
                        #相手側バトルゾーン
                        showbattlezone(save,screen,True,9,debug)
                elif upbase[1]<=y<=upbase[1]+height:
                    #相手側デッキ
                    if upbase[0]<=x<=upbase[0]+width:
                        deckinfo(save,False,screen,debug)
                    #相手側墓地
                    elif upbase[0]-10-width<=x<=upbase[0]-10:
                        showcards(save,screen,True,11,debug)
                    #相手側超次元
                    elif upbase[0]-20-2*width<=x<=upbase[0]-20-width:
                        showcards(save,screen,True,13,debug)
                elif upbase[1]-height-10<=y<=upbase[1]-10:
                    #相手側マナゾーン
                    if upbase[0]-10-width<=x<=downbase[0]+3*width+20:
                        showmanazone(save,screen,True,7,debug)
                    #相手側GRゾーン
                    elif upbase[0]-20-2*width<=x<=upbase[0]-20-width:
                        grdeckinfo(save,False,screen,debug)
            pygame.display.update()

#デュエル実行
def Duel(save,screen,log):
    sys.exit()

if __name__=="__main__":
    main()