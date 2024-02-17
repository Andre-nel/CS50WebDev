from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path(route='', view=views.index, name='index'),
    path(route='add', view=views.add, name='add')
]
