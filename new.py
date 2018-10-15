from urllib import request
from bs4 import BeautifulSoup
# 抓取地址
url = 'http://c.vivame.net.cn/v1/feedDetail/3486127201566798689.html?ver=0&p=7e28e516405a32fcd22d6ed77c7e896781176da74dd4ee4634a8a5336b67430656a93d956ea407cd408f7dbfdf1244980b1f3199f2f1d27de7fb37767189e5ff985a168b1f104cdde7aaa33edb403f111ca7a96b0bc5a9b1eb37e50c04e11fd443fdc316775b740bdfa55d2e4c7e609e2ff59da01ae883c65a63c95184af8b7ceb0bd88ec8628ee098d2e5b07cb0c858&accessId=24dd2ec1110e486fbe5fbb29d75b3cf3'
# 网页对象
htmlObject = request.urlopen(url)
# 解析对象
html = htmlObject.read()
# beautifulSoup格式化数据
soup = BeautifulSoup(html, 'html.parser')
# 筛出所有a标签
# div = soup.find_all(name='div',attrs={"class":"mod-tab-pane active"})
# titleNews = soup.find(name='ul',attrs={"class":"ulist focuslistnews"})
# a = titleNews.find_all('a')
# for val in a:
#     string = val.string
#     href = val.get('href')
#     print('标题：'+string)
#     print('地址：'+href)

# otherNews = soup.find(attrs={"class":"mod-tab-content"})
# print(otherNews);

# file = open("hello.html",'w')
# file.write(otherNews)
# file.close
img = soup.find_all('img')
# li = otherNews.find_all('li')
for val in img:
    # a = val.find('a')
    datasrc = val.get('data-src')
    if datasrc != None:
        val = val.get('src')
    href = a.get('href')
    print(src)

# for val in a:
#     string = val.string
#     href = val.get('href')
#     print('标题：'+string)
#     print('地址：'+href)
# ul = div.find_next('ul')

# for link in a:
#     # url = link.get('href')
#     string = link.string
#     print(string)
#     html = f.read()
#     soup = BeautifulSoup(html, 'html.parser')
#     arr = soup.find_all('a')
#     for link2 in arr:
#         print(link2.get('href'))
# print(arr)
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# f = request.urlopen(req)
# print('Status:', f.status, f.reason)
# for k, v in f.getheaders():
#     print('%s: %s' % (k, v))
# print('Data:', f.read().decode('utf-8'))