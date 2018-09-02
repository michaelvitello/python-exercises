#!/usr/bin/env python3

# Write a small python server that displays the current temperature each time we refresh an html page.
# Step 1, create the server (this is from internet research, did not know how to do it)
# Step 2, get the temperature from external service (only requires GET methods)
# Step 3, update info at each page refresh

#### --- HOW TO RUN THE SERVER --- ####
## Start the server from terminal (python exercise-11.py). ##
## Open http://localhost:8000/ in your web-browser. ## (for now nothing gets displayed)

import SimpleHTTPServer
import SocketServer

import urllib2
import json

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()

# Getting data from the weather api (https://openweathermap.org/)
# I can't find a way to display this properly on the HTML page...

api_url = 'http://api.openweathermap.org/data/2.5/weather?q=Paris&appid=8814e4f54ba37a17a1b7330dba1167bf'

f = urllib2.urlopen(api_url)
json_string = f.read()
parsed_json = json.loads(json_string)

location = "Paris"
temp_f = parsed_json['main']['temp']
temp_c = (temp_f-32)*0.5556

print "Current temperature in %s is: %s Farenheit degrees, or %s Celsius degrees " % (location, temp_f, temp_c)

f.close()
