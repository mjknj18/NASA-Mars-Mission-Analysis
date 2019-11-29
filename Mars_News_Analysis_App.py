#Import Modules
import flask
from flask import request, jsonify, render_template, redirect, url_for
import numpy as np
import pandas as pd
import pymongo

#Define Flask App Environment
app = flask.Flask(__name__, template_folder = 'C:/Users/mjknj/Desktop/UNCC/Homework/Web Scraping/NASA-Mars-Mission-Analysis/')
app.config["DEBUG"] = False

#Connect to Mongo Database
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

#Define Mongo Database Parameters
mongo_db = mongo_client['mars_db']
mongo_col = mongo_db['latest_info']

#Define Path for App Home Screen
@app.route('/', methods=['GET'])

#Define Function for Home Screen Content
def home():

    #Extract Scraped Data from Mongo Database
    for item in mongo_col.find():
        scraped_data = item

    #Launch NASA Mars Mission Analysis Web Page
    return render_template('index.html', **scraped_data)

#Define Path for Scraping New Data & Updating Web Page
@app.route('/scrape', methods=['GET'])

#Define Function for Scraping New Data & Updating Web Page
def new_scrape():
    
    #Import Scraping Function
    import mars_news_scraping as mns

    #Run Scraping Function
    scraped_data = mns.scrape()

    #Insert Scraped Data into Mongo Database
    mongo_col.insert_one(scraped_data)

    #Reload App Home Screen
    return redirect(url_for('home'))

#Initialize Flask App
app.run()