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
    return r.text
    

def parse_page(infolist,data):
    titlepat= '"title":"(.*?)"'
    commentpat='"abstract":"(.*?)"'
    lastpat='"last":"(.*?)"'
    
    titleall=re.compile(titlepat,re.S).findall(data)
    commentall=re.compile(commentpat,re.S).findall(data)
    next_cid=re.compile(lastpat).findall(data)[0]
    
    infolist.append([titleall[:len(commentall)],commentall])
    
    return next_cid

def print_comment_list(infolist):
    j=0
    for page in infolist:
        print('第'+str(j+1)+'页\n')
        titleall=page[0]
        commentall=page[1]
        for i in range(0,len(commentall)):
            print('='*30)
            print('评论标题：'+eval('u'+"'"+titleall[i]+"'")+'\n')
            print('评论内容：'+eval('u'+"'"+commentall[i]+"'")+'\n')
        j+=1
    
    
def save_to_txt(infolist,path):
    fw=open(path,'w+',encoding='utf-8')
    j=0
    for page in infolist:
        fw.write('第'+str(j+1)+'页\n')
        titleall=page[0]
        commentall=page[1]
        for i in range(0,len(commentall)):
            fw.write('='*30+'\n')
            fw.write('评论标题：'+eval('u'+"'"+titleall[i]+"'")+'\n')
            fw.write('评论内容是：'+eval('u'+"'"+commentall[i]+"'")+'\n')
        j+=1
    fw.close()
              
def main():
    infolist=[]       #page_nnum x 2(titleall,commentall) x req_num
    vid= '4baf2nzoljqyobl';  next_cid='0'; page_num=2
    
    for i in range(page_num):
        url='https://video.coral.qq.com/filmreviewr/c/upcomment/'+vid+'?'
        params={'commentid': next_cid,'reqnum': '3'}
        html=get_html(url,params)
        next_cid=parse_page(infolist,html)
    
    print_comment_list(infolist)
    save_to_txt(infolist,'./tencent_comment/xajh_cp.txt')
        
main()
