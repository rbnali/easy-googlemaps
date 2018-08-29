# easy-googlemaps

An easy to use Python script to get latitude and longitude coordinates from addresses using Google Maps API.

# Requirements

You need your own Google Maps API Key.

You can install all the necesssary packages that way:

```
pip install -r requirements.txt
```

# Arguments

Argument        | Help
-------------   | -------------
-f FILE         | Path to your CSV file with ; delimiters
-c ADDRESS_COL  | List of column elements to build the address. Ideally in the following order: street, zip, city, country.
-api API_KEY    | Your GOOGLE MAPS API KEY
-o OUTPUT       | Name of the CSV file in output

# Example

```
python get_latlng.py -f get_latlng_example.csv -c 'Street name' -c zip -c city -c country -api YOUR_GOOGLE_MAPS_API -o get_latlng_output.csv
```
