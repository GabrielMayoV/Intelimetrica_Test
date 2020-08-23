from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection

def statistics(request,longitude,latitud,radius):
    if request.method == 'GET':
        cursor = connection.cursor()
        q = "SELECT COUNT(rating), AVG(rating), stddev(rating)  FROM api_restaurant WHERE ST_DWithin(ST_SetSRID(ST_MakePoint(lng,lat),4326), ST_MakePoint({},{})::geography, {});".format(longitude,latitud,radius)
        cursor.execute(q)
        result = cursor.fetchall()
        return JsonResponse({'count':result[0][0],
                             'avg':result[0][1],
                             'std':result[0][2]})
