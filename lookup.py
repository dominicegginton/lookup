# File Name: lookup.py
""" Description: use this small handy program to lookup any ip adress.
    lookup uses the api focurl und at http://ip-api.com/ """
# https://github.com/dominicegginton/lookup

import argparse
import requests
from platform import system as os_name
from os import system as os_call

def main():

    """ Main  """

    parser = argparse.ArgumentParser(description='Lookup by Dominic Egginton')
    parser.add_argument('-a', '--address', metavar='Lookup', type=str, help='lookup address')
    parser.add_argument('-s', '--save', metavar='Save', type=str, help='Save result to file')
    parser.add_argument('-p', '--ping', help='Ping the address', action='store_true')
    parser.add_argument('-t', '--traceroute', help='Trace the address', action='store_true')
    args = parser.parse_args()

    print_header()

    if args.address:
        request = requests.get('http://ip-api.com/json/'+args.address)
    else:
        request = requests.get('http://ip-api.com/json/')

    if request.status_code == 200:
        request_json = request.json()
        line_width = 10
        printer(request_json, line_width)
        if args.ping:
            ping(request_json['query'])
        if args.traceroute:
            trace(request_json['query'])
        if args.save:
            save(request_json, args.save, line_width)

    else:
        print('Error: ' + request.status_code)

def print_header():
    """ Print the header of the UI """
    print("\033[1;31m _     ___   ___  _  ___   _ ____  ")
    print("| |   / _ \ / _ \| |/ / | | |  _ \ ")
    print("| |  | | | | | | | ' /| | | | |_) |")
    print("| |__| |_| | |_| | . \| |_| |  __/ ")
    print("|_____\___/ \___/|_|\_\\\___/|_|    \033[1;m     [ Dominic Egginton | github.com/dominicegginton/lookup ]")
    print("\n")

def printer(request_json, line_width):
    """ Print the main body of the UI """
    if request_json['status'] == 'success':
        print('Lookup Information For : ' + request_json['query'])
        print('\nGeneral IP Information')
        print(''.ljust(line_width)+ 'ISP: ' + request_json['isp'])
        print(''.ljust(line_width)+ 'AS number / name: ' + request_json['as'])
        print(''.ljust(line_width)+ 'Organization name: ' + request_json['org'])
        print('\nGeolocation IP Information')
        print(''.ljust(line_width)+ 'Latitude: ' + str(request_json['lat']))
        print(''.ljust(line_width)+ 'Longitude: ' + str(request_json['lon']))
        print(''.ljust(line_width)+ 'Country: ' + request_json['country']
              + ' ' + request_json['countryCode'])
        print(''.ljust(line_width)+ 'Region: ' + request_json['regionName']
              + ' ' + request_json['region'])
        print(''.ljust(line_width)+ 'City: ' + request_json['city'])
        print(''.ljust(line_width)+ 'Zip / Postcode: ' + request_json['zip'])
        print(''.ljust(line_width)+ 'Timezone: ' + request_json['timezone'] + '\n')
    elif request_json['status'] == 'fail':
        print('Sorry we could not find: ' + request_json['query'] + '\n')

def save(request_json, filename, line_width):
    ''' save '''
    print('saving to file')
    writer = open(str(filename), 'w')
    writer.writelines('Lookup Information For : ' + request_json['query'])
    writer.writelines('\n')
    writer.writelines('\nGeneral IP Information')
    writer.write('\n'.ljust(line_width)+ 'ISP: ' + request_json['isp'])
    writer.write('\n'.ljust(line_width)+ 'AS number / name: ' + request_json['as'])
    writer.write('\n'.ljust(line_width)+ 'Organization name: ' + request_json['org'])
    writer.write('\n')
    writer.write('\nGeolocation IP Information')
    writer.write('\n'.ljust(line_width)+ 'Latitude: ' + str(request_json['lat']))
    writer.write('\n'.ljust(line_width)+ 'Longitude: ' + str(request_json['lon']))
    writer.write('\n'.ljust(line_width)+ 'Country: ' + request_json['country']
                 + ' ' + request_json['countryCode'])
    writer.write('\n'.ljust(line_width)+ 'Region: ' + request_json['regionName']
                 + ' ' + request_json['region'])
    writer.write('\n'.ljust(line_width)+ 'City: ' + request_json['city'])
    writer.write('\n'.ljust(line_width)+ 'Zip / Postcode: ' + request_json['zip'])
    writer.write('\n'.ljust(line_width)+ 'Timezone: ' + request_json['timezone'])
    writer.write('\n')
    writer.close()

def ping(address):
    """ping"""
    if os_name().lower() == 'windows':
        print('\n' + os_call('ping -n 2 ' + address))
    else:
        print('\n' + str(os_call('ping -c 2 ' + address)))

def trace(address):
    """tracerout"""
    if os_name().lower() == 'windows':
        print('\n\n' + os_call('tracert ' + address))
    else:
        print('\n\n' + str(os_call('traceroute ' + address)))

if __name__ == '__main__':
    main()