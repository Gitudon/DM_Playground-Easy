import json

jsonfile="GUI/game/cardlist.json"

def main():
    flag=int(input("1:cardlist 2:carddic > "))
    if flag==1:
        cardlist()
    else:
        carddic()

#カードが追加されるたびに動かす
def cardlist():
    file=open('GUI/game/cardlist.json','r',encoding="utf_8")
    loading=json.load(file)
    dic={}
    dict= {k: {'key': v['key'], 'name': v['name']} for k, v in loading.items()}
    for k,v in dict.items():
        if type(v['name'])==list:
            dic[v['name'][0]+"/"+v['name'][1]]=k
        else:
            dic[v['name']]=k
    with open('GUI/etc/carddict.py','w', encoding='utf-8') as o:
        print(f'dic={dic}', file=o)
    with open('GUI/etc/cardname.txt','w', encoding='utf-8') as o:
        for k in dic:
            print(k,file=o)

#cip、常在能力で分ける
#手動で良くね
def carddic():
    file=open('GUI/game/cardlist.json','r',encoding="utf_8")
    loading=json.load(file)
    dic={}
    dict= {k: {'key': v['key'], 'name': v['name']} for k, v in loading.items()}
    for k in dict:
        dic[k]="cards."+k
    with open('GUI/etc/out/out.txt','w', encoding='utf-8') as o:
        print(f'dic={dic}', file=o)

if __name__=="__main__":
    main()
