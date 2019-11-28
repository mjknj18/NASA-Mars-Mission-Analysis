#Import Modules
import flask
from flask import request, jsonify, render_template
import numpy as np
import pandas as pd
import pymongo

#Define Flask App Environment
app = flask.Flask(__name__, template_folder = 'C:/Users/mjknj/Desktop/UNCC/Homework/Web Scraping/NASA-Mars-Mission-Analysis/')
app.config["DEBUG"] = True

#Connect to MongoDB Database
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client['mars_db']
mongo_col = mongo_db['latest_info']

#Define Path for App Home Screen
@app.route('/', methods=['GET'])

#Define Function for Home Screen Content
def home():

    #Launch NASA Mars Mission Analysis Web Page
    for item in mongo_col.find():
        scraped_data = item

    return render_template('index.html', **scraped_data)

#Define Path for Scaping New Data & Updating Web Page
@app.route('/scrape', methods=['GET'])

#Define Function for Scaping New Data & Updating Web Page
def new_scrape():
    import mars_news_scraping as mns
    scraped_data = mns.scrape()

    mongo_col.insert_one(scraped_data)

    return render_template('index.html', **scraped_data)

#Initialize Flask App
app.run()