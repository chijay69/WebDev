from django.urls import path
from . import views

#urls goes here

urlpatterns = [
    path('', views.index, name='index'),
    path('getProfile/', views.getProfile, name='getProfile'),
    path('aj/', views.AjaxHandlerView.as_view(), name='aj'),
    path('data/', views.TutorialDataView.as_view(), name='data'),
]
