#!/usr/bin/python

import requests
import socket
import sys
import urllib
import json

#if len(sys.argv) != 2:
#	print "Usage: sploitus.py <service>" + " \r\n"
#	print "Example: python sploitus.py smb 4.6" + " \r\n"
#	sys.exit(0)

#input = sys.argv[1]

def fetch_exloits():
	#s = requests.Session()
#	session.post("https://sploitus.com/search". data=dict(
#		type="exploits",
#		sort="default",
#		query="smb",
#		title:"false",
#		offset=0
#	))

	#Send a get request, this is necessary to get a session cookie so we can do a POST for the actual search
	#Update this to take an argv that is encoded with urllib!!!!!!!!
	r = requests.get("https://sploitus.com/?query=" + "smb", allow_redirects=True, timeout=3)

	if r.status_code == 200:
		print r.url + "\r\n"
		
		#Get the set cookie header from the response
		try:
			getcookie = r.headers['Set-Cookie'].split(' ')[0]
		except:
			print "Could not get cookie from header. We can run a POST request without this cookie"

		#Remove the semicolon from the end of the cookie that was returned
		try:
			cookie = getcookie.replace(";", "")
		except: 
			print "Either the cookie changed since this script was created or something else isn't working right"
		#try: 
			#Trying the request again with our new cookie?
			#headers = {"Cookie": cookie}
			#r = requests.get(url, headers=headers)
			#print r.text
		#except:
			#print "The Second request is busted.."

		#Debug Line.. remove
		#print cookie
		url = "https://sploitus.com/search"
		headers = {"Accept": "application/json","content-type": "application/json","Host": "sploitus.com"}
		body = {"type":"exploits","sort":"default","query":"smb","title":"true","offset":0}
		r = requests.post(url, data=json.dumps(body), headers=headers)
		canihazexploits = r.json()
		
		for exploit in canihazexploits["exploits"]:
			exploitscore = exploit['score']
			print "SCORE: " + str(exploitscore)
			print exploit['title']
			print "More info: " + exploit['href']
			print "================================="
			print "\r\n"


		#Send a post request to the search page
		#r = requests.post("https://sploitus.com/search")

    		sys.exit(0)

	else:
		#Upgrade this to pull the response code and display to user
    		print "HTTP response code was not 200. Check your connection"

fetch_exloits()
