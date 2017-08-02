# Ближайшие бары

Программа, позволяющая найти самый большой/маленький/ближайший бар. 
Список баров скачен с [link](data.mos.ru)

#Пример структуры файла с барами
<pre>
    <code>
$ {'ID': '00146684', 'Longitude_WGS84': '37.7502909235696360', 'Name': 'Кальян-бар Shisha Room', 'AdmArea': 'Южный административный округ', 'District': 'район Зябликово', 'geoData': {'type': 'Point', 'coordinates': [37.750290923482424, 55.61870614052117]}, 'system_object_id': '00146684', 'IsNetObject': 'нет', 'SeatsCount': 25, 'PublicPhone': [{'global_object_id': 281494751.0, 'system_object_id': '00146684 _1', 'PublicPhone': 'нет телефона', 'global_id': 35024.0}], 'global_id': 281494751, 'SocialPrivileges': 'нет', 'Latitude_WGS84': '55.6187061404540510', 'TypeObject': 'бар', 'Address': 'Кустанайская улица, дом 8, корпус 3'}
    </code>
</pre>

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5 В качестве аргументов требуется передовать директорий файла со списоком баров. 

<pre>
    <code>
$ python3 bars.py --path "filepath"
    </code>
</pre>

#Пример 

<pre>
    <code>
$ python3 bars.py --path "/Users/User/bars.json"
    </code>
</pre>

#Пример ответа
<pre>
    <code>
[The BIGGEST bar is]
Name: Спорт бар «Красная машина»
Seats count: 450
Address: Автозаводская улица, дом 23, строение 1
Phone: (905) 795-15-84

---------------------------
[The SMALLEST bar is]
Name: БАР. СОКИ
Seats count: 0
Address: Дубравная улица, дом 34/29
Phone: (495) 258-94-19

---------------------------
Do you want to find the closest bar?
Y/N?
  </code>
</pre>

<pre>
    <code>
y
    </code>
</pre>

<pre>
    <code>
Your current latitude: 50
Your current longitude: 30
[The CLOSEST bar is]
Name: Бар Виват
Seats count: 35
Address: посёлок Ерино, дом 1
Phone: (495) 867-55-75
    </code>
</pre>

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
