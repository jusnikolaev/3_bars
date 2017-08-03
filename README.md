# Bars

A program that allows you to find the largest / smallest / nearest bar.
List of bars dowloaded [here](data.mos.ru)

#Example of document signature
<pre>
    <code>
$ {'ID': '00146684', 'Longitude_WGS84': '37.7502909235696360', 'Name': 'Кальян-бар Shisha Room', 'AdmArea': 'Южный административный округ', 'District': 'район Зябликово', 'geoData': {'type': 'Point', 'coordinates': [37.750290923482424, 55.61870614052117]}, 'system_object_id': '00146684', 'IsNetObject': 'нет', 'SeatsCount': 25, 'PublicPhone': [{'global_object_id': 281494751.0, 'system_object_id': '00146684 _1', 'PublicPhone': 'нет телефона', 'global_id': 35024.0}], 'global_id': 281494751, 'SocialPrivileges': 'нет', 'Latitude_WGS84': '55.6187061404540510', 'TypeObject': 'бар', 'Address': 'Кустанайская улица, дом 8, корпус 3'}
    </code>
</pre>

# How launch

<pre>
    <code>
$ python3 bars.py --path "filepath"
    </code>
</pre>

#Use example

<pre>
    <code>
$ python3 bars.py --path "/Users/User/bars.json"
    </code>
</pre>

#Answer example
<pre>
    <code>
[Самый большой бар]
Название: Спорт бар «Красная машина»
Число мест: 450
Адрес: Автозаводская улица, дом 23, строение 1
Телефон: (905) 795-15-84

---------------------------
[Самый маленький бар]
Название: БАР. СОКИ
Число мест: 0
Адрес: Дубравная улица, дом 34/29
Телефон: (495) 258-94-19

---------------------------
Найти ближайший бар?
Д/Н?
  </code>
</pre>

<pre>
    <code>
Д
    </code>
</pre>

<pre>
    <code>
Широта: 50
Долгота: 30
[Самый близкий бар]
Название: Бар Виват
Число мест: 35
Адрес: посёлок Ерино, дом 1
Телефон: (495) 867-55-75
    </code>
</pre>

