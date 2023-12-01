from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_list/', views.post_list, name='post_list'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_post/<slug:slug>', views.edit_post, name='edit_post'),

]