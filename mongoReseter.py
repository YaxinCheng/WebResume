#!/Users/Cheng/Developer/Python/Resume/venv/bin/python
from pymongo import MongoClient

client = MongoClient('***REMOVED***')
print('DB is connected...')
input('You sure wanna clean the data ... ?')
db = client.heroku_q92lvkqx
db.contact.remove({})
db.education.remove({})
db.experience.remove({})
db.overview.remove({})
db.projects.remove({})
db.statistics.remove({})

db.statistics.insert({'_id': 'overview', 'count': 0, 'last visit': None})
db.statistics.insert({'_id': 'education', 'count': 0, 'last visit': None})
db.statistics.insert({'_id': 'projects', 'count': 0, 'last visit': None})
db.statistics.insert({'_id': 'experience', 'count': 0, 'last visit': None})
db.statistics.insert({'_id': 'contact', 'count': 0, 'last visit': None})

print('DB is cleared...')
