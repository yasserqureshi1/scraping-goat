import requests
import json

def search(query):
    headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"}
    url = 'https://2fwotdvm2o-dsn.algolia.net/1/indexes/ProductTemplateSearch/query'
    params = {'x-algolia-agent': 'Algolia for vanilla JavaScript 3.25.1',
          'x-algolia-api-key': 'ac96de6fef0e02bb95d433d8d5c7038a',
          'x-algolia-application-id': '2FWOTDVM2O'}
    data = {"params": "query={}&hitsPerPage=10".format(query.replace(' ','%20'))}
    html = requests.post(url=url, headers=headers, params=params, json=data)
    output = json.loads(html.text)
    return output['hits'][0]

def new_search(query):
      headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'dnt': '1',
            'origin': 'https://www.goat.com',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
      }
      url = f'https://ac.cnstrc.com/search/{query.replace(" ","%20")}?c=ciojs-client-2.27.9&key=key_XT7bjdbvjgECO5d8&i=0d562b86-f8cf-4b44-8277-ca435324260e&s=2&num_results_per_page=25&_dt=1653046311601'
      html = requests.get(url=url, headers=headers)
      output = json.loads(html.text)
      return output['response']['results'][0]


print(search('dunk'))