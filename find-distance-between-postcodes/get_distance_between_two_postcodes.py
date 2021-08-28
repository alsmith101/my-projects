import requests

origin_r = requests.get(
    'http://dev.virtualearth.net/REST/v1/Locations',
    params={
        'postalCode': 'RH42DY',
        "countryRegion": "UK",
        "key": "AvLAa02VsrPE9MphBqV8FoXlBz8BEUrKpUMGGJOLzYeN6kdyojhCGO0lpOAHZBO_",
    })

destination_r = requests.get(
    'http://dev.virtualearth.net/REST/v1/Locations',
    params={
        'postalCode': 'TW181RB',
        "countryRegion": "UK",
        "key": "AvLAa02VsrPE9MphBqV8FoXlBz8BEUrKpUMGGJOLzYeN6kdyojhCGO0lpOAHZBO_",
    })

origin_text = origin_r.json()
destination_text = destination_r.json()
print(destination_text)

origin_coordinates = origin_text['resourceSets'][0]['resources'][0]['point']['coordinates']
origin_longitude = origin_coordinates[0]
origin_latitude = origin_coordinates[1]

destination_coordinates = destination_text['resourceSets'][0]['resources'][0]['point']['coordinates']
destination_longitude = destination_coordinates[0]
destination_latitude = destination_coordinates[1]


r = requests.get(
    'https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix',
    params={
        'origins': f"{origin_longitude}, {origin_latitude}",
        'destinations': f"{destination_longitude}, {destination_latitude}",
        'travelMode': 'driving',
        "key": 'AvLAa02VsrPE9MphBqV8FoXlBz8BEUrKpUMGGJOLzYeN6kdyojhCGO0lpOAHZBO_',
    })

print(r.url)
print(r.json())
