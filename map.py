import pandas as pd
import pyperclip

#**Directory of CSV file from get_coordinates.py output**
directory = 'C:\\Users\\'

#Read the CSV to a dataframe
data = pd.read_csv(directory + 'Coordinates Output.csv', encoding='latin-1')

#Remove addresses missing coordinates
data = data.ix[((data['from_lat'] != 0) & (data['from_long'] != 0) & (data['to_lat'] != 0) & (data['to_long'] != 0)),:]
data = data.reset_index(inplace=False, drop=True)

#Initialize empty code string
code = ""

#Loop through coordinates and create string containing information for each journey
for i in range(0,len(data)):
    lat1 = str(data.ix[i,'from_lat'])
    long1 = str(data.ix[i,'from_long'])
    lat2 = str(data.ix[i,'to_lat'])
    long2 = str(data.ix[i,'to_long'])
    
    code += "var flightPlanCoordinates" + str(i) + " = [{lat:" + lat1 + ", lng:" + long1 + "}, {lat: " + lat2 + ", lng:" + long2 + "}]; var flightPath" + str(i) + " = new google.maps.Polyline({path: flightPlanCoordinates" + str(i) + ",geodesic: true,strokeColor: '#ff6400',strokeOpacity: 1.0, strokeWeight: .25}); flightPath" + str(i) + ".setMap(map);"
    
#Copy the string to the clipboard, paste between quotations marks below line commented "Paste code from "map.py" here, between quotation marks" in Map.html file
pyperclip.copy(code)
