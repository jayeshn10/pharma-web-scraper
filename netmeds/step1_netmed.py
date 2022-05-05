from time import sleep

import pandas as pd
import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'test'
}
url = 'https://www.netmeds.com/prescriptions'
f = requests.get(url, headers=headers)
soup = BeautifulSoup(f.content, 'lxml')

prod_cat_cols = soup.find_all('ul', {'class': 'alpha-drug-list'})

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
itr = 0
for prod_cat in prod_cat_cols:
    cat_li_list = prod_cat.find_all('li')
    for cat_li in cat_li_list:

        cat_link = cat_li.find('a')['href']
        # print(cat_link)
        c = requests.get(cat_link, headers=headers)
        cat_soup = BeautifulSoup(c.content, 'lxml')
        prod_cols = cat_soup.find_all('ul', {'class': 'alpha-drug-list'})
        for prod_div in prod_cols:
            prod_li = prod_div.find('li')
            subc_cat = prod_li.find('a', {'class': 'drug-list-title'})

            prod_li_list = prod_li.find_all('li', {'class': 'product-item'})
            for prod in prod_li_list:
                prod_link = prod.find('a')['href']
                p = requests.get(prod_link, headers=headers)
                prod_soup = BeautifulSoup(p.content, 'lxml')
                p_title = prod_soup.find('div', {'class': 'product-detail'}).find('h1').get_text()
                p_Manufacturer = prod_soup.find(lambda tag: tag.name == "span" and "* Mkt:" in tag.text).find(
                    'a').get_text()
                p_price = prod_soup.find('span', {'class': 'final-price'})
                for tag in p_price.find_all(['span']):
                    tag.replaceWith('')
                p_price = p_price.get_text()
                p_pack_size = prod_soup.find('span', {'calss': 'drug-varient'})

                if p_pack_size:
                    p_pack_size = p_pack_size.get_text()
                else:
                    p_pack_size = ''

                print(p_title, '-', p_Manufacturer, '-', cat_li.get_text(),
                      '-', subc_cat.get_text(), '-', p_pack_size,
                      '-', p_price)

                df2 = {'Title': p_title,
                       'Brand': '',
                       'Manufacturer': p_Manufacturer,
                       'Composition': '',
                       'Category': "" + cat_li.get_text() + "," + subc_cat.get_text() + "",
                       'Synonyms': '',
                       'Pack size': p_pack_size,
                       'Variant': '',
                       'MRP': p_price,
                       'Product listing url': prod_link,
                       }
                df = df.append(df2, ignore_index=True)


df.to_excel("netmeds_1_final.xlsx")


