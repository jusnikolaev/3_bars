import json
import os
import requests


def load_data(filepath):
    if not os.path.exists(filepath):
        print('No file in directory')
        return None
    with open(filepath, 'r', encoding='cp1251') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(list_of_bars):
    biggest_bar = max(list_of_bars, key=lambda bar: bar['SeatsCount'])
    print(show_bar(biggest_bar))


def get_smallest_bar(list_of_bars):
    smallest_bar = max(list_of_bars, key=lambda bar: bar['SeatsCount'])
    print(show_bar(smallest_bar))


def get_distance_to_bar(user_lon, user_lat, list_of_bars):
    step = 0
    for bar in list_of_bars:
        bar_lon = bar['geoData']['coordinates'][1]
        bar_lat = bar['geoData']['coordinates'][0]
        maps_api = requests.get('https://maps.googleapis.com/maps/api/directions/json?'
                                'origin={},{}&destination={},{}&mode=walking&'
                                'key=AIzaSyDRhyqsqDr3mzLXtA_Fi4CBaXNo0b-qSzQ'.format(
                                    user_lon, user_lat, bar_lon, bar_lat))
        maps_api = maps_api.json()
        print(maps_api)
        try:
            time_by_walk = maps_api['routes'][0]['legs'][0]['duration'].get('text').split()
            bar['geoData']['coordinates'] = count_time(time_by_walk)
            step += 1
            print('Step: {}'.format(step))
            closest_bar = min(list_of_bars, key=lambda time: time['SeatsCount'])
            print(show_bar(closest_bar))
        except IndexError:
            print('Index error')

def count_time(time_by_walk):
    if len(time_by_walk) is 4:
        time_in_minutes = int(time_by_walk[0]) * 60 + int(time_by_walk[2])
        return time_in_minutes
    elif len(time_by_walk) is 2:
        time_in_minutes = int(time_by_walk[0])
        return time_in_minutes
    else:
        print('Time count error')
        return None



def show_bar(bar):
    return 'Название: {} \n Адрес: {} \n Телефон: {} \n ' \
           'Число посадок: {}'.format(
        bar['Name'], bar['Address'],
        bar['PublicPhone'][0].get('PublicPhone'), bar['SeatsCount'])


if __name__ == '__main__':
    path = '/Users/jusnikolaev/Desktop/devman/3_bars/list_of_bars.json'
    a = load_data(path)
    get_distance_to_bar(55.752, 37.615, a)
