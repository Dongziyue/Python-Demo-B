import urllib.request
from urllib.request import Request, urlopen
import re

url = 'http://jandan.net/'
data = urllib.request.urlopen(url).read().decode('UTF-8')
list1 = re.findall(r'//img.+\.jpg!custom', data)
list2 = []
for a in list1:
    list2.append('http:' + a)
i = 0
for b in list2:
    i = i + 1
    request = Request(b, headers={'User-Agent': 'Mozilla/5.0'})
    with open(str(i) + '.jpg', 'wb') as f:
        f.write(urlopen(request).read())
