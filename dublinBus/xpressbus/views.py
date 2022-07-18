from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Stoprouteinfo
from .serializers import BusSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

def index(request):
    return render(request, "index.html")


class RouteStopView(APIView):
    http_method_names = ['get']

    def get(self, request):
        routeId = request.query_params.get('routeId')
        # stops = Stoprouteinfo.objects.all()
        stops = Stoprouteinfo.objects.filter(routesid__contains=routeId)
        serializer = BusSerializer(stops, many=True)
        return JsonResponse({"stops": serializer.data}, safe=False)

@api_view(['GET'])
def stop_detail(request, id):
    
    try:
        stop = Stoprouteinfo.objects.get(pk=id)
    except Stoprouteinfo.DoesNotExists:
        return Responsse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BusSerializer(stop)
        return Response(serializer.data)


