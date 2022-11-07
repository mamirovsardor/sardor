from django.urls import path,include
from .import views

urlpatterns = [
    path('turi/', views.TuriView.as_view()),
    path('turi/<int:pk>', views.TuriRetrieveView.as_view()),
    
    path('taom', views.ListView.as_view()),
    path('taom/<int:pk>', views.RetrieveView.as_view()),
]