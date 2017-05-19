# File Name: lookup.py
# Description: use this small handy program to lookup any ip adress. lookup uses the api focurl und at http://ip-api.com/
# https://github.com/dominicegginton/lookup

# import dependencys
import requests,sys,argparse

def Main():

    # args parser setup
    parser = argparse.ArgumentParser(description='Lookup by Dominic Egginton')
    parser.add_argument('-a', '--address', metavar='lookup', type=str, help='lookup adrress')
    args = parser.parse_args()

    # if address is supplied
    if args.address:
        r = requests.get('http://ip-api.com/json/'+args.address)
    else:
        r = requests.get('http://ip-api.com/json/')
    
    if r.status_code == 200:
        # sort and print responce
        requestJSON = r.json() 
        for key, value in requestJSON.items():
            print(str(key)+': '+str(value))
    else:
        print('Error in sending request')

if __name__ == '__main__':
    Main()