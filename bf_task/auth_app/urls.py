from django.urls import path

from bf_task.auth_app import views

urlpatterns = (
    path('register/', views.register, name='register'),
)