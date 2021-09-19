from django.urls import path

from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('post/category/<str:slug>/', GetPost.as_view(), name='post')
]


