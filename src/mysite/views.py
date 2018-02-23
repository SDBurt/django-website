'''Imports'''
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    '''provide the homepage'''
    #return HttpResponse("homepage")
    return render(request, 'mysite/homepage.html')


def about(request):
    '''Provide the about page'''
    #return HttpResponse("about")
    return render(request, 'mysite/about.html')
