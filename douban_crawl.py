import requests
from lxml import etree

url = 'https://movie.douban.com/top250'

def req(request_url):
    re = requests.get(request_url)
    return re.text

def handle(html):
    selector = etree.HTML(html)
    movies = selector.xpath('//ol[@class="grid_view"]/li')
    if len(movies) > 0:
        for movie in movies:
            titleArr = movie.xpath('.//div[@class="hd"]/a/span[@class="title"]')
            rateArr = movie.xpath('.//span[@class="rating_num"]')
            quoteArr = movie.xpath('.//span[@class="inq"]')
            titleString = ""
            rateString = ""
            quoteString = ""
            for title in titleArr:
                titleString = titleString + title.text
                pass
            for rate in rateArr:
                rateString = rate.text
                pass
            for quote in quoteArr:
                quoteString = quote.text
                pass
            f = open('douban.txt','a')
            f.write(titleString +"    " + rateString + "  " + quoteString + "\n")
            pass
        print("write movies in douban.txt")
    else:
        print('no movie')

for i in range(0,4):
    s = i * 25
    rurl = url + "?start=" + "%s" % (s)
    html = req(rurl)
    handle(html)