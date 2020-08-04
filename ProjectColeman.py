'''
Mia Coleman
July 26, 2020
CIS 245
Project Draft 1
'''

#import requests

def getData():
# Function to get user input. Verifies input from user.
	print("What's the weather like? ")
	zipString = input("Enter your zip code or 0 to exit: ")
	
	zip = int(zipString)

	if len(zipString) == 5:
		return zip
	elif zip == 0:
		exit()
	else:
		print("ERROR: INVALID ZIP CODE!")

# def getWeather(zip, ):
	# apiKey = ""
	# baseURL = "https://openweathermap.org/"
	# completeURL = baseURL + "appid=" + apiKey + "&" + 
	# JSON request
	# print("...requesting...")
	# try:
		# 
		# print("Connection successful!")
	# except:
		# print("Connection failed")


# def displayWeather():
	# Format and print weather data



zipCode = getData()

while zipCode != "0":
		# weatherData = getWeather(zipCode)
		# displayWeather(weatherData, zipCode)
	print(zipCode)
	getData()
		
