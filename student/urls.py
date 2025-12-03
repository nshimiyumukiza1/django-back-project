from django.urls import path
from.views import LoginApi, UsersApi
from.views import SingleUserApi

urlpatterns =[
    path('student/',UsersApi.as_view(),name='cteare student'),
    path('student/<int:pk>',SingleUserApi.as_view(),name='detail student'),
    path('login/', LoginApi.as_view(),name='student login'),

]

