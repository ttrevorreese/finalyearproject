from array import array
import pandas as pd
import time
import math

# Import data from csv
#data = pd.read_csv('/content/drive/MyDrive/! University of Roehampton/Year 3/! Final Year Project/Datasets/BusStops_v1 - Sheet1.csv')
data = pd.read_csv('https://github.com/ttrevorreese/finalyearproject/blob/3957f1e49997329f2fddccb63c926d7f3778678b/Datasets/BusStops')

# Drop unnecessary columns (can be utilized in further development)
data.drop(['Scores', 'Notes'], axis=1, inplace=True)

# Display a preview of the first 10 rows of the data
data.head(10)

# Storing latitude and longitude into a list each
lat = data["Latitude"]
lon = data["Longitude"]
name = data["Stop Name"]
clsf = data["Classification"]