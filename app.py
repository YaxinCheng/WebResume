import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
app = Flask(__name__, static_folder="static")
import pytz
from datetime import datetime
import requests
from loginForm import loginForm
import hashlib
from Manager import Manager
from random import randint

MONGO_URI = os.environ.get('MONGO_URL')
if not MONGO_URI:
  MONGO_URI = '***REMOVED***'

app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)
zone = pytz.timezone('America/Halifax')

app.config['GOOGLEMAPS_KEY'] = '***REMOVED***'
GoogleMaps(app)

app.secret_key = '***REMOVED***'
login_manager = LoginManager()
login_manager.init_app(app)

def getInfo(ip):
  url = 'http://ip-api.com/json/' + str(ip)
  info = requests.get(url).json()
  info.pop('as', None)
  info.pop('countryCode', None)
  info.pop('isp', None)
  info.pop('region', None)
  info.pop('status', None)
  return info

def getIP():
  return request.access_route[-1] if len(request.access_route) > 1 else request.access_route[0]

def keepRecordInDB(field):
  ip = getIP()
  if not ip == "127.0.0.1":
    time = datetime.now(zone).strftime('%Y-%m-%d %H:%M:%S')
    ipInfo = getInfo(ip)
    ipInfo['last visit'] = time
    mongo.db.statistics.update({'_id': field}, {'$set': ipInfo, '$inc': {'count': 1}})
    documentsList = {'overview': mongo.db.overview, 'education': mongo.db.education, 'projects': mongo.db.projects, 'experience': mongo.db.experience, 'contact': mongo.db.contact}
    document = documentsList[field]
    if document.find({'_id': ip}).count() > 0:
      document.update({'_id': ip}, {'$set': {'last visit': time}})
    else:
      ipInfo.pop('query', None)
      ipInfo['_id'] = ip
      document.insert(ipInfo)

@app.route('/')
@app.route('/Overview')
@app.route('/overview')
def index():
    keepRecordInDB('overview')
    info = mongo.db.overviewData.find({}).sort([("order", 1)])
    return render_template('overview.html', Subject="overview",  Information=info)


@app.route('/Education')
@app.route('/education')
def education():
    keepRecordInDB('education')
    info = mongo.db.educationData.find({}).sort([("order", 1)])
    return render_template('overview.html', Subject="education", Information=info)


@app.route('/Projects')
@app.route('/projects')
def projects():
    keepRecordInDB('projects')
    info = mongo.db.projectsData.find({}).sort([("order", -1)])
    return render_template('overview.html', Subject="projects", Information=info)


@app.route('/Experience')
@app.route('/experience')
def experience():
    keepRecordInDB('experience')
    info = mongo.db.experienceData.find({}).sort([("order", -1)])
    return render_template('overview.html', Subject="experience", Information=info)


@app.route('/Contact')
@app.route('/contact')
def contact():
    keepRecordInDB('contact')
    info = mongo.db.contactData.find({})
    return render_template('overview.html', Subject="contact", Information=info)

@app.route('/entry', methods = ['GET', 'POST'])
def entry():
    answer = None
    form = loginForm()
    label = 'You are gonna enter the core of universe'
    count = mongo.db.secret.find().count()
    # questionSel = randint(0, count - 1)
    questionSel = 0
    question = mongo.db.secret.find({'_id': questionSel})[0]
    if request.method == 'POST':
        answer = form.dumbQuestion.data
        sha256Hash = hashlib.sha256()
        sha256Hash.update((answer + 'ycheng').encode('utf-8'))
        hashed = sha256Hash.hexdigest()
        print(hashed)
        print(question['answer'])
        if hashed != question['answer']:
            label = 'You are expelled from the universe!'
        else:
            user = Manager.get('')
            login_user(user, remember = True)
            return redirect(url_for('visitors'))
    return render_template('form.html', form = form, question = question, label = label)

@login_manager.user_loader
def load_user(user_id):
    return Manager.get(user_id)

@app.route('/visitors')
@login_required
def visitors():
    mapInfo = {'Type': 2}
    coordinates = set()
    visitorData = [mongo.db.overview.find({}), mongo.db.projects.find({}), mongo.db.education.find({}), mongo.db.experience.find({}), mongo.db.contact.find({})]
    for eachData in visitorData:
        for eachVisitor in eachData:
            coordinates.add((eachVisitor['lat'], eachVisitor['lon'], eachVisitor['regionName'] + ', ' + eachVisitor['country']))
    visitorMap = Map(identifier = 'visitors', lat = 48.1548256, lng = 11.4017529, markers = list(coordinates), zoom = 2, maptype = 'SATELLITE', style = 'height:700px;margin:0;', fullscreen_control = False)
    mapInfo['map'] = visitorMap
    statInfo = {'Type': 3, 'Title': 'Statistics'}
    statistics = mongo.db.statistics.find({})
    data = list()
    for each in statistics:
      formatted = dict()
      formatted['subTitle'] = each['_id']
      formatted['subDescription'] = 'Visitor count: {}<br>Last visitor: {}<br>{}, {}<br>{}'.format(str(each['count']), each['last visit'], each['country'], each['regionName'], each['org'])
      data.append(formatted)
    statInfo['data'] = data
    return render_template('overview.html', Subject='visitor', Information=[statInfo, mapInfo])

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
