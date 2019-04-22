# dependencies
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from splinter import Browser
from selenium import webdriver
import requests

def init_browser():
    # chromedriver executable path
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)
    
def scrape():
    browser = init_browser()
    mars_facts_data = {}

    #URL
    url_mars = "https://mars.nasa.gov/news/"
    browser.visit(url_mars)
    #HTML
    html_mars = browser.html
    #BeatuifulSoup
    soup = BeautifulSoup(html_mars, 'html.parser')

    #Retrieving our variables
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text
    
    #Adding to the list
    mars_facts_data['news_title'] = news_title
    mars_facts_data['news_p'] = news_p
####
    #URL
    url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_image)
    time.sleep(3)
    #HTML
    html_image = browser.html
    #BeautifulSoup
    soup = BeautifulSoup(html_image, 'html.parser')
    
    #Use of style to retrieve the image URL; cleaning the URL
    featured_img_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

    #Main URL
    main_url = 'https://www.jpl.nasa.gov'

    #Combining two URLs
    final_image = main_url + url_image
    
    #Adding to the list
    mars_facts_data['featured_image'] = featured_img_url
####
    #URL
    url_weather = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_weather)
    time.sleep(5)
    #HTML
    html_weather = browser.html
    #SOUPSOUPSOUP
    soup = BeautifulSoup(html_weather, 'html.parser')

    #Grabbing the tweet
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    
    #Adding to list
    mars_facts_data['mars_weather'] = mars_weather
####
    #URL
    url_facts = 'http://space-facts.com/mars/'

    #Grabbing data for our table to convert into DF
    scrape_table = pd.read_html(url_facts)
    scrape_table[0]

    #Loading the table into a DF
    mars_facts_df = scrape_table[0]

    #Renaming columns, further cleaning
    mars_facts_df.rename(columns={0: 'Fact', 1: 'Value'}, inplace=True)
    mars_facts_df.set_index('Fact')
    
    #Converting DF into HTML string
    mars_html_table = mars_facts_df.to_html()
    mars_html_table.replace('\n', '')

    #Adding to list
    mars_facts_data['mars_facts_table'] = mars_html_table
#####
    # set url where we will scrape hemispheres images
    url_hemisphere_main = "https://astrogeology.usgs.gov"
    url_hemisphere_specific = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    
    # Retrieve page with the requests module
    response = requests.get(url_hemisphere_specific)
    
    # create bs object and visit url
    soup = BeautifulSoup(response.text, 'html.parser')
    browser.visit(url_hemisphere_specific)

    # parse html with bs
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # results are returned as an iterable list
    hemispheres = soup.find_all('a', class_="itemLink")

    # Loop through returned results
    hemisphere_img_urls = []

    for result in hemispheres:

        try:
            # find title
            title = result.find('h3').text

            # find link
            link = result['href']
            print("title: ", title)

            # use the full url
            full_link = url_hemisphere_main + link
            print("full-link: ", full_link)

            # go to the link to get to the page with the full image
            response = requests.get(full_link)
            # parse with bs 
            soup = BeautifulSoup(response.text, 'html.parser')

            try:

                # get full image url from href
                download = soup.find('div', class_='downloads')
                full_href = download.find('a')['href']
                print("full_href: ", full_href)

                # put title and image URL into dictionary
                hemisphere_img_urls.append({"title": title, "img_url": full_href})


            except Exception as f:
                print("f: ", f)

        except Exception as e:
            print("e: ", e)

        mars_facts_data['hemisphere_img_url'] = hemisphere_img_urls

    return mars_facts_data