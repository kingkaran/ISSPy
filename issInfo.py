#!/bin/pyhton3

import json
import turtle
import urllib.request
import time

urlPeople = 'http://api.open-notify.org/astros.json'
responsePeople = urllib.request.urlopen(urlPeople)
data = json.loads(responsePeople.read())

urlPosition = 'http://api.open-notify.org/iss-now.json'
responsePosition = urllib.request.urlopen(urlPosition)
coordinates = json.loads(responsePosition.read())

infoPeople = data['people']
numPeople = 0

for i in infoPeople:
    if i['craft'] == 'ISS':
        numPeople+=1
print('ISS REAL TIME INFO')
print('Number of astronauts on ISS: ', data['number'])
print()
print('Names: ')
for i in infoPeople:
    if i['craft'] == 'ISS':
        print(i['name'])

position = coordinates['iss_position']
latitude = position['latitude']
longitude = position['longitude']
print()
print('Latitude: ', latitude)
print('Longitude: ', longitude)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('world.gif')

screen.register_shape('satellite.gif')
satellite = turtle.Turtle()
satellite.shape('satellite.gif')
satellite.setheading(90)
satellite.penup()
satellite.setpos(float(longitude), float(latitude))

torLat = 43.6532
torLong = -79.3832
urlPass = 'http://api.open-notify.org/iss-pass.json?'
urlPass = urlPass + 'lat=' + str(torLat) + '&lon=' + str(torLong)
responsePass = urllib.request.urlopen(urlPass)
passing = json.loads(responsePass.read())

toronto = turtle.Turtle()
toronto.penup()
toronto.color('yellow')
toronto.setpos(torLong, torLat)
toronto.hideturtle()
toronto.dot(5)

nextPass = passing['response'][1]['risetime']
style = ('Calibri', 5)
toronto.write('Next pass over Toronto:\n'+time.ctime(nextPass)+" GMT", style)
