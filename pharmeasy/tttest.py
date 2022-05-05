import json

import requests
from bs4 import BeautifulSoup

url = 'https://pharmeasy.in/health-care/products/drools-absolute-calcium-bone-pouch-190g-3553168'
print(url)
headers = {
    'User-Agent': 'test'
}
f = requests.get(url, headers=headers)
soup = BeautifulSoup(f.content, 'lxml')

p = soup.find('script',{'id':'__NEXT_DATA__'})

data = json.loads(p.get_text())
prod = data['props']['pageProps']['productDetails']
print(prod['name'])
print(prod['manufacturer'])
print(",".join(prod['compositions']))
print(prod['salePrice'])
print(prod['productSpecifications'][0]['tableData'][0]['value'])
print('category')

"""
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
      '-', p_price)"""