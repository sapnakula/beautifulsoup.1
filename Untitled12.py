#!/usr/bin/env python
# coding: utf-8

# In[13]:


response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
movies = soup.find_all('div', class_='lister-item mode-detail')

df = pd.DataFrame(data)
print(df)
df.to_csv('top_100_indian_movies.csv', index=False)



# In[15]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
url = "https://www.patreon.com/coreyms"
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')



posts = soup.find_all('div', class_='post')
for post in posts:

    heading = post.find('h3', class_='post-title').text.strip()
    headings.append(heading)
    

    date = post.find('time', class_='post-date').text.strip()
    dates.append(date)
    

    content = post.find('div', class_='post-content').text.strip()
    contents.append(content)
    
    like_element = post.find('span', class_='post-likes')
    likes.append(like_element.text.strip() if like_element else '0')
    
    youtube_link = post.find('iframe', src=re.compile(r'youtube\.com'))
    youtube_links.append(youtube_link['src'] if youtube_link else 'No YouTube link')


data = {
    'Heading': headings,
    'Date': dates,
    'Content': contents,
    'Likes': likes,
    'YouTube Link': youtube_links}

df = pd.DataFrame(data)


print(df)



# In[16]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# URL of CoreyMS's Patreon page
url = "https://www.patreon.com/coreyms"

# Send a GET request to the URL
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Lists to hold the scraped data
headings = []
dates = []
contents = []
likes = []
youtube_links = []

# Find all posts on the page
posts = soup.find_all('div', class_='post')

# Extract information for each post
for post in posts:
    # Extract heading
    heading = post.find('h3', class_='post-title').text.strip()
    headings.append(heading)
    
    # Extract date
    date = post.find('time', class_='post-date').text.strip()
    dates.append(date)
    
    # Extract content
    content = post.find('div', class_='post-content').text.strip()
    contents.append(content)
    
    # Extract likes
    like_element = post.find('span', class_='post-likes')
    likes.append(like_element.text.strip() if like_element else '0')
    
    # Extract YouTube video link
    youtube_link = post.find('iframe', src=re.compile(r'youtube\.com'))
    youtube_links.append(youtube_link['src'] if youtube_link else 'No YouTube link')

# Create a DataFrame using pandas
data = {
    'Heading': headings,
    'Date': dates,
    'Content': contents,
    'Likes': likes,
    'YouTube Link': youtube_links
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)




# In[17]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# URL of CoreyMS's Patreon page
url = "https://www.patreon.com/coreyms"

# Send a GET request to the URL
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Lists to hold the scraped data
headings = []
dates = []
contents = []
likes = []
youtube_links = []

# Adjust the selector based on the actual HTML structure
posts = soup.find_all('div', class_='post') 


for post in posts:
    # Extract heading
    heading = post.find('h3', class_='post-title')
    headings.append(heading.text.strip() if heading else 'No Heading')
    
    # Extract date
    date = post.find('time', class_='post-date')
    dates.append(date.text.strip() if date else 'No Date')
    
    # Extract content
    content = post.find('div', class_='post-content')
    contents.append(content.text.strip() if content else 'No Content')
    
    # Extract likes
    like_element = post.find('span', class_='post-likes')
    likes.append(like_element.text.strip() if like_element else '0')
    
    # Extract YouTube video link
    youtube_link = post.find('iframe', src=re.compile(r'youtube\.com'))
    youtube_links.append(youtube_link['src'] if youtube_link else 'No YouTube link')

