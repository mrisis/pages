from django.urls import path
from .views import HomeView, AboutView

urlpatterns= [
    path("home/", HomeView.as_view(), name= "home"),
    path("about/",AboutView.as_view(), name="about"),
]