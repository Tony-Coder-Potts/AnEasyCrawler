import requests
from bs4 import BeautifulSoup


def crawler(t):
    # t为所需的数目
    result = []
    page = requests.get('https://www.solidot.org/')
    if page.status_code != 200:
        raise Exception('访问失败')
    page.encoding = 'utf-8'
    page = page.text
    soup = BeautifulSoup(page, 'html.parser')
    for x in soup.find_all(class_='block_m'):
        y = x.find('h2')
        z = y.find_all('a')
        if len(z) == 1:
            result.append(z[0].string)
        else:
            result.append(z[0].string + ':' + z[1].string)
    return result[0:t]

print(crawler(5))