import os
import json
from argparse import ArgumentParser
from math import sqrt


def load_data(path_to_file):
    if not os.path.exists(path_to_file):
        return None
    else:
        with open(path_to_file, 'r', encoding='cp1251') as json_bars:
            return json.load(json_bars)


def get_biggest_bar(json_bars):
    biggest_bar = max(json_bars, key=lambda bar: bar['SeatsCount'])
    return biggest_bar


def get_smallest_bar(json_bars):
    smallest_bar = min(json_bars, key=lambda bar: bar['SeatsCount'])
    return smallest_bar


def get_closest_bar(json_bars):
    closest_bar = min(json_bars, key=lambda bar: bar['distance_to_bar'])
    return closest_bar


def get_distance_to_bars(user_lat, user_lon, json_bars):
    for bar in json_bars:
        bar_lat = bar['geoData']['coordinates'][0]
        bar_lon = bar['geoData']['coordinates'][1]
        distance_to_bar = sqrt((bar_lat - float(user_lat)) ** 2 +
                               (bar_lon - float(user_lon)) ** 2)
        bar['distance_to_bar'] = distance_to_bar
    return json_bars


def get_coordinates():
    game = True
    while game:
        is_need_find_bar = input('Найти ближайший бар? \n'
                                 'Д/Н? \n')
        if is_need_find_bar == 'д' or is_need_find_bar == 'Д':
            latitude = input('Широта: ')
            longitude = input('Долгота: ')
            game = False
            return latitude, longitude
        elif is_need_find_bar == 'н' or is_need_find_bar == 'Н':
            game = False
            return None
        else:
            print('Д or Н ?')


def show_info_bar(json_bar, bar_property):
    if bar_property == 'biggest':
        print('[Самый большой бар]')
    elif bar_property == 'smallest':
        print('[Самый маленький бар]')
    elif bar_property == 'closest':
        print('[Самый близкий бар]')
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

    json_bars = load_data(arg.path)
    if json_bars:
        show_info_bar(get_biggest_bar(json_bars), 'biggest')
        show_info_bar(get_smallest_bar(json_bars), 'smallest')
    user_coordinates = get_coordinates()
    if user_coordinates:
        json_bars = get_distance_to_bars(user_coordinates[0], user_coordinates[1], json_bars)
        show_info_bar(get_closest_bar(json_bars), 'closest')
