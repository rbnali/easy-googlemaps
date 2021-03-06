# easy-googlemaps

An easy to use Python script to get latitude and longitude coordinates from a CSV file with addresses using Google Maps API.

# Requirements

You need your own Google Maps API Key.

You can install all the necesssary packages that way:

```
pip install -r requirements.txt
```

# Arguments

Arguments       | Help
-------------   | -------------
-f              | Path to your CSV file with ; delimiters
-c              | List of column elements to build the address. Ideally in the following order: street, zip, city, country.
-api            | Your GOOGLE MAPS API KEY
-o              | Name of the CSV file in output

# Example

```
python get_latlng.py -f get_latlng_example.csv -c 'Street name' -c zip -c city -c country -api YOUR_GOOGLE_MAPS_API -o get_latlng_output.csv
```
