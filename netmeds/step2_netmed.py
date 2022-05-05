import pandas as pd
import requests
from bs4 import BeautifulSoup

mylst = [['covid-essentials', 4], ['diabetes-support', 19], ['eyewear', 10],
         ['ayush', 573], ['fitness', 145],
         ['mom-baby', 107], ['devices', 99], ['surgical', 41],
         ['sexual-wellness', 19], ['treatments', 21]
         ]

dict = {'Title': [],
        'Brand': [],
        'Manufacturer':[],
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

for page in mylst:
    for p in range(1, page[1]+1):
        url = 'https://www.netmeds.com/non-prescriptions/' + page[0] + '/page/' + str(p)
        print(url)
        headers = {
            'User-Agent': 'test'
        }
        f = requests.get(url, headers=headers)
        soup = BeautifulSoup(f.content, 'lxml')
        prod_cnt = soup.find('div',{'id':'mstar_box'})
        product_list =prod_cnt.find_all('div',{'class':'cat-item'})
        for prod in product_list:
            prod_link = prod.find('a')['href']
            print(prod_link)
            p = requests.get(prod_link, headers=headers)
            prod_soup = BeautifulSoup(p.content, 'lxml')
            p_title = prod_soup.find('div', {'class': 'product-detail'})

            if p_title:
                p_title = p_title.find('h1')
                p_title = p_title.get_text()
            p_Manufacturer = prod_soup.find(lambda tag: tag.name == "span" and "* Mkt:" in tag.text)

            if p_Manufacturer:
                p_Manufacturer = p_Manufacturer.find('a')
            if p_Manufacturer:
                p_Manufacturer = p_Manufacturer.get_text()


            p_price = prod_soup.find('span', {'class': 'final-price'})
            if p_price:
                for tag in p_price.find_all(['span']):
                    tag.replaceWith('')
                p_price = p_price.get_text()

            p_pack_size = prod_soup.find('span', {'calss': 'drug-varient'})
            p_cats = prod_soup.find_all('span', {'class': 'gen_drug'})
            cat_lst = []
            for ct in p_cats:
                cat_lst.append(ct.get_text())

            cat = ",".join(cat_lst)

            if p_pack_size:
                p_pack_size = p_pack_size.get_text()
            else:
                p_pack_size = ''

            print(p_title, '-', p_Manufacturer, '-', cat, '-', p_pack_size,
                  '-', p_price)

            df2 = {'Title': p_title,
                   'Brand': '',
                   'Manufacturer': p_Manufacturer,
                   'Composition': '',
                   'Category': "" + cat,
                   'Synonyms': '',
                   'Pack size': p_pack_size,
                   'Variant': '',
                   'MRP': p_price,
                   'Product listing url': prod_link,
                   }
            df = df.append(df2, ignore_index=True)

df.to_excel("netmeds_2_final.xlsx")