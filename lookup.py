# File Name: lookup.py
# Description: use this small handy program to lookup any ip adress. lookup uses the api focurl und at http://ip-api.com/
# https://github.com/dominicegginton/lookup
import requests,sys

def Main():
    r = requests.get('http://ip-api.com/json/'+sys.argv[1])
    requestJSON = r.json() 
    for key, value in requestJSON.items():
        print(str(key)+': '+str(value))

if __name__ == '__main__':
    Main()