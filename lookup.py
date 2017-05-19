# File Name: lookup.py
# Description: use this small handy program to lookup any ip adress. lookup uses the api focurl und at http://ip-api.com/
# https://github.com/dominicegginton/lookup
import requests,sys,argparse

def Main():
    parser = argparse.ArgumentParser(description='Lookup by Dominic Egginton')
    parser.add_argument('-a', '--address', metavar='lookup', type=str, help='lookup adrress')
    args = parser.parse_args()
    
    
    
    if args.address:
        print('doing ' + args.address)
        r = requests.get('http://ip-api.com/json/'+args.address)
    else:
        r = requests.get('http://ip-api.com/json/')
    requestJSON = r.json() 
    for key, value in requestJSON.items():
        print(str(key)+': '+str(value))

if __name__ == '__main__':
    Main()