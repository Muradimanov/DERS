from django.urls import path
from muradapp import views

urlpatterns = [

    path('',views.index),
    path('about/',views.about)
]
