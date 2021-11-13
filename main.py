import time
import requests
import json
import pandas as pd

#url = "https://ikman.lk/data/serp?top_ads=2&spotlights=5&sort=date&order=desc&buy_now=0&urgent=0&categorySlug=cars&locationSlug=sri-lanka&category=392&page=2&filter_json=[]"

payload = {}
headers = {
	'authority': 'ikman.lk',
	'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
	'accept': 'application/json, text/plain, */*',
	'x-mobile-request': 'false',
	'accept-language': 'en',
	'sec-ch-ua-mobile': '?0',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
	'sec-ch-ua-platform': '"Windows"',
	'sec-fetch-site': 'same-origin',
	'sec-fetch-mode': 'cors',
	'sec-fetch-dest': 'empty',
	'referer': 'https://ikman.lk/en/ads/sri-lanka/cars?sort=date&order=desc&buy_now=0&urgent=0&page=2',
	'cookie': 'ab-test.pwa-only=reactapp; locale=en; _gcl_au=1.1.585064066.1636797459; _ga_R6R5PK08HD=GS1.1.1636797458.1.1.1636797458.60; _sp_ses.611c=*; _sp_id.611c=b0e22f6165eaab5a.1636797459.1.1636797459.1636797459.712452c6-dd2f-43a5-bd09-cd3e5b36419f; _ga=GA1.2.1159786591.1636797459; _gid=GA1.2.1956189973.1636797459; _dc_gtm_UA-33150711-4=1; _dc_gtm_UA-32280343-9=1; _fbp=fb.1.1636797459495.1045047720; FCCDCF=[null,null,["[[],[],[],[],null,null,true]",1636797459412],null,null,null,[]]; __gads=ID=06db6ac471ac3978-22b2ef48abce00cd:T=1636797459:S=ALNI_Ma_xRzouNYXJZ13ZvAAWygZzNBRFQ; FCNEC=[["AKsRol9v3zj3e5q3ZZ8jbmJFQXR3myM8WFZRDkwGZx4uTc1zytPEXTOpBpsnDAUH3m_GpbBC0AYtNd1fZS-Y1J7UOTSkeJWIb7Kj4nAW0V5LV4zQxPZXnY8GK36ggEb6eN_HE3-k-2MugOZi57gNTwQg1ukHKUSBjg=="],null,[]]; ab-test.pwa-only=reactapp'
}

cars = pd.DataFrame([])

for page in range(1,371): #Change Page Range
  url = f"https://ikman.lk/data/serp?top_ads=2&spotlights=5&sort=date&order=desc&buy_now=0&urgent=0&categorySlug=cars&locationSlug=sri-lanka&category=392&page={page}&filter_json=[]"
  r = requests.get(url, headers=headers)
  data = json.loads(r.text)
  cars = cars.append(pd.json_normalize(data['ads']))
  time.sleep(5)


  #print(type(data))
  #for ads in data['ads']:
	  #del ads['id']


  print(f'Getting page {page}', 'wait only select 5 page...')

  #new = json.dumps(data, )
  #print(type(new))

for ads in data['ads']:
  del ads['mrp']
  del ads['slug']
  del ads['imgUrl']
  del ads['discount']
  del ads['isDeliveryFree']
  del ads['isTopAd']
  del ads['isUrgentAd']
  del ads['isVerified']
  del ads['isLocalJob']
  del ads['adType']


 #json File
  f = open("IkmanCars.json", "w")
  json.dump(data, f, indent= 20)
  f.close()

 #CSV File
  cars.to_csv('ikman.csv')




