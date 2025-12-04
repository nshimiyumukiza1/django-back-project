from django.urls import path
from.views import productsData
urlpatterns =[
    path('product/',productsData.as_view())

]