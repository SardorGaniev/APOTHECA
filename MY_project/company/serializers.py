from rest_framework import serializers
from .models import *


class BannerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
