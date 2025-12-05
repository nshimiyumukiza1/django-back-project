from django.urls import path
from .views import CommentView

urlpatterns = [
    path('students/<int:student_id>/comment/', CommentView.as_view()),
    path('products/<int:product_id>/comment/', CommentView.as_view()),
]
