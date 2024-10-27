from django.urls import path
from bot import views

urlpatterns = [
    path('<str:country>/', view=views.get_data_view, name='get_data')
]