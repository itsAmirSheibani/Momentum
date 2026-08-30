from django.urls import path

from .views import *

app_name = 'dashbord'

urlpatterns = [

    # Dashbord and Settings:
    path('', dashboard, name='dashboard'),
    path('settings/', settings, name='settings'),

    # Tasks urls:
    path('tasks/', tasks, name='tasks'),
    path('tasks/<int:task_id>/toggle/', toggle_task, name='toggle_task'),
    path('tasks/add/', add_task, name='add_task'),
    path('tasks/<int:task_id>/delete/', delete_task, name='delete_task'),
    path('tasks/<int:task_id>/edit/', edit_task, name='edit_task'),

    # Journals urls:
    path('journal/', journal, name='journal'),
    path('journal/<int:reflection_id>/delete/',
         delete_journal, name='delete_journal'),
    path('journal/<int:reflection_id>/edit/',
         edit_journal, name='edit_journal'),

    # Goals urls:
    path('goals/', goals, name='goals'),
    path('goals/add/', add_goal, name='add_goal'),
    path('goals/<int:goal_id>/delete/', delete_goal, name='delete_goal'),
    path('goals/<int:goal_id>/edit/', edit_goal, name='edit_goal'),

    # Finances urls:
    path('finance/', finance, name='finance'),
    path('finances/add/', add_finance, name='add_finance'),
    path('finance/<int:transaction_id>/delete/',
         delete_finance, name='delete_transaction'),
    path('finance/<int:transaction_id>/edit/',
         edit_finance, name='edit_transaction'),

]
