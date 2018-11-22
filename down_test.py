# 下载一个在线的视频文件存在本地


import urllib.request

url = 'https://static.yximgs.com/s1/videos/www_main-059ce9beee.mp4'

urllib.request.urlretrieve(url, 'test.mp4')
