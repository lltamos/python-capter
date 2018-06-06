#  实战unsplash 爬取
import requests
from bs4 import BeautifulSoup


class Unsplash(object):
    def __init__(self):
        self.server = ''
        self.target = ''
        self.headers = {}


def get_photos():
    resq = requests.get(url='https://unsplash.com/new')
    es_bg = BeautifulSoup(resq.text, 'html5lib')
    imgs = es_bg.find_all('img', attrs={'data-test': 'standard-photo-grid-single-col-img'})
    print(len(imgs))
    for index, each in enumerate(imgs):
        print('图片{}&&地址{}'.format(index, each.get('src')))


get_photos()
