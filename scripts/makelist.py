#辞書
import carddict

#カード名と枚数を受け取って入力する
def main():
    deck=[]
    while True:
        key=input("カード名を入力/終了なら'z'と入力> ")
        if key=="z":
            break
        if key in carddict.dic:
            value=carddict.dic[key]
            num=int(input("枚数を入力> "))
            for _ in range(num):
                deck.append(value)
        else:
            print("カードが存在しません。")
    while True:
        num=int(input("デッキのスロット番号を入力> "))
        if 0<=num<=29:
            with open('GUI/etc/out/listout.txt','w', encoding='utf-8') as o:
                print(*deck,file=o)
            with open('GUI/decks/deck'+str(num)+'.txt','w', encoding='utf-8') as o:
                print(*deck,file=o)
            break
        else:
            print("存在しないスロット番号です。")

if __name__=="__main__":
    main()