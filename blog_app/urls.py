from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:monht>/<int:day>/<slug:post>', views.post_detail, name='post_detail'),
]