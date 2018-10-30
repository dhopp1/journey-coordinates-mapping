import pandas as pd
from geopy.geocoders import Nominatim
geolocator = Nominatim()
#Use rate limiter library for error catching and automatic throttling to avoid excessive API calls
from geopy.extra.rate_limiter import RateLimiter
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

#**Directory of CSV with addresses, output of CSV with coordinates, and file name of CSV**
#CSV should have column names: "id", "from_street", "from_city", "from_zip", "from_country", "to_street", "to_city", "to_zip, "to_country"
#"id" and "to" suffixed columns can be empty as well as "street" columns
directory = 'C:\\Users\\pamono-user\\Desktop\\BI\\1. Reports - Ad-Hoc\\2017-11-29 Intra-Inter Transactions Map\\2018-10-29 Update\\'
file_name = 'Addresses Template.csv'

#**State if getting coordinates for journeys (True), or just points (False)**
journeys = True

#Put addresses in dataframe
data = pd.read_csv(directory + file_name, encoding='latin-1')

#Replace nulls with blank
for i in range(0, len(list(data))):
    column = list(data)[i]
    data.ix[data[column].isnull(),column] = ''

#Split journeys into "from" and "to"
froms = data.ix[:,['from_street', 'from_city', 'from_zip', 'from_country']]
if journeys:
    tos = data.ix[:,['to_street', 'to_city', 'to_zip', 'to_country']]

#Adding columns for latitude and longitude, initializing with 0 to know when getting coordinates has failed
froms['lat'] = 0
froms['long'] = 0
if journeys:
    tos['lat'] = 0
    tos['long'] = 0

#Loop to get coordinates of addresses, loop instead of apply so that execution can be stopped/break part way through without loss of coordinates already acquired
for i in range(0,len(froms)):
    
    #Convert addresses to strings from dataframe columns
    from_address = str(froms.ix[i,'from_street']) + ' ' + str(froms.ix[i,'from_city']) + ' ' + str(froms.ix[i,'from_zip']) + ' ' + str(froms.ix[i,'from_country'])
    if journeys:
        to_address = str(tos.ix[i,'to_street']) + ' ' + str(tos.ix[i,'to_city']) + ' ' + str(tos.ix[i,'to_zip'])+' ' + str(tos.ix[i,'to_country'])
    
    #Call geocode function, which incorporates geolocator from geopy and ratelimiter
    from_location = geocode(from_address)
    if journeys:
        to_location = geocode(to_address)
    
    #Put lats and longs into columns from geocode location object, with error catching (may be redundant with geocode function of ratelimiter)
    try:     
        froms.ix[i,'lat'] = from_location.latitude
    except Exception:
        pass
    try:    
        froms.ix[i,'long'] = from_location.longitude
    except Exception:
        pass
    if journeys:    
        try:    
            tos.ix[i,'lat'] = to_location.latitude
        except Exception:
            pass
        try:    
            tos.ix[i,'long'] = to_location.longitude
        except Exception:
            pass
        
    #Print progress for monitoring of large files
    print(str(i) + '/' + str(len(froms)))

#Create final output dataframe
data['from_lat'] = froms.lat
data['from_long'] = froms.long
if journeys:
    data['to_lat'] = tos.lat
    data['to_long'] = tos.long

#Write output CSV to directory, a "0" coordinate means the address was not found
data.to_csv(directory + 'Coordinates Output.csv', index=False)
