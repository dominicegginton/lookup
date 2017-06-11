#!/usr/bin/python
""" Description: use this small handy program to lookup any ip adress.
    lookup uses the api focurl und at http://ip-api.com/ """

import argparse
import os
from platform import system as os_name

import requests
from colorama import init, Fore, Style

def main():
    """ Main  """
    line_width = 10
    init()

    parser = argparse.ArgumentParser(description='Lookup by Dominic Egginton')
    parser.add_argument('-a', '--address', metavar='Lookup', type=str, help='lookup address')
    parser.add_argument('-s', '--save', metavar='Save', type=str, help='Save result to file')
    parser.add_argument('-p', '--ping', help='Ping the address', action='store_true')
    parser.add_argument('-t', '--traceroute', help='Trace the address', action='store_true')
    args = parser.parse_args()

    print_header()
    try:
        if args.address:
            request = requests.get('http://ip-api.com/json/'+args.address)
        else:
            request = requests.get('http://ip-api.com/json/')
        request_json = request.json()
        if request_json['status'] == 'success':
            printer(request_json, line_width)
            if args.ping:
                ping(request_json['query'])
            if args.traceroute:
                trace(request_json['query'])
            if args.save:
                save(request_json, args.save, line_width)
        elif request_json['status'] == 'fail':
            print('Error:')
            print(''.ljust(line_width)+ 'Query sent: ' + request_json['query'])
            print(''.ljust(line_width)+ 'Message: ' + request_json['message'])
        else:
            print('Error: ' + str(request.status_code))
    except requests.exceptions.RequestException as error:
        print('Error: ' + str(error))
        print('\n Check your internet connection')

def print_header():
    """ Print the header of the UI """
    print(Fore.CYAN + " _     ___   ___  _  ___   _ ____  ")
    print("| |   / _ \ / _ \| |/ / | | |  _ \ ")
    print("| |  | | | | | | | ' /| | | | |_) |")
    print("| |__| |_| | |_| | . \| |_| |  __/ ")
    print("|_____\___/ \___/|_|\_\\\___/|_|    " + Style.RESET_ALL + "     [ Dominic Egginton | github.com/dominicegginton/lookup ]")
    print("\n")

def printer(request_json, line_width):
    """ Print the main body of the UI """
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
        os.system('ping -n 2 ' + address)
    else:
        os.system('ping -c 2 ' + address)

def trace(address):
    """tracerout"""
    print('\n')
    if os_name().lower() == 'windows':
        os.system('tracert ' + address)
    else:
        os.system('traceroute ' + address)
if __name__ == '__main__':
    main()
