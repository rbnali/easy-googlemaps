import pandas as pd
import googlemaps
import argparse
import os
from tqdm import tqdm

def append_address(row, address_list):
    full_address = []
    for address_element in address_list:
        full_address += [row[address_element]]
    return ' '.join(str(item) for item in full_address)

def gmaps_from_address(address, gmaps):
    gplaces = gmaps.geocode(address)
    result = ''
    
    for i in range(len(gplaces)):
        try:
            country = gplaces[i]['address_components'][-2]['short_name']  
            if country == 'FR':
                result = str(gplaces[i]['geometry']['location']['lat']) + ',' + str(gplaces[i]['geometry']['location']['lng'])
                break
        except:
            pass

    return result

def seperate_latlng(row):
    if ',' in row['latlng']:
        row['lat'], row['lng'] = row['latlng'].split(',')
    else:
        row['lat'], row['lng'] = '', ''
    return row

def get_latlng(file, address_col, api_key, output):
    
    format_str = {}
    for col in address_col:
        format_str[col] = str

    address_df = pd.read_csv(file, sep =';', dtype = format_str)

    ## CREATING COMPLETE ADDRESS
    address_df['full_address'] = address_df.apply(lambda x: append_address(x, address_col), axis=1)

    ## GET LAT LNG FROM GOOGLE MAPS API
    gmaps = googlemaps.Client(key=api_key)
    address_df['latlng'] = [gmaps_from_address(address, gmaps) for address in tqdm(address_df['full_address'])]

    ## SPLIT LAT AND LNG
    address_df = address_df.apply(seperate_latlng, axis=1)

    ## UPLOAD TO CSV
    address_df.to_csv(output, sep =';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='file', type=str,
                    help='Path to your CSV file with ; delimiters')
    parser.add_argument('-c', action='append', dest='address_col', type=str,
                    help='List of column elements to build the address. Ideally in the following order: street, zip, city, country.')
    parser.add_argument('-api', action='store', dest='api_key', type=str,
                    help='Your GOOGLE MAPS API KEY')
    parser.add_argument('-o', action='store', dest='output', type=str,
                    help='Name of the CSV file in output')
    args = parser.parse_args()

    get_latlng(args.file, args.address_col, args.api_key, args.output)

