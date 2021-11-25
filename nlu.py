#!/usr/bin/python3
# -*- coding: utf8 -*-

import sys 
try:
    reload         # Python 2
    reload(sys)
    sys.setdefaultencoding('utf8')
except NameError:  # Python 3
    from importlib import reload

import configparser
import urllib    
import uuid
import json
import requests


query = sys.argv[1]
lang = 'zh-tw'
session_id = str( uuid.uuid1() )
timezone = 'Asia/Taipei'

config = configparser.ConfigParser()
config.read('smart_speaker.conf')
project_id = config.get('dialogflow', 'project_id')
authorization = config.get('dialogflow', 'authorization')

headers = {
    "accept": "application/json",
    "authorization": authorization
}
url = 'https://dialogflow.googleapis.com/v2/projects/' + project_id +'/agent/sessions/' + session_id + ':detectIntent'
payload = {"queryInput":{"text":
{"text":query,"languageCode":lang}},"queryParams":{"timeZone":timezone}}
response = requests.post(url, data=json.dumps(payload), headers=headers)

data = json.loads(response.text)

#print(data)
queryText = data['queryResult']['queryText']
fulfillment = data['queryResult']['fulfillmentText']
confidence = data['queryResult']['intentDetectionConfidence']
#print("Query: {}".format(queryText))
print("{}".format(fulfillment))
#print("Confidence: {}".format(confidence))
