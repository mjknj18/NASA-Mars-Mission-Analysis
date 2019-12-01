# NASA-Mars-Mission-Analysis

The goal of this project was to develop a webpage to present scraped data from several NASA Mars Mission websites. Python with Splinter, BeautifulSoup, and Pandas, and MongoDB were used to scrape and store the required data, and Python with Flask was used to automate those processes. HTML with Bootstrap CSS was used to generate and format the completed webpage presenting the scraped data.

## Questions

1. Find and present the name and summary of the latest Mars news article.
2. Find and present the latest Mars featured image.
3. Find and present the latest Mars weather report.
4. Find and present the latest Mars facts.

## Datasets

1. https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest
2. https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
3. https://twitter.com/marswxreport?lang=en
4. https://space-facts.com/mars/

## Tasks

### Web Scraping

1. Create a connection to the Google Chrome browser.
2. Auto-load the Mars news webpage in the browser and scrape the data.
3. Parse the HTML data, and extract the title and summary of the latest article.
4. Auto-load the Mars images webpage in the browser and scrape the data.
5. Parse the HTML data, and extract the link of the latest Mars featured image.
6. Auto-load the Mars weather Twitter webpage in the browser and scrape the data.
7. Parse the HTML data, and extract the text of the latest Mars weather report.
8. Auto-load the Mars facts webpage in the browser and scrape the data.
9. Parse the HTML data, and extract the table of the latest Mars facts.
10. Compile all of the extracted data into a Python dictionary.

### Flask App Development

1. Create a connection to the MongoDB engine, and set the path to the appropriate database and collection.
2. Create a Scrape route that imports and calls the Python scraping code, and stores the outputted Python dictionary in MongoDB.
3. Create a Home route that loads the stored Python dictionary from MongoDB and passes it to the HTML webpage.

### HTML Webpage Development

1. Create a navigation bar with a header and a button that calls the Scrape route from the Flask App.
2. Create a content card for the name and summary of the latest Mars news article.
3. Create a content card for the latest Mars featured image.
4. Create a content card for the latest Mars weather report.
5. Create a content card for the latest Mars facts.

## Results

1. http://localhost:5000/ (Python Flask App and MongoDB must be running on the local machine to enable full site functionality.)