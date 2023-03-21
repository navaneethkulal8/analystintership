import csv
import requests
from bs4 import BeautifulSoup


# The variable headers is a dictionary which has the value of user_agent, we can get our user agent by direct googling it
headers ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
with open('products.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    product_urls = [row[0] for row in reader]

s = "https://www.amazon.in/ADISA-Laptop-Backpack-Office-College/dp/B09TPX22NF/ref=sr_1_6?crid=2M096C61O4MLT&keywords=bags&qid=1679429943&sprefix=ba%2Caps%2C283&sr=8-6%2CADISA&th=1"

response = requests.get(s,headers=headers)
html_content = response.content


soup = BeautifulSoup(html_content, 'html.parser')


# data1 = soup.find_all('ul',class_='a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list')
# for li in data1.find_all("li"):
#     print(li.text, end=" ")

children = soup.find('div',id="detailBullets_feature_div")
children2 = children.contexts[1]
print(children2)
# children = soup.find_all('ul',class_='a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list')[1]
# print(children)
# children2 = children.find("li")

# print(children2.prettify())



# for url in product_urls:
#      print(url)


    
#     response = requests.get(url)
#     html_content = response.content

    
#     soup = BeautifulSoup(html_content, 'html.parser')

    
#     description = soup.find('h1', {'class': 'a-size-large'}).text.strip()
    
   
#     asin = soup.find('th', {'class': 'prodDetSectionEntry'}).text.strip()

    
#     product_description = soup.find('div', {'id': 'productDescription'}).text.strip()

    
#     manufacturer = soup.find('a', {'id': 'bylineInfo'}).text.strip()

    
#     print(f'URL: {url}\nDescription: {description}\nASIN: {asin}\nProduct Description: {product_description}\nManufacturer: {manufacturer}\n')
