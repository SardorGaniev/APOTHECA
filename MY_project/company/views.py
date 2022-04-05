# from django.shortcuts import render
from rest_framework import generics
from . import models, serializers

class BannerListView(generics.ListAPIView):
    queryset = models.Banner.objects.all()
    serializer_class = serializers.BannerListSerializer

class FeedbackCreate(generics.CreateAPIView):
    queryset = models.Feedback.objects.all()
    serializer_class = serializers.FeedbackSerializer

class FeedbackListView(generics.ListAPIView):
    queryset = models.Feedback.objects.all()
    serializer_class = serializers.FeedbackSerializer
