import requests, bs4, sys, webbrowser

arg = sys.argv

if len(arg) > 1:
    keyword = ' '.join(arg[1:])
    print('keyword is ' + keyword)
    url = "http://www.baidu.com/s?wd=%s" % keyword
    print(url)
    res = requests.get(url)
    res.raise_for_status()
    bs = bs4.BeautifulSoup(res.text, "lxml")
    elems = bs.select('.t a')
    print('elem count is %d' % len(elems))
    num = min(5, len(elems))
    for i in range(num):
        ele = elems[i].get('href')
        webbrowser.open(ele)
        
else:
    print('no keyword')



