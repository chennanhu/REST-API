from flask import Flask, render_template
from flask import request
from flask import json
import requests
import os
import boto3 
import time
import datetime




app = Flask(__name__)

@app.route('/get_events',methods = ['POST'])
def get_events():
	ts=time.time()
	date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	print (request.is_json)
	content = request.get_json()
	print (content)
	for i in range(len(content)):
		start_date_time = content[i]['start_date_time']
		end_date_time = content[i]['end_date_time']
		city = content[i]['city']
		postal_code = content[i]['postal_code']
		ticket_master_api_key = content[i]['ticket_master_api_key']
		paramater_URL='https://app.ticketmaster.com/discovery/v2/events.json?start_date_time=%s&end_date_time=%s&city=%s&postal_code=%s&apikey=%s' %(start_date_time,end_date_time,city,postal_code,ticket_master_api_key) 
		events=requests.get(paramater_URL)
		s3 = boto3.resource('s3')
		s3.Bucket('goleftsherry').put_object(Key='%s/events%s.json'%(date,i) , Body=events.content)
		time.sleep(0.2)

	return '<h1>File saved to S3</h1>'

	
	


if __name__ == '__main__':
	app.run(debug=True)

