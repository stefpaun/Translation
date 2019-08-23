from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, "home.html")

def count(request):
    fulltext = request.GET['fulltext']
    wlist = fulltext.split()
    wdictionary = {}
    for w in wlist:
        if w in wdictionary:
            wdictionary[w] += 1
        else:
            wdictionary[w] = 1

    sortedwords = sorted(wdictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, "count.html", {'fulltext':fulltext, 'count':len(wlist), 'sortedwords':sortedwords})

def about(request):
    return render(request, "about.html")

