# coding:utf-8
import json

import requests

from download import download

query = '永野芽郁'
''' download all images of Mei Nagano from douban.com  '''


''' for loop to request all urls '''
for i in range(0, 22471, 20):
    url = 'https://www.douban.com/j/search_photo?q=' + \
        query+'&limit=20&start='+str(i)
    html = requests.get(url).text
    response = json.loads(html, encoding='utf-8')
    for image in response['images']:
        print('img src is:', image['src'])
        download(image['src'], image['id'], 'scrapted_imgs')
