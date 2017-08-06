#!usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
import os


def url_open(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url, headers=headers)
    response=urllib.request.urlopen(req)
    html=response.read().decode('utf-8')
    return html

def find_product(url):
    html=url_open(url)
    string=str("\"cursor:pointer;\"")+str("  href")
    a=html.find(string)
    productname=[]
    while a!=-1:
        b=html.find('</a><img alt=',a,a+200)
        if b!=-1:
            productname.append(html[a+74:b])
        else:
            b=a+20
        a=html.find(string,b)
    return productname
     
    
def page_address(n=9):
    os.mkdir("product")
    os.chdir("product")
    with open('name.txt',"w",encoding="utf-8") as file:
        order=0
        for i in range(n):
            url_address="http://www.zhongmin.cn/health/health0g-1m-1o-1s-1c-1e-1od2ot1bpg"
            url=url_address+str(i+1)+str(".html")
            product=find_product(url)
            print(product)
            print(type(product))
        
            for each in product:
                #file.write("{}\n".format(each))
                #print ("序号：%s   值：%s" % (product.index(each) + 1, each))
                num=order+product.index(each) + 1
                file.write("#% s  %s\n" % (num, each))
            order=num
                

        
if __name__ == "__main__":
    page_address()




