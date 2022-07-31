from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from xpressbus.models.models import Stoprouteinfo
from .serializers import BusSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import pandas as pd
import json
import pickle
import os 
from django.conf import settings

# Create your views here.

def index(request):
    return render(request, "index.html")


class RouteStopView(APIView):
    http_method_names = ['get']

    def get(self, request):
        routeId = request.query_params.get('routeId')
        routeId = routeId.upper()
        # stops = Stoprouteinfo.objects.all()
        stops = Stoprouteinfo.objects.filter(routesid__contains=routeId)
        serializer = BusSerializer(stops, many=True)
        return JsonResponse({"stops": serializer.data}, safe=False)

class RoutePredictView(APIView):
    http_method_names = ['get']
    
    def get(self, request):
        """get model name"""
        routeId = request.query_params.get('routeId')
        routeId = routeId.upper()
        direction = request.query_params.get('direction')
        basicPath = settings.BASE_DIR
        modelPath = os.path.join(basicPath, 'xpressbus/models/ML/')
        modelName = modelPath + routeId + "_" + direction + "dir_rf_model.pkl"
        f = open(modelName, 'rb')
        model = pickle.load(f)
        """get model input data"""
        # preprocess with month
        monthData = request.query_params.get('month')
        monthDict = {"JAN" : 0, "FEB": 1, "MAR" : 2, "APR" : 3, "MAY" : 4, "JUN" : 5, "JUL" : 6, "AUG" : 7, "SEP" : 8, "OCT" : 9, "NOV" : 10, "DEC" : 11}
        month = monthDict.get(monthData.upper())
        # preprocess with day
        dayOfWeekData = request.query_params.get('dayOfWeek')
        weekDict = {"MON" : 0, "TUE" : 1, "WED" : 2, "THU" : 3, "FRI" : 4, "SAT" : 5, "SUN" : 6}
        dayOfWeek = weekDict.get(dayOfWeekData.upper())
        # preprocess with the hour and rushHour
        hour = int(request.query_params.get('hour'))
        rushHour = 0 # default not rushHour
        if dayOfWeek <= 4:
            if 8 <= hour <= 9 or 16 <= hour <= 18:
                rushHour = 1
        # get temp and wind_speed
        temp = request.query_params.get('temp')
        wind_speed = request.query_params.get('wind_speed')
        data = {'month': month, 
                'dayOfWeek': dayOfWeek,
                'rushHour': rushHour,
                'hour': hour,
                'temp': temp,
                'wind_speed': wind_speed,
                }
        """get machine learning model result"""
        df = pd.DataFrame([data])
        predictTime = model.predict(df)
        return JsonResponse({"result": predictTime[0]}, safe=False)
        

@api_view(['GET'])
def stop_detail(request, id):
    
    try:
        stop = Stoprouteinfo.objects.get(pk=id)
    except Stoprouteinfo.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BusSerializer(stop)
        return Response(serializer.data)

# Query dublin bus web page to get bus times:
# code adapted from https://stackabuse.com/reading-and-writing-html-tables-with-pandas/
@api_view(['GET'])
def realTimeData(request, busNo):
    if request.method == 'GET':
        url = "https://www.dublinbus.ie/en/RTPI/Sources-of-Real-Time-Information/?searchtype=view&searchquery="
        df = pd.read_html(url + str(busNo))
        bus_times = df[3]
        bus_times.rename(columns={'Expected Time': 'Arrival'},inplace=True)
        bus_times = bus_times.to_json(orient='records')
        return Response(json.loads(bus_times))


