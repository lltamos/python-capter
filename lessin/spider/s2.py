import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    server = 'http://www.biqukan.com/'
    target = 'http://www.biqukan.com/1_1094/'
    req = requests.get(url=target)
    html = req.text
    div_bf = BeautifulSoup(html, 'html5lib')
    div = div_bf.find_all('div', class_='listmain')
    print(type(div[0]))
    print(type(str(div[0])))

    # f = open('directory.txt', 'w')
    # f.write(str(div[0].text))
    # f.close()

    a_bf = BeautifulSoup(str(div[0]), 'html5lib')
    a = a_bf.find_all('a')
    for each in a:
        print(each.string, server + each.get('href'))
