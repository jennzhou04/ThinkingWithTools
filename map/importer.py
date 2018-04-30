import requests
import operator
import statistics
import MySQLdb
from map.models import Map

def get_data():
    #textfile = open("map/data.txt", 'r')
    #readin = textfile.read()
    url = 'https://my.api.mockaroo.com/interview-api-0.json?key=e6ac1da0'
    readin = requests.get(url).text
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



