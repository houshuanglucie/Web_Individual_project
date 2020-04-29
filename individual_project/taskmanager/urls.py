from django.urls import path
from . import views

urlpatterns = [
    path('connection/', views.connection, name='connection'),
    path('disconnection/', views.disconnection, name='disconnection'),
    # path('projects/', views.connection, name='projects'),
    path('project/<int:project_id>/', views.project, name='project'),
    path('task/<int:task_id>/', views.task, name='task'),
    path('add_task/', views.add_task, name='add_task'),
    path('add_journal/', views.add_journal, name='add_journal'),
]