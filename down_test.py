# 下载一个在线的视频文件存在本地


import urllib.request

url = 'http://you.163.com/item/detail?id=1505027&_stat_area=mod_limit_item_3&_stat_referer=index'

with urllib.request.urlopen(url) as f:
    for line in f.readlines():
        print(line.decode('UTF-8'))

# urllib.request.urlretrieve(url, 'test.mp4')
