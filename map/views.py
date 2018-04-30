from django.shortcuts import render
from django.http import HttpResponse
from . import importer
from map.models import Map
import statistics
import operator
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def index(request):
    #return HttpResponse("hi
    importer.get_data()

    #print(Map.objects.all())
    #for item in Map.objects.all():
    #    print(item)
    temp = Map.objects.all()
    qset = {}
    for data in temp:
        if data.import_country in qset:
            qset[data.import_country].append(data.sale_price)
        else:
            qset[data.import_country]=[]
            qset[data.import_country].append(data.sale_price)
    for q in qset:
        qset[q] = statistics.mean(qset[q])
        
    queryset = sorted(qset.items(), key=operator.itemgetter(1))[-5:]
    qset_json = json.dumps(list(queryset), cls=DjangoJSONEncoder)

    context = {
        "queryset": queryset,
        "qset_list": qset_json
    }
    return render(request, 'map/index.html', context)

def visualization(request):
    return render(request, 'map/visualization.html')

