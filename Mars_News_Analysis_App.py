#Import Modules
import flask
from flask import request, jsonify, render_template
import numpy as np
import pandas as pd

#Define Flask App Environment
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Define Path for App Home Screen
@app.route('/', methods=['GET'])

#Define Function for Home Screen Content
def home():

    #Launch NASA Mars Mission Analysis Web Page
    scraped_data = {'mars_news': {'title': 'Global Storms on Mars Launch Dust Towers Into the Sky',
                    'description': 'A Mars Dust Tower Stands Out Dust storms are common on Mars. But every decade or so, something unpredictable happens: a series of runaway storms break out, covering the entire planet in a dusty haze.'},
                    'mars_image': 'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA17793_ip.jpg',
                    'mars_weather': 'InSight sol 355 (2019-11-25), low -99.6ºC (-147.4ºF), high -23.2ºC (-9.7ºF), winds from the SSE at 5.4 m/s (12.2 mph), gusting to 19.8 m/s (44.2 mph), pressure at 6.70 hPa',
                    'mars_facts': '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th></th>\n    </tr>\n    <tr>\n      <th>Mars Facts</th>\n      <th></th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>Equatorial Diameter:</th>\n      <td>6,792 km</td>\n    </tr>\n    <tr>\n      <th>Polar Diameter:</th>\n      <td>6,752 km</td>\n    </tr>\n    <tr>\n      <th>Mass:</th>\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n    </tr>\n    <tr>\n      <th>Moons:</th>\n      <td>2 (Phobos &amp; Deimos)</td>\n    </tr>\n    <tr>\n      <th>Orbit Distance:</th>\n      <td>227,943,824 km (1.38 AU)</td>\n    </tr>\n    <tr>\n      <th>Orbit Period:</th>\n      <td>687 days (1.9 years)</td>\n    </tr>\n    <tr>\n      <th>Surface Temperature:</th>\n      <td>-87 to -5 °C</td>\n    </tr>\n    <tr>\n      <th>First Record:</th>\n      <td>2nd millennium BC</td>\n    </tr>\n    <tr>\n      <th>Recorded By:</th>\n      <td>Egyptian astronomers</td>\n    </tr>\n  </tbody>\n</table>'}
    return render_template('index.html', **scraped_data)

# #Define Path for Precipitation Information Static API
# @app.route('/api/v1.0/precipitation', methods=['GET'])

# #Define Function for Precipitation Information Static API Content
# def api_precip():

#     #Extract All Avialable Dates from Measurements Table
#     date_list = engine.execute('SELECT date FROM Measurement')

#     #Loop Thruough Dates to Find Latest Record
#     for date in date_list:
#         last_date = date[0]
    
#     #Split Lastest Date Record at Dashes to Isolate Year/Month/Day
#     date_split = last_date.split('-')

#     #Subtract One from Year Index
#     date_split[0] = str(int(date_split[0]) - 1)

#     #Re-Assemble Date Value & Record as Year Prior Date
#     prior_date = date_split[0] + '-' + date_split[1] + '-' + date_split[2]

#     #Query Database to Create Pandas Data Frame of Precipitation Data for Selected Year-Long Period
#     precip_data = pd.read_sql('SELECT date, prcp FROM Measurement WHERE date >= (?)', engine, params = (prior_date,))

#     #Drop Rows with Missing Values
#     precip_data = precip_data.dropna()

#     #Set Date Values as Data Frame Index
#     precip_data = precip_data.set_index('date')

#     #Sort Data Frame by Date
#     precip_data = precip_data.sort_index()

#     #Convert Data Frame to Dictionary
#     precip_dict = {date_name: date_group['prcp'].tolist() for date_name, date_group in precip_data.groupby('date')}

#     #Display Precipitation Information
#     return jsonify(precip_dict)

# #Define Path for Station Information Static API
# @app.route('/api/v1.0/stations', methods=['GET'])

# #Define Function for Station Information Static API Content
# def api_stations():
    
#     #Extract All Station IDs and Names from Stations Table
#     active_stations = engine.execute('SELECT station, name FROM Station')

#     #Define Blank Dictionary for Station IDs and Names
#     station_list = {}

#     #Loop Through Station ID & Name Pairs
#     for occurences in active_stations:

#         #Create Dictionary of Station IDs & Names
#         station_list.update({occurences[0]: occurences[1]})

