import json

with open('json/historyhot.json', 'r') as f:
    historyhot = json.load(f)
with open(r'json/record.txt', 'r') as f:
    x = f.readlines()
for filename in x:
    with open('json/' + filename.strip() + '.json', 'r') as f:
        yy = json.load(f)
        print(str(yy['hot']['time']) + '\t此刻热词：\t' + yy['hot']['hotcode'])
        for i in range(50):
            i = str(i)
            if yy[i]["关键字"] not in historyhot.keys():
                historyhot[yy[i]["关键字"]] = {}
                historyhot[yy[i]["关键字"]]['firsttime'] = yy['hot']['time']
                historyhot[yy[i]["关键字"]]['firstrank'] = yy[i]["排名"]
                historyhot[yy[i]["关键字"]]['firstpopu'] = yy[i]["人气值"]
                historyhot[yy[i]["关键字"]]['lasttime'] = yy['hot']['time']
                historyhot[yy[i]["关键字"]]['lastrank'] = yy[i]["排名"]
                historyhot[yy[i]["关键字"]]['lastpopu'] = yy[i]["人气值"]
            else:
                historyhot[yy[i]["关键字"]]['lasttime'] = yy['hot']['time']
                historyhot[yy[i]["关键字"]]['lastrank'] = yy[i]["排名"]
                historyhot[yy[i]["关键字"]]['lastpopu'] = yy[i]["人气值"]

print(x[0].strip())
print(yy['hot']['time'])

for key in historyhot.keys():
    if (historyhot[key]['firstrank'] <= 10) and (str(historyhot[key]['firsttime']) != str(x[0].strip())):
        print('最初排名异常')
        print(key)
        print(historyhot[key])
    if (historyhot[key]['lastrank'] <= 10) and (historyhot[key]['lasttime'] != yy['hot']['time']) and (
            str(historyhot[key]['lasttime']) != str(x[0].strip())):
        print('最后排名异常')
        print(key)
        print(historyhot[key])

# print (historyhot)
with open('json/historyhot.json', 'w') as f:
    # json2.dump(name_num,f,ensure_ascii=False)
    data = json.dumps(historyhot)
    f.write(data)