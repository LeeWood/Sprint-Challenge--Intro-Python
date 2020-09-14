# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
    def __str__(self):
        return f'{self.name}, {self.lat}, {self.lon}' 


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

# with open(r'C:\Users\Aleesha\LAMBDA_PROJECTS\SPRINTS\Sprint-Challenge--Intro-Python\src\cityreader\cities.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader: 
#         print(row)

cities = []

def cityreader(cities=[]):
    import csv

    with open(r'C:\Users\Aleesha\LAMBDA_PROJECTS\SPRINTS\Sprint-Challenge--Intro-Python\src\cityreader\cities.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader, None)
        
        for row in reader:
            #print(City(row[0], row[3], row[4]))
            cities.append(City(row[0], float(row[3]), float(row[4])))

  # Ensure that the lat and lon values are all floats
  # For each city record, create a new City instance and add it to the 
  # `cities` list
    
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
# for c in cities:
#     print(c)


# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user
#* If city lat and lon falls in lat1 and lon1...include in within.
# * also if city lat and lon falls in lat2 and lon2...include in within 

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=cities):
  within = []

  lats = [lat1, lat2]
  lons = [lon1, lon2]
  
  for c in cities:
      if min(lats) <= c.lat <= max(lats) and min(lons) <= c.lon <= max(lons):
          within.append(c)
          print(c.name, c.lat, c.lon)

  return within

#cityreader_stretch(45, -100, 32, -120)  

def cityreader_stretch_pt2(cities=cities):
  within = []

  lat1 = float(input("Frist Latitude: "))
  lon1 = float(input("First Longitude: "))
  lat2 = float(input("Second Latitude: "))
  lon2 = float(input("Second Longitude: "))


  lats = [lat1, lat2]
  lons = [lon1, lon2]
  
  for c in cities:
      if min(lats) <= c.lat <= max(lats) and min(lons) <= c.lon <= max(lons):
          within.append(c)
          print(c.name, c.lat, c.lon)

  return within

#cityreader_stretch_pt2()

