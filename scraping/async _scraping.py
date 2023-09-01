from parsel import Selector
import httpx
import asyncio


class AllCarsScraping:
    START_URL = 'https://www.mashina.kg/'
    PLUS_URL = 'https://www.mashina.kg'
    LINK_XPATH = '//div[@class="after-logo-7"]/ul/li/a/@href'
    CATEGORY_XPATH = '//ul[@class="login-submenu"]//li/a/@href'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
        'Accept': 'image/avif,image/webp,*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': ''
    }

    async def create_link(self, links):
        for link in links:
            yield link

    async def Get_url(self, client, url):
        response = await client.get(url)
        await self.parse_links(content=response.text)
        return response

    async def parse_links(self, content):
        tree = Selector(text=content)
        links = tree.xpath(self.LINK_XPATH).extract()
        print('Ссылки на категории:')
        for link in links:
            print(self.PLUS_URL+link)
        await self.parse_categories(content=content)

    async def parse_categories(self,content):
        tree = Selector(text=content)
        category_links = tree.xpath(self.CATEGORY_XPATH).extract()
        print('\nСсылки на тип категории:')
        for category_link in category_links:
            print(self.PLUS_URL+category_link)

    async def parse_data(self):
        async with httpx.AsyncClient(headers=self.HEADERS) as client:
            await self.get_url(client=client, url=self.START_URL)