from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import *


# Категории
class CategoryListSerializer(serializers.ModelSerializer):
    parent_name = serializers.SerializerMethodField()
    childs = RecursiveField(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image', 'slug', 'parent_name', 'childs', 'created_at', 'updated_at']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

    def get_parent_name(self, obj):
        parent = getattr(obj, 'parent', None)
        return getattr(parent, 'name', 'no parent')

class CategoryDrugSerializer(serializers.ModelSerializer):
    parent_name = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image', 'slug', 'parent_name', 'created_at', 'updated_at']
    def get_parent_name(self, obj):
        parent = getattr(obj, 'parent', None)
        return getattr(parent, 'name', 'no parent')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image']

class ReleaseFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release_form
        fields = ['id', 'name']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name']

class PharmGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharm_group
        fields = ['id', 'name']

class DrugListSerializer(serializers.ModelSerializer):
    drug_image = ImageSerializer(many=True)
    release_form = ReleaseFormSerializer()
    category = CategoryDrugSerializer()
    country = CountrySerializer()
    manufacturer = ManufacturerSerializer()
    pharm_group = PharmGroupSerializer()
    active_substance = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    class Meta:
        model = Drug
        fields = ['id', 'name', 'drug_image', 'price', 'active_substance', 'amount', 'release_form', 'brand',
                  'category', 'country', 'manufacturer', 'created_at', 'updated_at', 'pharm_group']

    def get_active_substance (self, obj):
        active_substance = getattr(obj, 'active_substance', None)
        return getattr(active_substance, 'name', 'no Active_substance')

    def get_brand(self, obj):
        brand = getattr(obj, 'brand', None)
        return getattr(brand, 'name', 'no brand')

