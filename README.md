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

