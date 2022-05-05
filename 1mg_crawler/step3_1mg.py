import pandas as pd
import requests
from bs4 import BeautifulSoup

dfx = pd.read_csv('med_cat_id.csv')
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
df = pd.DataFrame(dict)

for index, row in dfx.iterrows():
    p_num = 1
    while True:
        cat_id =str(row['category-id'])
        #cat_id = '208'
        url = str(f'https://www.1mg.com/pharmacy_api_gateway/v4/drug_skus/by_therapeutic_class_id?therapeutic_class_id={cat_id}&page={str(p_num)}&per_page=50')

        r = requests.get(url)
        data = r.json()
        if data['data']['skus']:
            for prod in data['data']['skus']:
                prod_url = 'https://www.1mg.com' + prod['slug']
                print(prod['name'], prod['manufacturer_name'], prod['price'], prod['pack_size_label'],
                      prod['short_composition'], prod_url)

                df2 = {'Title': prod['name'],
                       'Brand': '',
                       'Manufacturer': prod['manufacturer_name'],
                       'Composition': prod['short_composition'],
                       'Category': "" + row['category'] + "," + row['sub-category'] + "",
                       'Synonyms': '',
                       'Pack size': prod['pack_size_label'],
                       'Variant': '',
                       'MRP': prod['price'],
                       'Product listing url': prod_url,
                       }
                df = df.append(df2, ignore_index=True)
            p_num = p_num + 1
        else:
            print('no')
            break


df.to_excel("1mg_med_final.xlsx")
"""
p_num = 1
#cat_id =str(row['category-id'])
cat_id = '208'
url = str(f'https://www.1mg.com/pharmacy_api_gateway/v4/drug_skus/by_therapeutic_class_id?therapeutic_class_id={cat_id}&page={str(p_num)}&per_page=50')

r = requests.get(url)
data = r.json()
if data['data']['skus']:
    for prod in data['data']['skus']:
        print(prod['name'],prod['manufacturer_name'],prod['price'],prod['pack_size_label'],prod['short_composition'],'https://www.1mg.com'+prod['slug'])
    p_num = p_num+1
else:
    print('no')
    #break"""