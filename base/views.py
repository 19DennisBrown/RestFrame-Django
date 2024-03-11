

from django.shortcuts import render
from django.http import JsonResponse
from .models import Person
from .serializers import PersonSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def view(request):
  if request.method == 'GET':
    persons = Person.objects.all()
    serialized = PersonSerializer(persons, many=True)
    return JsonResponse(serialized.data, safe=False)
  
  if request.method == 'POST':
    serialized = PersonSerializer(data=request.data)
    if serialized.is_valid():
      serialized.save()
      return Response(serialized.data, status=status.HTTP_201_CREATED)
  return JsonResponse(serialized.data, safe=False)


def personView(request, id):

  try:
    person = Person.objects.get(id=id)
  except person.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serialized = PersonSerializer(person)
    return JsonResponse(serialized.data, safe=False)
  
  if request.method == 'PUT':
    serialized = PersonSerializer(person, data=request.data)
    if serialized.is_valid():
      serialized.save()
      return Response(serialized.data)
    else:
      return Response(status=status.HTTP_400_BAD_REQUEST)

  if request.method == 'DELETE':
    person.delete()
    return Response(status=status.HTTP_404_NOT_FOUND)