from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Stoprouteinfo
from .serializers import BusSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import pandas as pd
import json
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
        print(df)
        bus_times = df[3]
        bus_times.rename(columns={'Expected Time': 'Arrival'},inplace=True)
        bus_times = bus_times.to_json(orient='records')
        print(bus_times)
        return Response(json.loads(bus_times))
