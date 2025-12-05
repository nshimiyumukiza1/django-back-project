from django.urls import path
from.views import productsData
from.views import PoductDetail
urlpatterns =[
    path('product/',productsData.as_view()),
    path('product/<int:pk>',PoductDetail.as_view())

]