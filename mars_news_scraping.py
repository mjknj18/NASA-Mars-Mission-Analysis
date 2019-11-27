#Define Scraping Function
def scrape():
    #Import Modules
    import pandas as pd
    import requests
    from splinter import Browser
    from bs4 import BeautifulSoup as bs
    import urllib.request
    import time

    #Open Chrome Window
    browser = Browser('chrome')

    #Define URL for NASA Mars News Site
    news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    #Open NASA Mars News Site in Chrome
    news_site = browser.visit(news_url)

    #Request HTML Information from Mars News Site
    news_info = browser.html
  
    #Parse HTML Information
    news_soup = bs(news_info, 'html5lib')

    #Pause Code 2 Seconds
    time.sleep(2)

    #Record Title of Latest Mars News Article
    news_title = news_soup.find('div', class_ = "content_title").text

    #Record Description of Latest Mars News Article
    news_text = news_soup.find('div', class_ = "article_teaser_body").text

    #Define URL for JPL Featured Space Image Site
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    #Open JPL Featured Space Image Site in Chrome
    image_site = browser.visit(image_url)

    #Request HTML Information from JPL Featured Space Image Site
    image_info = browser.html
  
    #Parse HTML Information
    image_soup = bs(image_info, 'html5lib')

    #Pause Code 2 Seconds
    time.sleep(2)

    #Record URL of JPL Featured Space Image
    featured_image = 'https://www.jpl.nasa.gov' + image_soup.find('a', class_ = 'button fancybox').get('data-fancybox-href')

    #Define URL for Mars Weather Twitter Site
    weather_url = 'https://twitter.com/marswxreport?lang=en'

    #Open Mars Weather Twitter Site in Chrome
    weather_site = browser.visit(weather_url)

    #Request HTML Information from Mars Weather Twitter Site
    weather_info = browser.html
  
    #Parse HTML Information
    weather_soup = bs(weather_info, 'html5lib') 

    #Pause Code 2 Seconds
    time.sleep(2)

    #Extract Latest Weather Report & Image Data from Mars Weather Twitter Site
    weather_report = weather_soup.find('p', class_ = 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    weather_images = weather_soup.find('a', class_ =  'twitter-timeline-link u-hidden')

    #Remove Latest Weather Image Data & '\n' Characters from Latest Weather Information
    weather_report = weather_report.replace(weather_images.text, '').replace('\n', ' ')

    #Add Commas to Separate Data Types
    weather_report = weather_report.replace(') ', '), ')

    #Define URL for Mars Facts Site
    facts_url = 'https://space-facts.com/mars/'

    #Open Mars Facts Site in Chrome
    facts_site = browser.visit(facts_url)

    #Request HTML Information from Mars Facts Site
    facts_info = browser.html
  
    #Parse HTML Information
    facts_soup = bs(facts_info, 'html5lib') 

    #Pause Code 2 Seconds
    time.sleep(2)

    #Extract Data from Mars Planet Profile Table
    facts_table = facts_soup.find('table', class_ = 'tablepress tablepress-id-p-mars')
    facts_rows = facts_table.find_all('tr')

    #Define Blank List for Table Text Data
    facts_text = []

    #Loop Through Table Row Data to Extract Text Data
    for tr in facts_rows:
        td = tr.find_all('td')
        text_data = [tr.text for tr in td]
        facts_text.append(text_data)
    
    #Create Pandas Data Frame of Table Text Data
    facts_df = pd.DataFrame(facts_text, columns=['Mars Facts', '']).set_index('Mars Facts')

    #Convert Data Frame of Mars Facts to HTML
    facts_html = facts_df.to_html()

    #Create Dictionary of Scraped Data
    scraped_data = {'mars_news': {'title': news_title, 'description': news_text}, 'mars_image': featured_image,
                    'mars_weather': weather_report, 'mars_facts': facts_html}

    print(scraped_data)