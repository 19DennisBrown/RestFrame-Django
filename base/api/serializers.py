from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from base.models import Person



class personSerializer(ModelSerializer):
  class Meta:
    model = Person
    fields = '__all__'