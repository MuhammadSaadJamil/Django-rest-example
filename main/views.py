from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import *
from .serializer import ObjectSerializer
from .models import *


class CreateListObject(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


create_list_object = CreateListObject.as_view()


class HandleObject(RetrieveUpdateDestroyAPIView):
    serializer_class = ObjectSerializer
    queryset = Object.objects.all()


handle_object = HandleObject.as_view()
