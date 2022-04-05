from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view()),
    path('category/<str:slug>/', views.CategoryView.as_view()),
    path('drug/', views.DrugListView.as_view()),
    ]