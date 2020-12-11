#!/usr/bin/env python
# coding: utf-8

# In[8]:


#import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time


# In[9]:


# Import BeautifulSoup for parsing and splinter for site navigation
from bs4 import BeautifulSoup
from splinter import Browser
executable_path = {"executable_path":"C:\chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# In[10]:


# Visit the NASA news URL
url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[11]:


# Scrape page into soup
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[12]:


# save the most recent article, title and date
article = soup.find("div", class_="list_text")
news_para = article.find("div", class_="article_teaser_body").text
news_title = article.find("div", class_="content_title").text
news_date = article.find("div", class_="list_date").text
print(news_date)
print(f"Title: {news_title}")
print(f"Para: {news_para}")


# In[13]:


# Visit the JPL Mars URL
url2 = "https://jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url2)

# Scrape the browser into soup and use soup to find the image of mars
# Save the image url to a variable called `img_url`
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
image = soup.find("img", class_="thumb")["src"]
img_url = "https://jpl.nasa.gov"+image
featured_image_url = img_url
# Use the requests library to download and save the image from the `img_url` above
import requests
import shutil
response = requests.get(img_url, stream=True)
with open('img.jpg', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
    
# Display the image with IPython.display
from IPython.display import Image
Image(url='img.jpg')


# In[14]:


# Visit the Mars facts webpage and scrape table data into Pandas
url3 = "http://space-facts.com/mars/"
browser.visit(url3)


# In[15]:


# place data into a dataframe, clean it up and output it into an HTML table
import pandas as pd 
grab=pd.read_html(url3)
mars_data=pd.DataFrame(grab[0])
mars_data.columns=['Mars','Data']
mars_table=mars_data.set_index("Mars")
marsdata = mars_table.to_html(classes='marsdata')
marsdata=marsdata.replace('\n', ' ')
marsdata


# In[16]:


# Visit the USGS Astogeology site and scrape pictures of the hemispheres
url4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url4)


# In[17]:


# Use splinter to loop through the 4 images and load them into a dictionary
import time 
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
mars_hemis=[]


# In[18]:


# loop through the four tags and load the data to the dictionary

for i in range (4):
    time.sleep(5)
    images = browser.find_by_tag('h3')
    images[i].click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    partial = soup.find("img", class_="wide-image")["src"]
    img_title = soup.find("h2",class_="title").text
    img_url = 'https://astrogeology.usgs.gov'+ partial
    dictionary={"title":img_title,"img_url":img_url}
    mars_hemis.append(dictionary)
    browser.back()


# In[19]:


print(mars_hemis)


# In[ ]:




