from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import *
from rest_framework.response import Response

from .serializer import *
from .models import *


class CreateListObject(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        data = Object.objects.all()
        data = RelatedObjectSerializer(data, many=True)
        return Response(data.data)


create_list_object = CreateListObject.as_view()


class HandleObject(RetrieveUpdateDestroyAPIView):
    serializer_class = ObjectSerializer
    queryset = Object.objects.all()

    def get(self, request, *args, **kwargs):
        data = Object.objects.get(id=kwargs['pk'])
        data = RelatedObjectSerializer(data)
        return Response(data.data)


handle_object = HandleObject.as_view()
