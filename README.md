# NASA-Mars-Mission-Analysis

The goal of this project was to develop a webpage to present scraped data from several NASA Mars Mission websites. Python with BeautifulSoup and MongoGB were used to scrape and store the required data, and Python with Flask was used to automate that process. HTML with Bootstrap CSS was used to generate and formate the completed webpage presenting the scraped data.

## Questions

1. What are the name and summary of the latest Mars news article?
2. What is the latest Mars featured image?
3. What is the latest Mars weather report?
4. What are the latest Mars facts?

## Datasets

1. https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest
2. https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
3. https://twitter.com/marswxreport?lang=en
4. https://space-facts.com/mars/

## Tasks

### Web Scraping

1. Create a connection to chrome browser using Splinter.
2. Auto-load the Mars news article webpage in the browser and scrape the data.
3. Parse the HTML data, and extract title and summary of latest article.
4. Auto-load the Mars featured image webpage in the browser and scrape the data.
5. Parse the HTML data, and extract link of latest Mars featured image.
6. Auto-load the Mars weather twitter webpage in the browser and scrape the data.
7. Parse the HTML data, and extract the text of the latest Mars weather report.
8. Auto-load the Mars facts webpage in the browser and scrape the data.
9. Parse the HTML data, and extract the table of the latest Mars facts.

### Flask App



### HTML Webpage



## Results

1. http://localhost:5000/ (Flask App and MongoDB must be running on local machine to enable full site functionality)