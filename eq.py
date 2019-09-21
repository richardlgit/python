import requests
import json
import time
import re


lstQuakesInCA = []

#Using Requests module to grab the data
response = requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson')

# Using json, load the data into earthquake variable which produces dict. data object
earthquakes = json.loads(response.text)


numFeatures = len(earthquakes['features'])

#Each feature represents 1 earthquake - Prints total no. of earthquakes.
#print(numFeatures)

for j in range(0,numFeatures):

	# Grab the tite by travesring the earthquakes dict 
	title = earthquakes['features'][j]['properties']['title']
	
	#Split Title based on commma delimter
	lstsplitTitle = title.split(",")

	#Grab the state from the above list
	lststate = lstsplitTitle[-1]

	#print(state)
	if ('CA' in lststate or 'California' in lststate):
		#print(title)	
		
		#if the Stat is California then grab the Time the earthquake occured
		earthquakeEpocTime = earthquakes['features'][j]['properties']['time']
		

		# Replacing the '-' in title with # delimiter. This was done since some of the Magnitudes are in negative.
		title = re.sub(' - ', " # ", title)

		# Substiture 'CA' with 'California' as requested 
		title = re.sub(', CA', ", California", title)

		#print (title)
		
		#Create a new list by appending time and Title with '#' delimeter. 
		#Each item will be split and manipulated when we iterate over the list later 
		lstQuakesInCA.append(str(earthquakeEpocTime) + " # " +  title)


#Sort the list in ascending order to ensure our results are in printed in ascending order of time		
lstQuakesInCA.sort()

#print(lstQuakesInCA)

#Finnally iterate over the list of Earth Quakes
for quake in lstQuakesInCA:
	
	items = quake.split("#")
	earthquakeEpocTime = items[0]

	earthquakeDateTime = time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.localtime(float(earthquakeEpocTime)/1000))

	location = items[2]
	Mag = items[1]

	Mag = re.sub('M',"Magnitude:",Mag)

	# Finally ready to print out results in the required format
	print(earthquakeDateTime + '|' + location + '|' + Mag )




