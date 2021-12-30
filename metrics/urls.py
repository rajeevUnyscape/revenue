from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('instant', views.instant, name='instant'),
    path('historic', views.historical, name='historical'),
    path('graphical', views.graphical, name='graphical'),

]