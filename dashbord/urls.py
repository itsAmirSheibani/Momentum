from django.urls import path

from .views import *

app_name = "dashbord"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("tasks/", tasks, name="tasks"),
    path("journal/", journal, name="journal"),
    path("goals/", goals, name="goals"),
    path("finance/", finance, name="finance"),
    path("settings/", settings, name="settings"),
    path('tasks/<int:task_id>/toggle/', toggle_task, name='toggle_task'),
    path('tasks/add/', add_task, name='add_task'),
    path('finances/add/',add_finance, name='add_finance'),
    path('goals/add/',add_goal,name='add_goal')
]
