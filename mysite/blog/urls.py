from django.urls 
import pathfrom . import views

urlpatterns = [   
    path('', views.post_list, name='post_list'),
]