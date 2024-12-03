from django.contrib import admin
from django.urls import path
from . views import HomeView, PostViewDetails

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path("post/<int:pk>", PostViewDetails.as_view(), name = "post-details")
]




