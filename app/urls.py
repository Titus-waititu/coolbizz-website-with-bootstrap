from django.urls import path
from . import views


app_name = "app"
urlpatterns = [
    path("",views.index ,name="index"),
    path('portfolio-details/' ,views.portfolio , name="portfolio-details"),
    path('service-details/' ,views.service , name="service-details"),
    path('starter-page/' ,views.starter , name="starter-page")
]