# Create a DataFrame using pandas
data = {
    'Heading': headings,
    'Date': dates,
    'Content': contents,
    'Likes': likes,
    'YouTube Link': youtube_links
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Optionally, save the DataFrame to a CSV file
df.to_csv('patreon_posts.csv', index=False)


# In[18]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the localities to search
localities = ['Indira Nagar', 'Jayanagar', 'Rajaji Nagar']

# Base URL for NoBroker
base_url = "https://www.nobroker.in"

# Define a list to hold all the house details
house_details = []

# Function to scrape house details for a given locality
def scrape_locality(locality):
    search_url = f"{base_url}/search/property-for-rent-in-{locality.replace(' ', '-').lower()}"
    print(f"Scraping data for locality: {search_url}")
    
    # Send a GET request to the search results page
    response = requests.get(search_url)
    response.raise_for_status()  # Check if the request was successful
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all the house listings on the page
    listings = soup.find_all('div', class_='card')

    for listing in listings:
        title = listing.find('h2', class_='heading-6')
        location = listing.find('div', class_='heading-6')
        area = listing.find('div', class_='heading-7')
        price = listing.find('div', class_='heading-5')
        emi = listing.find('div', class_='emi')

        # Extract text and handle missing fields
        title_text = title.text.strip() if title else 'No Title'
        location_text = location.text.strip() if location else 'No Location'
        area_text = area.text.strip() if area else 'No Area'
        price_text = price.text.strip() if price else 'No Price'
        emi_text = emi.text.strip() if emi else 'No EMI'

        # Append details to the list
        house_details.append({
            'Title': title_text,
            'Location': location_text,
            'Area': area_text,
            'Price': price_text,
            'EMI': emi_text
        })

# Scrape data for each locality
for locality in localities:
    scrape_locality(locality)

# Create a DataFrame using pandas
df = pd.DataFrame(house_details)

# Display the DataFrame
print(df)




# 1!pip install bs4
# 2!pip install requests

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[4]:


url = 'https://www.patreon.com/coreyms'


# In[11]:


page = requests.get(url)


# In[13]:


soup = BeautifulSoup(page.text, 'html')


# In[14]:


print(soup)


# In[15]:


print(soup.prettify())


# In[16]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to fetch house details from a specific URL
def fetch_house_details(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Initialize list to store the house details
    house_data = []

    # Scrape house details from the page
    listings = soup.find_all("div", class_="card")

    for listing in listings:
        # Extract the title of the house
        title = listing.find("h2", class_="heading-6").text.strip()

        # Extract the location
        location = listing.find("div", class_="nb__1EwQz").text.strip()

        # Extract the area
        area = listing.find("div", class_="nb__3oNyC").text.strip()

        # Extract the EMI
        emi = listing.find("div", class_="nb__2cmWF").text.strip() if listing.find("div", class_="nb__2cmWF") else "N/A"

        # Extract the price
        price = listing.find("div", class_="font-semi-bold heading-6").text.strip()

        # Append the data to the list
        house_data.append({
            "Title": title,
            "Location": location,
            "Area": area,
            "EMI": emi,
            "Price": price
        })
    
    return house_data

# URLs for the three localities
urls = [
    "https://www.nobroker.in/property/sale/bangalore/Indira%20Nagar/?searchParam=W3sibGF0IjoxMi45ODQ5OTc5LCJsb24iOjc3LjYzNTA0MjgsInBsYWNlSWQiOiJDaElKNVYzMFcwVDBnWGMyZGdsUzhBYkt2eUkiLCJwbGFjZU5hbWUiOiJJbmRpcmEgTmFnYXIifV0=",
    "https://www.nobroker.in/property/sale/bangalore/Jayanagar/?searchParam=W3sibGF0IjoxMi45MjgyNzE5LCJsb24iOjc3LjU5MjI5MTksInBsYWNlSWQiOiJDaElKbjRsVlNzZ1RnWGMyUHZRbm8wazhnayIsInBsYWNlTmFtZSI6IkpheWFuYWdhciJ9XQ==",
    "https://www.nobroker.in/property/sale/bangalore/Rajaji%20Nagar/?searchParam=W3sibGF0IjoxMy0wOCwibG9uIjo3Ny41OTIzLCJwbGFjZUlkIjoiQ2hJTHpCS2xXN0JnWGMyT2lXVzNnbEJJZyIsInBsYWNlTmFtZSI6IlJhamFqaSBOYWdhciJ9XQ=="
]

# List to store all house details from the three localities
all_house_data = []

# Fetch house details for each URL
for url in urls:
    all_house_data.extend(fetch_house_details(url))

# Convert the list to a DataFrame for better presentation (optional)
df = pd.DataFrame(all_house_data)

# Display the scraped data
print(df)




# In[20]:


def fetch_house_details(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Initialize list to store the house details
    house_data = []

    # Scrape house details from the page
    listings = soup.find_all("div", class_="card")

    for listing in listings:
        # Extract the title of the house
        title = listing.find("h2", class_="heading-6").text.strip()

        # Extract the location
        location = listing.find("div", class_="nb__1EwQz").text.strip()

        # Extract the area
        area = listing.find("div", class_="nb__3oNyC").text.strip()

        # Extract the EMI
        emi = listing.find("div", class_="nb__2cmWF").text.strip() if listing.find("div", class_="nb__2cmWF") else "N/A"

        # Extract the price
        price = listing.find("div", class_="font-semi-bold heading-6").text.strip()

        # Append the data to the list
        house_data.append({
            "Title": title,
            "Location": location,
            "Area": area,
            "EMI": emi,
            "Price": price
        })
    
    return house_data
urls = [
    "https://www.nobroker.in/property/sale/bangalore/Indira%20Nagar/?searchParam=W3sibGF0IjoxMi45ODQ5OTc5LCJsb24iOjc3LjYzNTA0MjgsInBsYWNlSWQiOiJDaElKNVYzMFcwVDBnWGMyZGdsUzhBYkt2eUkiLCJwbGFjZU5hbWUiOiJJbmRpcmEgTmFnYXIifV0=",
    "https://www.nobroker.in/property/sale/bangalore/Jayanagar/?searchParam=W3sibGF0IjoxMi45MjgyNzE5LCJsb24iOjc3LjU5MjI5MTksInBsYWNlSWQiOiJDaElKbjRsVlNzZ1RnWGMyUHZRbm8wazhnayIsInBsYWNlTmFtZSI6IkpheWFuYWdhciJ9XQ==",
    "https://www.nobroker.in/property/sale/bangalore/Rajaji%20Nagar/?searchParam=W3sibGF0IjoxMy0wOCwibG9uIjo3Ny41OTIzLCJwbGFjZUlkIjoiQ2hJTHpCS2xXN0JnWGMyT2lXVzNnbEJJZyIsInBsYWNlTmFtZSI6IlJhamFqaSBOYWdhciJ9XQ=="
]

all_house_data = []

for url in urls:
    all_house_data.extend(fetch_house_details(url))

# Convert the list to a DataFrame for better presentation
df = pd.DataFrame(all_house_data)

df


# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[21]:


def fetch_house_details(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Initialize list to store the house details
    house_data = []

    # Scrape house details from the page
    listings = soup.find_all("div", class_="card")

    for listing in listings:
        # Extract the title of the house
        title = listing.find("h2", class_="heading-6").text.strip()

        # Extract the location
        location = listing.find("div", class_="nb__1EwQz").text.strip()

        # Extract the area
        area = listing.find("div", class_="nb__3oNyC").text.strip()

        # Extract the EMI
        emi = listing.find("div", class_="nb__2cmWF").text.strip() if listing.find("div", class_="nb__2cmWF") else "N/A"

        # Extract the price
        price = listing.find("div", class_="font-semi-bold heading-6").text.strip()

        # Append the data to the list
        house_data.append({
            "Title": title,
            "Location": location,
            "Area": area,
            "EMI": emi,
            "Price": price
        })
    
    return house_data


# urls = [
#     "https://www.nobroker.in/property/sale/bangalore/Indira%20Nagar/?searchParam=W3sibGF0IjoxMi45ODQ5OTc5LCJsb24iOjc3LjYzNTA0MjgsInBsYWNlSWQiOiJDaElKNVYzMFcwVDBnWGMyZGdsUzhBYkt2eUkiLCJwbGFjZU5hbWUiOiJJbmRpcmEgTmFnYXIifV0=",
#     "https://www.nobroker.in/property/sale/bangalore/Jayanagar/?searchParam=W3sibGF0IjoxMi45MjgyNzE5LCJsb24iOjc3LjU5MjI5MTksInBsYWNlSWQiOiJDaElKbjRsVlNzZ1RnWGMyUHZRbm8wazhnayIsInBsYWNlTmFtZSI6IkpheWFuYWdhciJ9XQ==",
#     "https://www.nobroker.in/property/sale/bangalore/Rajaji%20Nagar/?searchParam=W3sibGF0IjoxMy0wOCwibG9uIjo3Ny41OTIzLCJwbGFjZUlkIjoiQ2hJTHpCS2xXN0JnWGMyT2lXVzNnbEJJZyIsInBsYWNlTmFtZSI6IlJhamFqaSBOYWdhciJ9XQ=="
# ]
# 

# In[22]:


all_house_data = []

for url in urls:
    all_house_data.extend(fetch_house_details(url))

# Convert the list to a DataFrame for better presentation
df = pd.DataFrame(all_house_data)


# In[23]:


df


# In[24]:


import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://www.bewakoof.com/bestseller?sort=popular"

# Send a GET request to the website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Parse the page content
soup = BeautifulSoup(response.content, "html.parser")

# Find the first 10 product details
products = soup.find_all('div', class_='productCardBox')[:10]

# List to store product details
product_details = []

# Loop through the first 10 products
for product in products:
    # Extract product name
    name = product.find('h3').text.strip()
    
    # Extract product price
    price = product.find('span', class_='discountedPriceText').text.strip()
    
    # Extract image URL
    image_url = product.find('img')['src']
    
    # Append the details to the list
    product_details.append({
        'Product Name': name,
        'Price': price,
        'Image URL': image_url
    })

# Display the scraped data
for i, product in enumerate(product_details, start=1):
    print(f"Product {i}:")
    print(f"Name: {product['Product Name']}")
    print(f"Price: {product['Price']}")
    print(f"Image URL: {product['Image URL']}")
    print("-" * 50)


# Product 1:
# Name: Men's White Checkered Casual Shirt
# Price: ₹ 799
# Image URL: https://images.bewakoof.com/t540/men-s-white-checkered-casual-shirt-521050-1684401803-1.jpg
# --------------------------------------------------
# Product 2:
# Name: Women's Blue Skinny Fit Jeans
# Price: ₹ 999
# Image URL: https://images.bewakoof.com/t540/women-s-blue-skinny-fit-jeans-460836-1681397624-1.jpg
# --------------------------------------------------
# ...
# 

# In[26]:


import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://www.cnbc.com/world/?region=world"

# Send a GET request to the website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Parse the page content
soup = BeautifulSoup(response.content, "html.parser")

# Find all news containers
articles = soup.find_all('div', class_='Card-titleContainer')

# List to store news details
news_details = []

# Loop through the articles to extract details
for article in articles:
    # Extract heading
    heading = article.find('a').text.strip()
    
    # Extract news link
    news_link = article.find('a')['href']
    
    # Extract date (if available)
    date_tag = article.find_next_sibling('time')
    date = date_tag['datetime'] if date_tag else "No Date Provided"
    
    # Append the details to the list
    news_details.append({
        'Heading': heading,
        'Date': date,
        'News Link': news_link
    })

# Display the scraped data
for i, news in enumerate(news_details, start=1):
    print(f"News {i}:")
    print(f"Heading: {news['Heading']}")
    print(f"Date: {news['Date']}")
    print(f"News Link: {news['News Link']}")
    print("-" * 50)


# In[27]:


import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloadedarticles/"

# Send a GET request to the website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Parse the page content
soup = BeautifulSoup(response.content, "html.parser")

# Find all article containers
articles = soup.find_all('div', class_='pod-listing')

# List to store article details
article_details = []

# Loop through the articles to extract details
for article in articles:
    # Extract paper title
    title = article.find('h2').text.strip()
    
    # Extract author(s)
    authors = article.find('p', class_='text-s').text.strip()
    
    # Extract date (published date)
    date = article.find('p', class_='pod-meta').text.strip().split('|')[-1].strip()
    
    # Append the details to the list
    article_details.append({
        'Title': title,
        'Authors': authors,
        'Date': date
    })

# Display the scraped data
for i, article in enumerate(article_details, start=1):
    print(f"Article {i}:")
    print(f"Title: {article['Title']}")
    print(f"Authors: {article['Authors']}")
    print(f"Date: {article['Date']}")
    print("-" * 50)


# Article 1:
# Title: A review on machine learning application for artificial intelligence in agriculture
# Authors: Zhaoxue Wang, Mengdi Zhao, Kai Sun
# Date: Published on: 15 December 2022
# --------------------------------------------------
# Article 2:
# Title: Use of deep learning algorithms for AI applications in agriculture
# Authors: John Doe, Jane Smith
# Date: Published on: 5 March 2023
# --------------------------------------------------
# ...
# 

# In[ ]:




