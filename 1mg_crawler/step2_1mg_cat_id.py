import re

import pandas as pd

dict = {'category': [],
        'sub-category': [],
        'category-id': []
        }

df = pd.DataFrame(dict)




dfx = pd.read_csv('med_cat.csv')


for index, row in dfx.iterrows():
    res = re.findall(r'\d+', row['category url'][-4:])
    print(res[0])

    df2 = {'category': row['category'], 'sub-category': row['sub-category'], 'category-id': res[0]}
    df = df.append(df2, ignore_index=True)

df.to_csv('med_cat_id.csv')