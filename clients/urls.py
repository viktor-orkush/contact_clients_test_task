from django.urls import path

from clients import views

app_name = 'clients'

urlpatterns = [
    path('create/', views.create_client, name='create_client'),
    path('edit/<int:id_client>', views.edit_client, name='edit_client'),
]
