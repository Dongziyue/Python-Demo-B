# 下载一个在线的视频文件存在本地


import urllib.request

url = 'http://jandan.net/ooxx'

with urllib.request.urlopen(url) as f:
    for line in f.readlines():
        print(line.decode('UTF-8'))

# urllib.request.urlretrieve(url, 'test.mp4')
