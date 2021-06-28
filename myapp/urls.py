from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('delete/', views.DeleteView.as_view(), name='delete'),
    path('edit/', views.EditView.as_view(), name='edit'),


]