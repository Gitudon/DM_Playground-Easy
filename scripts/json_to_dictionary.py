import json

jsonfile="resources/cards/cardlist.json"

#カードが追加されるたびに動かす
def main():
    file=open(jsonfile,'r',encoding="utf_8")
    loading=json.load(file)
    dic={}
    dict= {k: {'key': v['key'], 'name': v['name']} for k, v in loading.items()}
    for k,v in dict.items():
        if type(v['name'])==list:
            dic[v['name'][0]+"/"+v['name'][1]]=k
        else:
            dic[v['name']]=k
    with open('scripts/carddict.py','w', encoding='utf-8') as o:
        print(f'dic={dic}', file=o)
    with open('resources/textdata/refs/cardname.txt','w', encoding='utf-8') as o:
        for k in dic:
            print(k,file=o)

if __name__=="__main__":
    main()
