import locale
locale.setlocale(locale.LC_COLLATE, 'zh_CN.UTF8')
cmp = locale.strcoll


with open(r'明星词典.txt', 'r',encoding="utf-8") as f:
    star = f.readlines()

print(star)
star.sort(lambda x,y:cmp(x[0],y[0]))
print(star)