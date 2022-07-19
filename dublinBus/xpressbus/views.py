from django.shortcuts import render
import pandas as pd
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

def index(request):
    return render(request, "index.html")

def real_time_bus(request):

    url = "https://www.dublinbus.ie/en/RTPI/Sources-of-Real-Time-Information/?searchtype=view&searchquery=2"
    # read html table into a data frame
    df = pd.read_html(url)
    # print(df)


    time_table = df[3].to_json(orient='records')

    return Response(json.loads(time_table))