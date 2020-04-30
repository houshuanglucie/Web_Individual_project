from django.urls import path
from . import views

urlpatterns = [
    path('connection/', views.connection, name='connection'),
    path('disconnection/', views.disconnection, name='disconnection'),
    # path('projects/', views.connection, name='projects'),
    path('project/<int:project_id>/', views.project, name='project'),
    path('task/<int:task_id>/', views.task, name='task'),
    path('add_journal/', views.add_journal, name='add_journal'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    # path('del_task/<int:task_id>/', views.del_task, name='del_task'),
]