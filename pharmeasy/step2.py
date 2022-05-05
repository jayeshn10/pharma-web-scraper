import json
from itertools import count

import pandas as pd
import requests
from bs4 import BeautifulSoup

lst = [
    ['Personal Care', 877, 120],
    ['Health Food and Drinks', 648, 37],
    ['Skin Care', 93, 31],
    ['Home Care', 734, 15],
    ['Ayurvedic Care', 765, 33],
    ['Sexual Wellness', 575, 11],
    ['Fitness & Supplements', 623, 36],
    ['Mother and Baby Care', 838, 29],
    ['Healthcare Devices', 717, 10],
    ['Surgicals and Dressings', 599, 6],
    ['Covid Essentials', 109, 29],
    ['Health Condition', 693, 31],
    ['Diabetic Care', 145, 12],
    ['Elderly Care', 750, 26],
    ['Accessories And Wearables', 788, 25],
    ['Pet Care', 178, 5],
]
dict = {
    'Category': [],
    'Product listing url': [],
}

df = pd.DataFrame(dict)
itr = 0
# https://pharmeasy.in/api/otc/getCategoryProducts?categoryId=178&page=6

for l in lst:
    for i in range(1, l[2]):
        response = requests.get(str(f'https://pharmeasy.in/api/otc/getCategoryProducts?categoryId=877&page={l[1]}&perPage=50'))

        data = response.json()
        prod_list = data['data']['products']

        for prod in prod_list:
            url = 'https://pharmeasy.in/health-care/products/' + prod['slug']
            df2 = {
                'Category': l[0],
                'Product listing url': url,
            }

            df = df.append(df2, ignore_index=True)
            print(l[0], url)

df.to_excel("pharmeasy_prod_url.xlsx")
