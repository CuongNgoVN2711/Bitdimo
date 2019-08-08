from django.urls import path
from . import views

urlpatterns = [
    path('users/<str:username>&<str:password>/', views.Login, name = 'auth user'),
    path('users/', views.CreateUser, name = 'add user'),
    path('filter=<str:param>/', views.ListAdminPost, name = 'get list admin post'),
    path('id=<int:id>/', views.DetailAdminPost, name = 'detail admin post'),
    path('users/post/filter=<str:param>/', views.ListUserPost, name = 'list user post')
]