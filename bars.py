import json
import os
import requests
import argparse


# Загружаем JSON с барами
def load_data(filepath):
    if not os.path.exists(filepath):
        print('No file in directory')
        return None
    with open(filepath, 'r', encoding='cp1251') as file_handler:
        return json.load(file_handler)


# Нахождение самого большого бара
def get_biggest_bar(list_of_bars):
    biggest_bar = max(list_of_bars, key=lambda bar: bar['SeatsCount'])
    print(show_bar(biggest_bar))


# Нахождение самого маленького бара
def get_smallest_bar(list_of_bars):
    smallest_bar = min(list_of_bars, key=lambda bar: bar['SeatsCount'])
    print(show_bar(smallest_bar))


# Поиск минимального времени пешком от текущих координат до всех баров
def get_distance_to_bar(user_lon, user_lat, list_of_bars):
    step = 0
    for bar in list_of_bars:
        bar_lon = bar['geoData']['coordinates'][1]
        bar_lat = bar['geoData']['coordinates'][0]
        maps_api = requests.get('https://maps.googleapis.com'
                                '/maps/api/directions/json?'
                                'origin={},{}&destination={},'
                                '{}&mode=walking&'
                                'key=AIzaSyDRhyqsqDr3mzLXtA_Fi4CBaXNo0b-qSzQ'
                                .format(user_lon, user_lat, bar_lon, bar_lat))
        maps_api = maps_api.json()
        try:
            time_by_walk = maps_api['routes'][0]['legs'][0]['duration'].get('text').split()
            bar['geoData']['coordinates'][0] = count_time(time_by_walk)
            step += 1
            loading_show(list_of_bars, step)
        except IndexError:
            print('Index error')
    closest_bar = min(list_of_bars, key=lambda time: time['geoData']['coordinates'][0])
    print(show_bar(closest_bar))


# Преобразование полученных временных данных из Гугла в минуты
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


# Функция вывода бара
def show_bar(bar):
    return '-------------------- \n Название: {} \n Адрес: {} \n ' \
           'Телефон: {} \n ' \
           'Число посадок: {} \n --------------------'.format(
            bar['Name'], bar['Address'],
            bar['PublicPhone'][0].get('PublicPhone'), bar['SeatsCount'])


# Получение текущих координат пользователя по IP
def current_location():
    send_url = 'http://freegeoip.net/json'
    result = requests.get(send_url)
    j = json.loads(result.text)
    curr_coords = [j['longitude'], j['latitude']]
    return curr_coords


# Вывод этапа загрузки в процентах
def loading_show(list_of_bars, current_count):
    percent = int(len(list_of_bars) / 100)
    if current_count % percent is 0:
        print('Loading: '.format(int(current_count / percent)))


# Тривиальная версия функции выше.
def user_info_bars(bars):
    print('Please, wait. \n Looking info about bars...')
    curr_user_loc = current_location()
    print('Biggest bar: {}  \n'
          'Smallest bar: {} \n'
          'Closest bar: {}'.format(get_biggest_bar(bars),
                                   get_smallest_bar(bars),
                                   get_distance_to_bar(curr_user_loc[0], curr_user_loc[1], bars)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Path to file with bars')
    parser.add_argument('--path', type=argparse.FileType('r'))
    args = parser.parse_args()
    try:
        path = load_data(args.path)
    except TypeError:
        path = '/Users/jusnikolaev/Desktop/devman/3_bars/list_of_bars.json'
    bars = load_data(path)
    user_info_bars(bars)

