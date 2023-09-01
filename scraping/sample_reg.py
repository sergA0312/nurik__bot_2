import requests

url = "https://24.kg/thumbnails/bc4be/9a9b4/306312_w848_h445.jpg"

payload = {}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
  'Accept': 'image/avif,image/webp,*/*',
  'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
  'Accept-Encoding': 'gzip, deflate, br',
  'Referer': 'https://24.kg/'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
