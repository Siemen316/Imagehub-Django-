from django.urls import path
from .import views
urlpatterns = [
    path('', views.home ,name = 'home'),
    path('Submissions', views.Submissions ,name = 'Submissions'),
]