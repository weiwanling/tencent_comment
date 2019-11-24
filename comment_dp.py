import requests
import re
import random

def get_html(url,params):
    uapools=[
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
             'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14'         
            ]
    
    thisua=random.choice(uapools)
    headers={"User-Agent":thisua}
    r=requests.get(url,headers=headers,params=params)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    r.encoding='utf-8'       # 不加此句出现乱码
    return r.text
    

def parse_page(infolist,data):
    commentpat='"content":"(.*?)"'
    lastpat='"last":"(.*?)"'
    
    commentall=re.compile(commentpat,re.S).findall(data)
    next_cid=re.compile(lastpat).findall(data)[0]
    
    infolist.append(commentall)
    
    return next_cid

def print_comment_list(infolist):
    j=0
    for page in infolist:
        print('第'+str(j+1)+'页\n')
        commentall=page
        for i in range(0,len(commentall)):
            print('评论内容：'+commentall[i]+'\n')
        j+=1
    
    
def save_to_txt(infolist,path):
    fw=open(path,'w+',encoding='utf-8')
    j=0
    for page in infolist:
        fw.write('第'+str(j+1)+'页\n')
        commentall=page
        for i in range(0,len(commentall)):
            fw.write('评论内容：'+commentall[i]+'\n')
        j+=1
    fw.close()
    
def main():
    infolist=[]
    vid='1001103527';  cid = "0"; page_num=2
    url = 'https://video.coral.qq.com/varticle/'+vid+'/comment/v2'
    
    for i in range(page_num):
        params={'orinum':'10','cursor':cid}
        html=get_html(url,params)
        cid=parse_page(infolist,html)
    
    print_comment_list(infolist)
    save_to_txt(infolist,'./tencent_comment/xajh_dp.txt')
    
main()                    
