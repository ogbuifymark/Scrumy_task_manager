from django.urls import path,include
from ogbuifyscrumy import views

urlpatterns = [
path('index/', views.index),
path('movetask/<int:task_id>/', views.move_goal),
path('adduser/', views.add_user),
]