import requests
import operator
import statistics
import MySQLdb
from map.models import Map

def get_data():
    textfile = open("map/data.txt", 'r')
    readin = textfile.read()
    dataset = readin.splitlines()
    #elements = []
    for line in dataset[1:]:
        temp = Map()
        sep = line.split(",")
        temp.id = int(sep[0])
        temp.import_country = sep[1]
        temp.model = sep[2]
        temp.make = sep[3]
        temp.sold_by = sep[4]
        temp.sale_price = float(sep[5])
        temp.save()

def get_features():
    db = MySQLdb.connect(host='localhost', user='root', passwd='1234', db='thinkingwithtools')
    cur = db.cursor()
    cur.execute("SELECT * FROM map_map")
    data = cur.fetchall()

    country = {}
    for e in data:
        if e.import_country in country:
            country[e.import_country].append(e.sale_price)
        else:
            country[e.import_country]= []
            country[e.import_country].append(e.sale_price)

    for c in country:
        country[c] = statistics.mean(country[c])

    sorted_country = sorted(country.items(), key=operator.itemgetter(1))
    top_5 = sorted_country[-5:]


