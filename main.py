import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_'
# The variable headers is a dictionary which has the value of user_agent, we can get our user agent by direct googling it
# headers ={'user-agent':"add the link here and remove the comment"}
pages_to_scrape = 20
fieldnames = ['Product URL', 'Product Name', 'Product Price', 'Rating', 'Number of reviews']
with open('products.csv', 'w',encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)

    for i in range(1, pages_to_scrape+1):
        page_url = url + str(i)
        response = requests.get(page_url,headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        products = soup.find_all('div', class_='sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16')
    

        for product in products:
            product_url = "http://amazon.in"+str(product.find('a')['href'])
            product_name = product.find('span', class_='a-size-medium a-color-base a-text-normal').text.strip()
            product_price = product.find('span', class_='a-price-whole').text.strip()
            rating = product.find('span', class_='a-size-base').text.strip()
            num_reviews = product.find('span', class_='a-size-base s-underline-text').text.strip()
            num_reviews_modified = num_reviews[1:-1]

            # Save the scraped data into a CSV file
            with open('products.csv', 'a',encoding='utf-8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([product_url,product_name,product_price,rating,num_reviews_modified])
