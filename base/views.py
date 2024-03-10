
from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def view(request):
  if request.method == 'GET':
    persons = Person.objects.all()
    serialized = PersonSerializer(persons, many=True)
    return JsonResponse(serialized.data, safe=False)
  
  if request.method == 'POST':
    serialized = PersonSerializer(data = request.data)
    if serialized.is_valid():
      serialized.save()
      return Response(serialized.data, status = status.HTTP_201_CREATED)