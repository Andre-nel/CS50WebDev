from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(route="andre", view=views.andre, name="andre"),
    path(route="david", view=views.david, name="david"),
    path("<str:name>", views.greet, name="greet"),
]
