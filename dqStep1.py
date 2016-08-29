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

import csv
f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here
def nfl_wins(team):
    wins = 0
    for row in nfl:
        if row[2] == team:
            wins += 1
    return(wins)
cowboys_wins =  nfl_wins("Dallas Cowboys")
falcons_wins =  nfl_wins("Atlanta Falcons")

import csv
class Team():
    def __init__(self, name):
        self.name = name
        f = open("nfl.csv", 'r')
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count
class Team():
    def __init__(self, name):
        self.name = name
        f = open("nfl.csv", 'r')
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count

    def count_wins_in_year(self, year):
        count = 0
        for row in self.nfl:
            if row[2] == self.name and row[0] == year:
                count += 1
        return count

niners = Team("San Francisco 49ers")
niners_wins_2013 = niners.count_wins_in_year("2013")

name_counts = {}
for i in legislators:
    gender = i[3]
    year = i[7]
    name = i[1]
    if gender == "F" and year>1940:
        name = i[1]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

teams = [row[1] for row in nfl_suspensions]
unique_teams = set(teams)
print(unique_teams)

games = [row[2] for row in nfl_suspensions]
unique_games = set(games)
print(unique_games)

import csv
f = open("askreddit_2015.csv", 'r')
csvreader = csv.reader(f)
posts_with_header = list(csvreader)
posts = posts_with_header[1:]
for post in posts[:10]:
    print(post)

if re.search("needle", "haystack") != None:
    print("We found it!")
else:
    print("Not a match")

import re
year_strings = []
for string in strings:
    if re.search("[1-2][0-9]{3}", string) != None:
       year_strings.append(string)

import re
years = re.findall("[1-2][0-9]{3}", years_string)

def count_posts_in_month(month):
    count = 0
    for row in posts:
        if row[2].month == month:
            count += 1
    return count
feb_count = count_posts_in_month(2)
aug_count = count_posts_in_month(8)

world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter=",", dtype="U75", skip_header=True)
print(world_alcohol)