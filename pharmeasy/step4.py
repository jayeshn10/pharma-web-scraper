import pandas as pd
from pandas import read_excel

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


df2 = read_excel('pharmeasy_1_final.xlsx')

df = df.append(df2, ignore_index=True)

df2 = read_excel('pharmeasy_2_final.xlsx')

df = df.append(df2, ignore_index=True)

df.to_excel("pharmeasy_final.xlsx")
