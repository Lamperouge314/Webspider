import urllib.request
import json
import time

url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index'

while True:
    word=input('input a word: ')
    if word=='quit':
        break
    
    data={}
    data['type'] = 'AUTO'
    data['i'] = word
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['action'] = ['FY_BY_CLICKBUTTON']
    data['typoResult']= 'true'

    data=urllib.parse.urlencode(data).encode('utf-8')
    req=urllib.request.Request(url,data)
    req.add_header('User-Agent',"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11")
    response=urllib.request.urlopen(req)

    html=response.read().decode('utf-8')
    target=json.loads(html)
    try:
        print(target['smartResult']['entries'])
    except:
        print(target['translateResult'][0][0]['tgt'])
    
    time.sleep(2)
