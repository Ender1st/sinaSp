
import urllib.request
import re

#import ast
import json
from bs4 import BeautifulSoup
import time

def get_data1(html):
    x = re.findall(r"STK\.pageletM\.view\(.+\)?", html)[4]
    x = x[18:-10]
    x = json.loads(x)
    #x = ast.literal_eval(x)
    x = x['html']
    #print(x)
    #star_name = re.findall(r'<a.+>.+<//a>?', x)
    soup = BeautifulSoup(x,'lxml')
    #star_names = soup.select('.star_name')
    star_names = soup.select('a')
    star_nums = soup.select('.star_num')
    hoting = star_names.pop(0).text
    for names in star_names:
     if names.text == '':
            star_names.remove(names)
    rnums, rnames = [], []
    for num in star_nums: rnums.append(num.text)
    for name in star_names: rnames.append(name.text)

    return hoting,rnums,rnames

def get_data2(html):
    soup = BeautifulSoup(html, 'lxml')
    names = soup.select('.td-02 > a')
    #nums = soup.select('.td-03')[1:]
    nums = soup.select('.td-02 > span')
    hoting = names.pop(0).text
    star_nums, star_names = [], []
    for num in nums: star_nums.append(num.text)
    for name in names: star_names.append(name.text)
    return hoting, star_nums, star_names

def get_html():
    url = r'http://s.weibo.com/top/summary?cate=realtimehot'
    req = urllib.request.Request(url)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5702.400 QQBrowser/10.2.1893.400'}
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html

def save_hot(hoting, star_nums, star_names):
    #print(len(star_names))
    name_num = {}
    name_num['hot'] = {"hotcode":hoting, 'time':time.time()}
    for test in range(50):
      name_num[test] = {
          '排名':test+1,
          '关键字':star_names[test],
         '人气值':star_nums[test],
      }
    #   print("排名："+str(name_num[test]['排名'])+"** \t关键字："+name_num[test]['关键字']+"** \t人气值："+name_num[test]['人气值'] + "\n")

    with open('json/'+str(name_num['hot']['time'])+'.json','w') as f:
       #json2.dump(name_num,f,ensure_ascii=False)
        data = json.dumps(name_num)
        f.write(data)
        print('写入成功'+str(name_num['hot']['time']))

    with open(r'json/record.txt','a') as f:
        f.write(str(name_num['hot']['time'])+'\n')

    with open('json/'+str(name_num['hot']['time'])+'.json','r') as f:
        yy =  json.load(f)
        print(str(yy['hot']['time'])+'\t此刻热词：\t'+yy['hot']['hotcode'])
        for i in range(50):
            i = str(i)
            print("排名：" + str(yy[i]["排名"]) + "---\t关键字：" + yy[i]["关键字"] + "---\t人气值：" + yy[i]["人气值"] + "\n")


if __name__ == "__main__":

    flag = True
    while flag:
        html = get_html()
        try:
            hoting, star_nums, star_names = get_data1(html)
            save_hot(hoting, star_nums, star_names)
            time.sleep(60)
        except:
            try:
                hoting, star_nums, star_names = get_data2(html)
                save_hot(hoting, star_nums, star_names)
                time.sleep(60)
            except Exception as e:
                print(e)
                flag = False
    #get_hot()
