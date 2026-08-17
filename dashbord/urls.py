from django.urls import path

from .views import *

app_name = "dashbord"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("tasks/", tasks, name="tasks"),
    path("journal/", journal, name="journal"),
    path("habits/", habits, name="habits"),
    path("goals/", goals, name="goals"),
    path("finance/", finance, name="finance"),
    path("settings/", settings, name="settings"),
]
