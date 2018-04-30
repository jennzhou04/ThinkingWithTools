import json
import requests
import operator
import statistics
#from pymodels import *



class Data:
    id = None
    import_country = ""
    model = ""
    make = ""
    sold_by = ""
    sale_price = None

    def __str__(self):
        return self.import_country
        #return '%s %s' % (self.make, self.model)
    def print(self):
        return {
            "id": self.id,
            "import_country": self.import_country,
            "model": self.model,
            "make": self.make,
            "sold_by": self.sold_by,
            "sale_price": self.sale_price
        }

def get_data(dataset):
    dataset = dataset.splitlines()
    data = {}
    first = dataset[0].split(",")
    for i, elem in enumerate(first):
        data[elem] = i
    elements = []
    for line in dataset[1:]:
        temp = Data()
        sep = line.split(",")
        temp.id = int(sep[0])
        temp.import_country = sep[1]
        temp.model = sep[2]
        temp.make = sep[3]
        temp.sold_by = sep[4]
        temp.sale_price = int(sep[5])
        elements.insert(temp.id, temp)
        #print(temp)
    return elements

def common_car(dataset):
    car = {}

    for d in dataset:
        if d.model in car:
            car[d.model]+=1
        else:
            car[d.model] = 1

    return sorted(car.items(), key=operator.itemgetter(1))[-5:]
def find_top_5(elements):
    country = {}

    for e in elements:
        if e.import_country in country:
            country[e.import_country].append(e.sale_price)
        else:
            country[e.import_country]= []
            country[e.import_country].append(e.sale_price)

    for c in country:
        country[c] = statistics.mean(country[c])

    sorted_country = sorted(country.items(), key=operator.itemgetter(1))
    top_5 = sorted_country[-5:]
    return top_5



if __name__ == "__main__":
    url = 'https://my.api.mockaroo.com/interview-api-0.json?key=e6ac1da0'
    dataset = requests.get(url).text
    data = get_data(dataset)

    five = find_top_5(data)
    popular_car = {}
    for f in five:
        #print(f[0])
        url2 = url + '&amp;countries=' + f[0]
        country_data = get_data(requests.get(url2).text)
        popular_car[f[0]]=common_car(country_data)
    print(popular_car)







#print(sorted_country[-5:])
'''
max = {
    "country": None,
    "highest": 0
}
for c in country:
    country[c] = statistics.mean(country[c])
    if country[c] > max["highest"]:
        max["highest"]= country[c]
        max["country"] = c
print(country)
print(max)
'''






#print(input)