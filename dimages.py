import json
import random
import shutil

import requests
import re

def validate_title(raw):

    new_title=re.sub("UHD.jpg","1920x1080.jpg", raw)
    return new_title

def downloads(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    json_data = requests.get(url=url, headers=headers).json()
    pic_url = r'https://cn.bing.com{0}'.format(
        json_data['images'][0]['url'].split("&")[0])
    start_date = json_data['images'][0]['startdate']
    open(f'./json/{start_date}.json',
         'wb').write(requests.get(url=url, headers=headers).content)
    pic = requests.get(pic_url, stream=True)
    if (pic.status_code == 200):     
        open(f'./images/{start_date}.png', 'wb').write(pic.content)
        shutil.copyfile(f'./images/{start_date}.png',
                        f'./images/latest.png')
        print(f'Create {start_date} Image Success!')
    else:
        print(f'Create {start_date} Image Failed!')
    



    
    pic_1080p = requests.get(validate_title(pic_url), stream=True)
    if (pic_1080p.status_code == 200):     
        open(f'./1080pimages/{start_date}.png', 'wb').write(pic_1080p.content)
        shutil.copyfile(f'./1080pimages/{start_date}.png',
                        f'./1080pimages/latest.png')
        print(f'Create {start_date} 1080P_Image Success!')
    else:
        print(f'Create {start_date} 1080P_Image Failed!')
        
    return