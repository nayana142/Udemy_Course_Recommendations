from django.urls import path
from .views import  recommend_courses 

urlpatterns = [
    path('',recommend_courses, name='recommend_courses'),
]
