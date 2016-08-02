f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
final_data = []
for row in rows:
    split_list = row.split(',')
    final_data.append(split_list)
print(final_data[0:4])

vocabulary = open("dictionary.txt", "r").read()

weather_counts = {}
for item in weather:
    if item in weather_counts:
        weather_counts[item] = weather_counts[item]+1
    else:
        weather_counts[item] = 1