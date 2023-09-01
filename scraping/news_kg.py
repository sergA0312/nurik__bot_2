import self as self
from parsel import Selector
import requests


class News_kg:
    START_URL = 'https://24.kg/'
    LINK_XPATH = '//div[@class="col-xs-12"]/div/div/a/@href'
    def pars_data = (self):
    text = requests.get(self.START_URL).text
    tree = Selector(text=text)
    links = tree.xpath(self.LINK_XPATH).extract()
    data = []
    for link in links:
        data.append(f'https://24.kg' + link)
  return data[:5]