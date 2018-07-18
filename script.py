from flask import Flask, render_template
import requests
import json





headers = {'Content-type': 'application/json'}
url='http://127.0.0.1:5000/get_events'
contents = open('request.json', 'rb').read()
r = requests.post(url, data=contents, headers=headers)