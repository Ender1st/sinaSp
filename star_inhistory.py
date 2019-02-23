import json
import re


with open('json/historyhot.json', 'r',encoding='utf-8') as f:
    historyhot = json.load(f)
    for x in historyhot.keys():
        print(x)

with open(r'明星词典.txt', 'r',encoding="utf-8") as f:
    star = f.readlines()
    starcount = {}
    startiao = 0
    for xx in star:
        #print(xx.strip())
        r = xx.strip()
        for yy in historyhot.keys():
            te = re.findall(r,yy)
            if te :
                startiao += 1
                try:
                    starcount[xx.strip()] = starcount[xx.strip()] + 1
                except:
                    starcount[xx.strip()] = 1
    for scount in starcount.keys():
        xx = '{0}-出现次数{1}'.format(str(scount),starcount[scount])
        print(xx)
print("热搜总条数:",len(historyhot))
print("与多少个明星有关:",len(starcount.keys()))
print("条数:",startiao)
y = 0
for x in starcount.keys():
    y += starcount[x]
    #print(y)
