import requests
from lxml import etree
import json
# http://mobile.cfda.gov.cn/datasearch/QueryRecord?tableId=27&searchF=ID&searchK=39396
url = 'http://mobile.cfda.gov.cn/datasearch/QueryList?pageIndex=1&pageSize=10&tableId=27&searchF=Quick Search&searchK=骨针'

def req(request_url):
    re = requests.get(request_url)
    return re.text

hasTitle = False
jsonString = req(url)
dic = json.loads(jsonString)
for item in dic:
    itemURL = "http://mobile.cfda.gov.cn/datasearch/QueryRecord?tableId=27&searchF=ID&searchK={}".format(item['ID'])
    detailJson = req(itemURL)
    detail = json.loads(detailJson)
    output = ''
    if hasTitle == False:
        hasTitle = True
        for category in detail:
            output = output + category['NAME'] + ', '
        output = output + '\n'

    for category in detail:
        content = category['CONTENT']
        if isinstance(content, str):
            content = content.strip()
            content = content.replace('\n', '')
            content = content.replace('\r', '')
        output = output + content + ', '

    output = output + '\n'
    with open('骨针.csv','a+') as f:
        try:
            f.write(output)
        except:
            print('no')
            f.write('None')
