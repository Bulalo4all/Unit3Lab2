with open('weather.csv', 'r') as weather:
    data = weather.read()

items = data.split(",")
print(items)