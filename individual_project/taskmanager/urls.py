from django.urls import path
from . import views

urlpatterns = [
    path('', views.connection, name='connection'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:project_id>/', views.project, name='project'),
    path('project/task/', views.task, name='task'),
]