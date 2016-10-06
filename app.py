import os
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
app = Flask(__name__, static_folder="static")
import pytz
from datetime import datetime
import requests

MONGO_URI = os.environ.get('MONGO_URL')
if not MONGO_URI:
  MONGO_URI = '***REMOVED***'

app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)
zone = pytz.timezone('America/Halifax')

def getInfo(ip):
  url = 'http://ip-api.com/json/' + str(ip)
  info = requests.get(url).json()
  info.pop('as', None)
  info.pop('countryCode', None)
  info.pop('isp', None)
  info.pop('region', None)
  info.pop('status', None)
  return info

@app.route('/')
@app.route('/Overview')
@app.route('/overview')
def index():
    ip = request.access_route[-1] if len(request.access_route) > 1 else request.access_route[0]
    if not ip == "127.0.0.1":
      time = datetime.now(zone).strftime('%Y-%m-%d %H:%M:%S')
      ipInfo = getInfo(ip)
      ipInfo['last visit'] = time
      mongo.db.statistics.update({'_id': 'overview'}, {'$set': ipInfo, '$inc': {'count': 1}})
      if mongo.db.overview.find({'_id': ip}).count() > 0:
        mongo.db.overview.update({'_id': ip}, {'$set': {'last visit': time}})
      else:
        ipInfo.pop('query', None)
        ipInfo['_id'] = ip
        mongo.db.overview.insert(ipInfo)
    info = mongo.db.overviewData.find({}).sort([("order", 1)])
    return render_template('overview.html', Subject="overview",  Information=info)


@app.route('/Education')
@app.route('/education')
def education():
    ip = request.access_route[-1] if len(request.access_route) > 1 else request.access_route[0]
    if not ip == "127.0.0.1":
      time = datetime.now(zone).strftime('%Y-%m-%d %H:%M:%S')
      ipInfo = getInfo(ip)
      ipInfo['last visit'] = time
      mongo.db.statistics.update({'_id': 'education'}, {'$set': ipInfo, '$inc': {'count': 1}})
      if mongo.db.education.find({'_id': ip}).count() > 0:
        mongo.db.education.update({'_id': ip}, {'$set': {'last visit': time}})
      else:
        ipInfo.pop('query', None)
        ipInfo['_id'] = ip
        mongo.db.education.insert(ipInfo)
    info = mongo.db.educationData.find({}).sort([("order", 1)])
    return render_template('overview.html', Subject="education", Information=info)


@app.route('/Projects')
@app.route('/projects')
def projects():
    ip = request.access_route[-1] if len(request.access_route) > 1 else request.access_route[0]
    if not ip == "127.0.0.1":
      time = datetime.now(zone).strftime('%Y-%m-%d %H:%M:%S')
      ipInfo = getInfo(ip)
      ipInfo['last visit'] = time
      mongo.db.statistics.update({'_id': 'projects'}, {'$set': ipInfo, '$inc': {'count': 1}})
      if mongo.db.projects.find({'_id': ip}).count() > 0:
        mongo.db.projects.update({'_id': ip}, {'$set': {'last visit': time}})
      else:
        ipInfo.pop('query', None)
        ipInfo['_id'] = ip
        mongo.db.projects.insert(ipInfo)
    info = mongo.db.projectsData.find({}).sort([("order", -1)])
    return render_template('overview.html', Subject="projects", Information=info)


@app.route('/Experience')
@app.route('/experience')
def experience():
    ip = request.access_route[-1] if len(request.access_route) > 1 else request.access_route[0]
    if not ip == "127.0.0.1":
      time = datetime.now(zone).strftime('%Y-%m-%d %H:%M:%S')
      ipInfo = getInfo(ip)
      ipInfo['last visit'] = time
      mongo.db.statistics.update({'_id': 'experience'}, {'$set': ipInfo, '$inc': {'count': 1}})
      if mongo.db.experience.find({'_id': ip}).count() > 0:
        mongo.db.experience.update({'_id': ip}, {'$set': {'last visit': time}})
      else:
        ipInfo.pop('query', None)
        ipInfo['_id'] = ip
        mongo.db.experience.insert(ipInfo)
    info = mongo.db.experienceData.find({}).sort([("order", -1)])
    return render_template('overview.html', Subject="experience", Information=info)


@app.route('/Contact')
@app.route('/contact')
def contact():
    ip = request.access_route[-1] if len(request.access_route) > 1 else request.access_route[0]
    if not ip == "127.0.0.1":
      time = datetime.now(zone).strftime('%Y-%m-%d %H:%M:%S')
      ipInfo = getInfo(ip)
      ipInfo['last visit'] = time
      mongo.db.statistics.update({'_id': 'contact'}, {'$set': ipInfo, '$inc': {'count': 1}})
      if mongo.db.contact.find({'_id': ip}).count() > 0:
        mongo.db.contact.update({'_id': ip}, {'$set': {'last visit': time}})
      else:
        ipInfo.pop('query', None)
        ipInfo['_id'] = ip
        mongo.db.contact.insert(ipInfo)
    info = mongo.db.contactData.find({})
    return render_template('overview.html', Subject="contact", Information=info)

@app.route('/keepAlive')
def alive():
  INFO = {"Type": 0, 'Title': 'Keep Going', 'Description': '''Can't believe that you found this page?! You must be my crazy fan!<br>
  Actually this page is to keep the website awake due to the sleep mode of heroku. So there you go.<br>
  Email me from the right bottom corner if you have something to talk. Have a nice day''', 'Image': False}
  return render_template('overview.html', Subject="contact", Information=[INFO])

@app.errorhandler(404)
def page_not_found(e):
    Error = {"Type": 1, "Title": "404 Page Not Found", "images": ["images/4.png","images/0.png","images/4.png"], "subDescription":
            ["Page", "Not", "Found"], "subTitle": ["","",""],
            "buttonLink": ["","",""],"buttonTitle": ["","",""]}
    return render_template('overview.html', Information = [Error]), 404

@app.errorhandler(500)
def internal_server_error(e):
    Error = {"Type": 1, "Title": "500 Internal Server Error", "images": ["images/5.png","images/0.png","images/0.png"], "subDescription":
            ["Internal", "Server", "Error"],"subTitle": ["","",""],
            "buttonLink": ["","",""],"buttonTitle": ["","",""]}
    return render_template('overview.html', Information = [Error]), 500

if __name__ == "__main__":
    app.run()
