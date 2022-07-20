from django.shortcuts import render
from rest_framework.generics import *
from .serializer import ObjectSerializer
from .models import *


class CreateObject(CreateAPIView):
    serializer_class = ObjectSerializer


create_object = CreateObject.as_view()


class HandleObject(RetrieveUpdateDestroyAPIView):
    serializer_class = ObjectSerializer
    queryset = Object.objects.all()


handle_object = HandleObject.as_view()


class ListObject(ListAPIView):
    serializer_class = ObjectSerializer
    queryset = Object.objects.all()


list_object = ListObject.as_view()
