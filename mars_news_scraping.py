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

    #Pause Code 5 Seconds
    time.sleep(5)

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

    #Pause Code 5 Seconds
    time.sleep(5)

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

    #Pause Code 5 Seconds
    time.sleep(5)

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

    #Pause Code 5 Seconds
    time.sleep(5)

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

    #Define URL for Mars Hemispheres Site
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    #Open Mars Hemispheres Site in Chrome
    hemispheres_site = browser.visit(hemispheres_url)

    #Request HTML Information from Mars Hemispheres Site
    hemispheres_info = browser.html
  
    #Parse HTML Information
    hemispheres_soup = bs(hemispheres_info, 'html5lib')

    #Pause Code 2 Seconds
    time.sleep(2)

    #Create List for Hemisphere Names & Hemiphere Page Links
    hemispheres_names = []
    hemispheres_links = []

    #Loop Through All H3 Tags & Add Hemisphere Names to Appropriate List
    for name in hemispheres_soup.find_all('h3'):
        current_name = name.text.replace('Enhanced','')

        hemispheres_names.append(current_name)
    
    #Set Counter Variable
    count_1 = 0

    #Loop Through Attribute Tages & Add Hemisphere Page Links to Appropriate List
    for data in hemispheres_soup.find_all('a', class_ = 'itemLink product-item'):
        if count_1 == 0:
            hemispheres_links.append('https://astrogeology.usgs.gov' + data.get('href'))
        else:
            if 'https://astrogeology.usgs.gov' + data.get('href') == hemispheres_links[-1]:
                pass
            else:
                hemispheres_links.append('https://astrogeology.usgs.gov' + data.get('href'))
            
        count_1 = count_1 + 1

    #Create Blank List for Hemispheres Data
    hemispheres_images = []

    #Loop Through Length of Hemisphere Page Link List
    for count_2 in range(0, len(hemispheres_links)):

        #Open Mars Hemispheres Site in Chrome
        hemisphere_site = browser.visit(hemispheres_links[count_2])

        #Request HTML Information from Mars Hemispheres Site
        hemisphere_info = browser.html
  
        #Parse HTML Information
        hemisphere_soup = bs(hemisphere_info, 'html5lib') 
    
        #Extract Hemisphere Image Link
        hemisphere_link = 'https://astrogeology.usgs.gov' + hemisphere_soup.find('img', class_ = 'wide-image').get('src')
    
        #Create Python Dictionary of Hemisphere Name & Image Link & Append to Hemisphere Data List
        hemispheres_images.append({'name': hemispheres_names[count_2], 'link': hemisphere_link})

    #Create Dictionary of Scraped Data
    scraped_data = {'mars_news': {'title': news_title, 'description': news_text}, 'mars_image': featured_image,
                    'mars_weather': weather_report, 'mars_facts': facts_html, 'mars_hemispheres': hemispheres_images}

    #Return Dictionary of Scraped Data
    return scraped_data