from django.urls import path 
from . import views
from django.views.generic import ListView
from django.views.generic.edit import CreateView


urlpatterns = [
    path('', views.AddDetail.as_view(), name="index"),
    path('update/<int:pk>/', views.UpdateStudent.as_view(), name="update"),
    path('delete/<int:pk>/', views.DeleteStudent.as_view(), name="delete"),
    path('detail/', views.DetailListView.as_view(), name="detail") 
]