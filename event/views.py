from django.shortcuts import render
from django.http import HttpResponse
# from .serializers import EventSerializer
# from rest_framework.decorators import api_view
from .data_import import get_data

# @api_view(['GET', 'POST'])
def index(request):
    # if request.POST:
    # else :
    if request.method == 'GET':
        # get_data()
        print("request.GET", request.GET)
        print("request.data", request.data)
        return HttpResponse("Hello, world. You're at the GET event index.")
    if request.method == 'POST':
        print("request.POST", request.POST)
        print("request.data", request.data)
        return HttpResponse("Hello, world. You're at the POST event index.")
