#Import Modules
import flask
from flask import request, jsonify, render_template
import numpy as np
import pandas as pd
import pymongo

#Define Flask App Environment
app = flask.Flask(__name__, template_folder = 'C:/Users/mjknj/Desktop/UNCC/Homework/Web Scraping/NASA-Mars-Mission-Analysis/')
app.config["DEBUG"] = True

#Define Path for App Home Screen
@app.route('/', methods=['GET'])

#Define Function for Home Screen Content
def home():

    #Launch NASA Mars Mission Analysis Web Page
    scraped_data = {'mars_news': {'title': "NASA's Briefcase-Size MarCO Satellite Picks Up Honors",
  'description': 'The twin spacecraft, the first of their kind to fly into deep space, earn a Laureate from Aviation Week & Space Technology.'},
 'mars_image': 'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA17470_ip.jpg',
 'mars_weather': 'InSight sol 355 (2019-11-25), low -99.6ºC (-147.4ºF), high -23.2ºC (-9.7ºF), winds from the SSE at 5.4 m/s (12.2 mph), gusting to 19.8 m/s (44.2 mph), pressure at 6.70 hPa',
 'mars_facts': '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th></th>\n    </tr>\n    <tr>\n      <th>Mars Facts</th>\n      <th></th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>Equatorial Diameter:</th>\n      <td>6,792 km</td>\n    </tr>\n    <tr>\n      <th>Polar Diameter:</th>\n      <td>6,752 km</td>\n    </tr>\n    <tr>\n      <th>Mass:</th>\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n    </tr>\n    <tr>\n      <th>Moons:</th>\n      <td>2 (Phobos &amp; Deimos)</td>\n    </tr>\n    <tr>\n      <th>Orbit Distance:</th>\n      <td>227,943,824 km (1.38 AU)</td>\n    </tr>\n    <tr>\n      <th>Orbit Period:</th>\n      <td>687 days (1.9 years)</td>\n    </tr>\n    <tr>\n      <th>Surface Temperature:</th>\n      <td>-87 to -5 °C</td>\n    </tr>\n    <tr>\n      <th>First Record:</th>\n      <td>2nd millennium BC</td>\n    </tr>\n    <tr>\n      <th>Recorded By:</th>\n      <td>Egyptian astronomers</td>\n    </tr>\n  </tbody>\n</table>'}

    return render_template('index.html', **scraped_data)

#Define Path for Scaping New Data & Updating Web Page
@app.route('/scrape', methods=['GET'])

#Define Function for Scaping New Data & Updating Web Page
def new_scrape():
    import mars_news_scraping as mns
    scraped_data = mns.scrape()

    return render_template('index.html', **scraped_data)

#Initialize Flask App
app.run()