import requests

r = requests.get('https://www.baidu.com')
f = open('my_html','w')
f.write(r.text)