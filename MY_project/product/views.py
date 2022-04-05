# from django.shortcuts import render
from rest_framework import generics, views
from . import models, serializers
from helper.paginations import *
from rest_framework.response import Response
import random

class CategoryListView(generics.ListAPIView):
    queryset = models.Category.objects.filter(parent=None)
    serializer_class = serializers.CategoryListSerializer

class CategoryView(generics.RetrieveAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoryListSerializer
    lookup_field = 'slug'

class DrugListView(generics.ListAPIView):
    queryset = models.Drug.objects.all()
    serializer_class = serializers.DrugListSerializer
    pagination_class = ListPagination

# class ResultsCreate(views.APIView):
#     def post(self, request, *args, **kwargs):
#         for x in range(0,10):
#             models.Drug.objects.create(name = random.randrange(1,4), maxball = random.randrange(5,10), user=User.objects.all().first(), science = Science.objects.all().first())
#         return Response ({
#             "status":"ok"
#         })
#     serializer_class = serializers.ResultSerializer


