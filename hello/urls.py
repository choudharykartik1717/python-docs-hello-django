from django.urls import path

from . import views

urlpatterns = [    
    path('', views.hello, name='hello'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<id>/', views.edit_post, name='edit_post'),
    path('delete_post/<id>/', views.delete_post, name='delete_post'),
]
