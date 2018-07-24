import requests
from scrapy import Selector
from requests.exceptions import ConnectionError
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",}

for i in range(1,100):
    try:
        html = requests.get('http://www.bianlun.com/forum-803-{}.html'.format(i)).text
    except ConnectionError as e:
        print(e)    
    titles = Selector(text=html).xpath('//th[@class="new"]/a[@class="xst"]/text()').extract()
    with open("result.txt",'a') as f:
        for line in titles:
            f.write(line+'\n')
