from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('', views.LatestIndexView.as_view(), name='latestindex'),
    path('<int:pk>/', views.PostView.as_view(), name='detail'),
]
