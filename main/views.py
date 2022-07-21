from django.shortcuts import render
from rest_framework import generics, viewsets, routers
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializer import *
from .models import *


class CreateListObject(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        data = Object.objects.all()
        data = RelatedObjectSerializer(data, many=True, context={'request': request})
        return Response(data.data)


create_list_object = CreateListObject.as_view()


class HandleObject(RetrieveUpdateDestroyAPIView):
    serializer_class = ObjectSerializer
    queryset = Object.objects.all()
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        data = Object.objects.get(id=kwargs['pk'])
        data = RelatedObjectSerializer(data)
        return Response(data.data)


handle_object = HandleObject.as_view()

User = get_user_model()


class RegisterUser(mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            user = data.save()
            refresh = RefreshToken.for_user(user)
            res = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(res)
        return Response(data.errors)


register_user = RegisterUser.as_view()


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


contact_router = routers.DefaultRouter()
contact_router.register(r'contact', ContactViewSet)
