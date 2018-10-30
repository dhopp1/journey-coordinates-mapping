# journey_coordinates_mapping
Simple scripts to get latitudinal and longitudinal coordinates of addresses from a CSV file, and visualize those journeys on a map.

## The project provides two useful actions:
1. Easily getting the coordinates (latitude and longitude) of addresses in a CSV.  Either the two ends of a journey or of single addresses.  A template CSV is in the repository.
2. Mapping the journeys of point to point pairs on a customizable google map.

## Getting Coordinates
The get_coordinates.py script takes the addresses from a CSV in the format of:
"id", "from_street", "from_city", "from_zip", "from_country", "to_street", "to_city", "to_zip, "to_country".
<br><br>
Both the "id" and "to" suffixed columns can be left blank, in which case coordinates will be found only for the "from" suffixed addresses. Andy "state" aspects of addresses should be concatenated after the "city" fields.  The output is a new CSV with the same colums but suffixed with "from_lat", "from_long", "to_lat", "to_long".
<br><br>
Any comments in code surrounded by "\*\*" is where the user should change parameters, directory, preferences, etc.

## Mapping Journey
The map.py script takes the CSV output of the first script and maps the journeys to an HTML file. Customization for the journey lines takes place within the script, while customization of the map itself takes place directly in the HTML output file.
<br><br>
More resources on customization of the map can be found at: https://developers.google.com/maps/documentation/javascript/styling#creating_a_styledmaptype
