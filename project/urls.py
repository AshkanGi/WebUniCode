from . import views
from django.urls import path

app_name = 'project'
urlpatterns = [
    path('<slug:slug>/', views.ProjectView.as_view(), name='detail_project')
]