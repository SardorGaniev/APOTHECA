from django.urls import path
from . import views

urlpatterns = [
    path('banner/', views.BannerListView.as_view()),
    path('feedback-create/', views.FeedbackCreate.as_view()),
    path('feedback-list/', views.FeedbackListView.as_view()),
    ]