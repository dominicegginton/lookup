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

    # print header
    print(" _     ___   ___  _  ___   _ ____  ")
    print("| |   / _ \ / _ \| |/ / | | |  _ \ ")
    print("| |  | | | | | | | ' /| | | | |_) |")
    print("| |__| |_| | |_| | . \| |_| |  __/ ")
    print("|_____\___/ \___/|_|\_\\\___/|_|    ")
    print("\n")

    # if address is supplied
    if args.address:
        r = requests.get('http://ip-api.com/json/'+args.address)
    else:
        r = requests.get('http://ip-api.com/json/')
    
    if r.status_code == 200:
        # sort and print responce
        requestJSON = r.json()
        
        if requestJSON['status'] == 'success':
            lineWidth = 10
            print('Lookup Information For : ' + requestJSON['query'])
            
            print('\nGeneral IP Information')
            print(''.ljust(lineWidth)+ 'ISP: ' + requestJSON['isp'])
            print(''.ljust(lineWidth)+ 'AS number / name: ' + requestJSON['as'])
            print(''.ljust(lineWidth)+ 'Organization name: ' + requestJSON['org'])
            print(''.ljust(lineWidth)+ 'Organization name: ' + requestJSON['org'])

            print('\nGeolocation IP Information')
            print(''.ljust(lineWidth)+ 'Latitude: ' + str(requestJSON['lat']))
            print(''.ljust(lineWidth)+ 'Longitude: ' + str(requestJSON['lon']))
            print(''.ljust(lineWidth)+ 'Country: ' + requestJSON['country'] + ' ' + requestJSON['countryCode'])
            print(''.ljust(lineWidth)+ 'Region: ' + requestJSON['regionName'] + ' ' + requestJSON['region'])
            print(''.ljust(lineWidth)+ 'City: ' + requestJSON['city'])
            print(''.ljust(lineWidth)+ 'Zip / Postcode: ' + requestJSON['zip'])
            print(''.ljust(lineWidth)+ 'Timezone: ' + requestJSON['timezone'])
        elif requestJSON['status'] == 'fail':
            print('Sorry we could not find: ' + requestJSON['query'] + '\n')
    else:
        print('Error: ' + r.status_code)

if __name__ == '__main__':
    Main()