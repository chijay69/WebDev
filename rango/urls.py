from django.urls import path
from rango import views

# urls

urlpatterns =[
    path("", views.index, name = "index"),
    path("about", views.about, name = "about"),
]
