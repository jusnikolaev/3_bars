import os
import json
from argparse import ArgumentParser
from math import sqrt


def validate_path(path_to_file):
    if not os.path.exists(path_to_file):
        print('No such file')
        return False
    else:
        return True


def load_data(path_to_file):
    with open(path_to_file, 'r', encoding='cp1251') as json_bars:
        return json.load(json_bars)


def get_biggest_bar(json_bars):
    biggest_bar = max(json_bars, key=lambda bar: bar['SeatsCount'])
    return biggest_bar


def get_smallest_bar(json_bars):
    smallest_bar = min(json_bars, key=lambda bar: bar['SeatsCount'])
    return smallest_bar


def get_closest_bar(json_bars, user_latitude, user_longitude):
    closest_bar = min(json_bars,
                      key=lambda bar: get_distance_to_bars(user_latitude,
                                                           user_longitude,
                                                           bar['geoData']
                                                           ['coordinates']))
    return closest_bar


def get_distance_to_bars(user_lat, user_lon, bar):
    bar_lat = bar[0]
    bar_lon = bar[1]
    distance_to_bar = sqrt((bar_lat - user_lat) ** 2 +
                           (bar_lon - user_lon) ** 2)
    return distance_to_bar


def validate_coordinates(latitude, longitude):
    try:
        latitude = float(latitude)
        longitude = float(longitude)
        if -90 <= latitude <= 90 and -180 <= longitude <= 180:
            return latitude, longitude
        else:
            print('Invalid value: Values are not within the allowed range.'
                  'Try again.')
            return None
    except ValueError:
        print('Invalid value: Coordinates must be numbers.'
              'Try again.')
        return None


def get_coordinates():
    latitude = input('Latitude: ')
    longitude = input('Longitude: ')
    return latitude, longitude


def show_info_bar(json_bar, bar_property):
    if bar_property == 'biggest':
        print('[The biggest bar]')
    elif bar_property == 'smallest':
        print('[The smallest bar]')
    elif bar_property == 'closest':
        print('[The closest bar]')
    print('Название: {} \n'
          'Число мест: {} \n'
          'Адрес: {} \n'
          'Телефон: {} \n'.format(json_bar['Name'],
                                  json_bar['SeatsCount'],
                                  json_bar['Address'],
                                  json_bar['PublicPhone'][0]['PublicPhone']))
    print('---------------------------')


if __name__ == '__main__':
    parser = ArgumentParser(description='Path to file with bars')
    parser.add_argument('--path', type=str)
    arg = parser.parse_args()

    json_bars = validate_path(arg.path)
    if json_bars:
        json_bars = load_data(arg.path)
        user_coordinates = get_coordinates()
        user_coordinates = validate_coordinates(user_coordinates[0],
                                                user_coordinates[1])
        if user_coordinates:
            show_info_bar(get_closest_bar(json_bars,
                                          float(user_coordinates[0]),
                                          float(user_coordinates[1])),
                          'closest')
            show_info_bar(get_biggest_bar(json_bars), 'biggest')
            show_info_bar(get_smallest_bar(json_bars), 'smallest')
        else:
            print('Error: try again.')
