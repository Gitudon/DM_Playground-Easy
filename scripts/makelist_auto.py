#辞書
import carddict

#カード名と枚数を受け取って入力する
#入力をリダイレクト
def main():
    deck=[]
    f=open('GUI/etc/in/listinput.txt','r', encoding='utf-8')
    cardlist=f.readlines()
    i=0
    while True:
        if cardlist[i][:(len(cardlist[i])-1)]=="z":
            break
        key=cardlist[i][:(len(cardlist[i])-1)]
        print(key)
        i+=1
        if key in carddict.dic:
            value=carddict.dic[key]
            num=int(cardlist[i][:len(cardlist[i])-1])
            for _ in range(num):
                deck.append(value)
        else:
            print("カードが存在しません。")
        i+=1
    i+=1
    num=cardlist[i]
    with open('GUI/decks/deck'+str(num)+'.txt','w', encoding='utf-8') as o:
        print(*deck,file=o)
    print(len(deck))

if __name__=="__main__":
    main()