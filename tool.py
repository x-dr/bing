import requests
import re


def validate_title(raw):

    new_title=re.sub("UHD.jpg","1920x1080.jpg", raw)
    return new_title

def get_date():


    url='https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=10&nc=1612409408851&pid=hp&FORM=BEHPTB&uhd=1&uhdwidth=3840&uhdheight=2160'

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }
    json_data = requests.get(url=url, headers=headers).json()

    images_url = "https://cn.bing.com"+json_data['images'][0]['url']
    copyright=json_data['images'][0]['copyright']
    title=json_data['images'][0]['title']
    startdate=json_data['images'][0]['startdate']

    # print(startdate)
    # print(images_url.split("&")[0]) 
    # print(copyright)
    # print(title)


    # date=

    # print(date)

    with open('1080purl.txt','r+',encoding='utf-8') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(validate_title(images_url.split("&")[0])+'\n'+content)
        print(f'Create 1080purl.txt Failed!')


    with open('url.txt','r+',encoding='utf-8') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(images_url.split("&")[0]+'\n'+content)
        print(f'Create url.txt Failed!')
        
    with open('startdate.txt','r+',encoding='utf-8') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(startdate+'\n'+content)
        print(f'Create startdate.txt Failed!')
    with open('copyright.txt','r+',encoding='utf-8') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(copyright+'\n'+content)
        print(f'Create copyright.txt Failed!')
        
    topimg='![{}]({}&w=1000) Today:[{}]({})'.format(title,images_url.split("&")[0],copyright,images_url.split("&")[0])
    img_info='{} | [{}]({})'.format(startdate,copyright,images_url.split("&")[0])
    return topimg,img_info

def get_list():

    url=[]
    copyright=[]
    startdate=[]
    with open('url.txt', 'r') as fu:
        for line in fu:
            if(line!='\n'):
                url.append(line[:-1])


    with open('copyright.txt', 'r') as fc:
        for line in fc:
            if(line!='\n'):
                copyright.append(line[:-1])
            # print(line)

    with open('startdate.txt', 'r') as fd:
        for line in fd:
            if(line!='\n'):
                startdate.append(line[:-1])
            # print(line)


    list_img = ['!['+a+']'+ '('+b+'&pid=hp&w=384&h=216&rs=1&c=4'+')'+'`'+c+'`'+'['+a+']'+'('+b+')' for a, b,c in zip(copyright,url,startdate)]


    # # print(str(a))
    # print(list_a_b)
    return list_img
    # print(url)