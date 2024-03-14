from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import personSerializer
from base.models import Person


@api_view(['GET'])
def getRoutes(request):
  routes = [
    'GET /',
    'GET /api/rooms',
    'GET /api/rooms/:id',
  ]
  persons = Person.objects.all()
  serializers = personSerializer(persons, many=True)
  return Response(serializers.data)

@api_view(['GET'])
def getRoute(request, id):
  routes = [
    'GET /',
    'GET /api/rooms',
    'GET /api/rooms/:id',
  ]
  person = Person.objects.get(id=id)
  serializers = personSerializer(person)
  return Response(serializers.data)