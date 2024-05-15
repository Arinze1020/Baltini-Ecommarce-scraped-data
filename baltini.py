import os
from bs4 import BeautifulSoup
products = []
for filename in os.listdir("baltini"):
        if filename.endswith(".html"):
            file_path = os.path.join("baltini", filename)
            with open(file_path, 'rb') as f:
                print(f)
                soup = BeautifulSoup(f.read(), 'lxml')
                data = soup.find('ul', class_='snize-search-results-content clearfix')
                

                items = data.find_all('li') # Use a common container

                for item in items:
                    name = item.find('span', class_='snize-title').text.strip()
                    link = "https://www.baltini.com"+item.find('a', class_='snize-view-link')['href']
                    img = item.find('img', class_='snize-item-image')['src']

                    first_price = item.find('span', class_='snize-price snize-price-with-discount')
                    price = first_price.text.strip() if first_price else 'NA'

                    dis_count = item.find('span', class_="snize-discounted-price")
                    discount = dis_count.text.strip() if dis_count else 'NA'

                    brand_id = item.find('span', class_='snize-attribute').text.strip()
                    idd = item.get('id')

                    product = {
                        'brand': brand_id,
                        'product_code':idd,
                        'full_price': discount,
                        'price': price,
                        'title': name,
                        'imageurl': img,
                        'itemurl': link,
                        
                    }
                    products.append(product)
                print(len(products))
import pandas as pd
df = pd.DataFrame(products)
df.to_csv('data_blint.csv')
