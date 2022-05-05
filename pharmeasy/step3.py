# https://pharmeasy.in/online-medicine-order/195999
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup

dict = {'Title': [],
        'Brand': [],
        'Manufacturer': [],
        'Composition': [],
        'Category': [],
        'Synonyms': [],
        'Pack size': [],
        'Variant': [],
        'MRP': [],
        'Product listing url': [],
        }

dfx = pd.read_excel('pharmeasy_prod_url.xlsx')

df = pd.DataFrame(dict)

for index, row in dfx.iterrows():
    p_category = row['Category']
    p_url = row['Product listing url']

    headers = {
        'User-Agent': 'test'
    }
    f = requests.get(p_url, headers=headers)
    soup = BeautifulSoup(f.content, 'lxml')

    p = soup.find('script', {'id': '__NEXT_DATA__'})

    data = json.loads(p.get_text())
    prod = data['props']['pageProps']['productDetails']
    try:
        p_brand = prod['productSpecifications'][0]['tableData'][0]['value']
    except:
        p_brand = ""

    print(prod['name'], prod['manufacturer'], ",".join(prod['compositions']), prod['salePrice'], p_brand)

    df2 = {'Title': prod['name'],
           'Brand': p_brand,
           'Manufacturer': prod['manufacturer'],
           'Composition': ",".join(prod['compositions']),
           'Category': p_category,
           'Synonyms': '',
           'Pack size': '',
           'Variant': '',
           'MRP': prod['salePrice'],
           'Product listing url': p_url,
           }

    df = df.append(df2, ignore_index=True)

df.to_excel("pharmeasy_prod_1.xlsx")
