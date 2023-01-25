from django.urls import path
from web.views import login_view, tasks_view, tooth_view

app_name = 'web'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('tasks/', tasks_view, name='tasks'),
    path('tooth/', tooth_view, name='tooth'),
]