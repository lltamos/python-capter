import requests
from bs4 import BeautifulSoup as bf


class SpiderUtil(object):



    def fetch(url):
        if url is None:
            return None
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                return resp.text
            return None
        except:
            return None

    def parse_item(resp):
        deic_list = []
        bf_r = bf(resp, 'html5lib')
        rlist = bf_r.find_all('li', class_='ui-slide-item', attrs={'data-title': True});
        for r in rlist:
            deic_item = {}
            deic_item['data-title'] = r['data-title']
            deic_item['data-region'] = r['data-region']
            deic_item['data-release'] = r['data-release']
            deic_item['data-director'] = r['data-director']
            img_temp = r.find_all('img')
            data_img = img_temp[0]['src']
            deic_item['data-img'] = data_img
            deic_list.append(deic_item)
        return deic_list


if __name__ == '__main__':
    url_content = SpiderUtil.fetch('https://movie.douban.com/')
    res = SpiderUtil.parse_item(url_content)
    print(res)