#     #Display Station Information
#     return jsonify(station_list)

# #Define Path for Temperature Information Static API
# @app.route('/api/v1.0/tobs', methods=['GET'])

# #Define Function for Temperature Information Static API Content
# def api_temp():

#     #Extract All Avialable Dates from Measurements Table
#     date_list = engine.execute('SELECT date FROM Measurement')

#     #Loop Thruough Dates to Find Latest Record
#     for date in date_list:
#         last_date = date[0]
    
#     #Split Lastest Date Record at Dashes to Isolate Year/Month/Day
#     date_split = last_date.split('-')

#     #Subtract One from Year Index
#     date_split[0] = str(int(date_split[0]) - 1)

#     #Re-Assemble Date Value & Record as Year Prior Date
#     prior_date = date_split[0] + '-' + date_split[1] + '-' + date_split[2]

#     #Query Database to Create Pandas Data Frame of Temperature Data for Selected Year-Long Period for Most Active Weather Station
#     temp_data = pd.read_sql('SELECT date, tobs FROM Measurement WHERE date >= (?) AND station = (?)', engine, params = (prior_date, 'USC00519281',))

#     #Drop Rows with Missing Values
#     temp_data = temp_data.dropna()

#     #Set Date Values as Data Frame Index
#     temp_data = temp_data.set_index('date')

#     #Sort Data Frame by Date
#     temp_data = temp_data.sort_index()

#     #Convert Data Frame to Dictionary
#     temp_dict = {date_name: date_group['tobs'].tolist() for date_name, date_group in temp_data.groupby('date')}

#     #Display Temperature Information
#     return jsonify(temp_dict)

# #Define Path for Temperature Information Dynamic API with Start Date
# @app.route('/api/v1.0/<start>', methods=['GET'])

# #Define Function for Temperature Information Dynamic API with Start Date
# def api_start(start):

#     #Query Database to Create Pandas Data Frame of Temperature Data for Selected Year-Long Period for Most Active Weather Station
#     temp_data = pd.read_sql('SELECT date, tobs FROM Measurement WHERE date >= (?)', engine, params = (start,))

#     #Drop Rows with Missing Values
#     temp_data = temp_data.dropna()

#     #Set Date Values as Data Frame Index
#     temp_data = temp_data.set_index('date')

#     #Sort Data Frame by Date
#     temp_data = temp_data.sort_index()

#     #Convert Data Frame to Dictionary
#     temp_dict = {date_name: date_group['tobs'].tolist() for date_name, date_group in temp_data.groupby('date')}

#     #Define Blank Dictionary for Temperature Summary Data
#     summary_dict = {}
    
#     #Loop Through Daily Temperature Data
#     for index in temp_dict:

#         #Calculate Daily Minimum/Maximum/Average Temperatures
#         summary_dict.update({index: [min(temp_dict[index]), max(temp_dict[index]), round(mean(temp_dict[index]),1)]})

#     #Display Temperature Information
#     return jsonify(summary_dict)

# #Define Path for Temperature Information Dynamic API with Start & End Dates
# @app.route('/api/v1.0/<start>/<end>', methods=['GET'])

# #Define Function for Temperature Information Dynamic API with Start & End Date
# def api_end(start, end):
#     #Query Database to Create Pandas Data Frame of Temperature Data for Selected Year-Long Period for Most Active Weather Station
#     temp_data = pd.read_sql('SELECT date, tobs FROM Measurement WHERE date >= (?) AND date <= (?)', engine, params = (start, end,))

#     #Drop Rows with Missing Values
#     temp_data = temp_data.dropna()

#     #Set Date Values as Data Frame Index
#     temp_data = temp_data.set_index('date')

#     #Sort Data Frame by Date
#     temp_data = temp_data.sort_index()

#     #Convert Data Frame to Dictionary
#     temp_dict = {date_name: date_group['tobs'].tolist() for date_name, date_group in temp_data.groupby('date')}

#     #Define Blank Dictionary for Temperature Summary Data
#     summary_dict = {}
    
#     #Loop Through Daily Temperature Data
#     for index in temp_dict:

#         #Calculate Daily Minimum/Maximum/Average Temperatures
#         summary_dict.update({index: [min(temp_dict[index]), max(temp_dict[index]), round(mean(temp_dict[index]),1)]})

#     #Display Temperature Data
#     return jsonify(summary_dict)

#Initialize Flask App
app.run()