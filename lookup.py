# File Name: lookup.py
""" Description: use this small handy program to lookup any ip adress.
    lookup uses the api focurl und at http://ip-api.com/ """
# https://github.com/dominicegginton/lookup

# import dependencys
import argparse
import requests

def main():

    """ Main  """

    # args parser setup
    parser = argparse.ArgumentParser(description='Lookup by Dominic Egginton')
    parser.add_argument('-a', '--address', metavar='Lookup', type=str, help='lookup adrress')
    parser.add_argument('-s', '--save', metavar='Save', type=str, help='Save result to file')
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
        request = requests.get('http://ip-api.com/json/'+args.address)
    else:
        request = requests.get('http://ip-api.com/json/')

    if request.status_code == 200:
        # sort and print responce
        request_json = request.json()

        if request_json['status'] == 'success':
            line_width = 10
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
            print(''.ljust(line_width)+ 'Timezone: ' + request_json['timezone'])
        elif request_json['status'] == 'fail':
            print('Sorry we could not find: ' + request_json['query'] + '\n')

        if args.save:
            save(request_json, args.save, line_width)

    else:
        print('Error: ' + request.status_code)

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

if __name__ == '__main__':
    main()