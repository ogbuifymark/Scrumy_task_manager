from django.urls import path,include
from ogbuifyscrumy import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('movetask/<int:task_id>/', views.move_goal),
    path('add_user/', views.add_user, name='add_user'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
]