# https://pharmeasy.in/online-medicine-order/195999
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

df = pd.DataFrame(dict)
itr = 0

for page in range(1, 196000):
    url = 'https://pharmeasy.in/online-medicine-order/' + str(page)
    print(url)
    headers = {
        'User-Agent': 'test'
    }
    f = requests.get(url, headers=headers)
    soup = BeautifulSoup(f.content, 'lxml')
    p_title = soup.find('h1', {'class': 'MedicineOverviewSection_medicineName__3D2tG'})
    if not p_title:
        p_title = soup.find('h1', {'class': 'OverviewSection_productNameOTC__22wbT'})

    p_manufacturer = soup.find('div', {'class': 'MedicineOverviewSection_brandName__YOB67'})

    if not p_manufacturer:
        soup.find('div', {'class': 'OverviewSection_productBrandOTC__2iDOu'})

    p_brand = soup.find('div', {'class': 'ProductDescription_tableValue__GBKiQ'})
    p_price = soup.find('div', {'class': 'PriceInfo_ourPrice__P1VR1'})

    if not p_price:
        p_price = soup.find('div', {'class': 'ProductPriceContainer_mrp__pX-2Q'})

    p_composition = soup.find('div', {'class': 'MedicineMolecules_text__22hJW'})
    p_category = soup.find('td', {'class': 'MedicineTherapy_text__1YWLq'})
    p_pack_size = soup.find('div', {'class': 'MedicineOverviewSection_measurementUnit__RUDyf'})
    if p_pack_size:
        p_pack_size = p_pack_size.get_text()

    if p_brand:
        p_brand = p_brand.get_text()

    if p_title:
        p_title = p_title.get_text()

    if p_price:
        p_price = p_price.get_text()

    if p_composition:
        p_composition = p_composition.get_text()

    if p_category:
        p_category = p_category.get_text()

    if p_manufacturer:
        p_manufacturer = p_manufacturer.get_text()

    print(p_title, '-', p_brand, '-', p_manufacturer,
          '-', p_composition, '-', p_category, '-', '-', p_pack_size,
          '-', p_price)

    df2 = {'Title': p_title,
           'Brand': p_brand,
           'Manufacturer': p_manufacturer,
           'Composition': p_composition,
           'Category': p_category,
           'Synonyms': '',
           'Pack size': p_pack_size,
           'Variant': '',
           'MRP': p_price,
           'Product listing url': url,
           }
    if p_title is None and p_brand is None and p_manufacturer is None and p_composition is None and p_category is None and p_pack_size is None and p_price is None:
        print('all none')
    else:
        df = df.append(df2, ignore_index=True)

df.to_excel("pharmeasy_1_final.xlsx")
