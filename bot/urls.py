from django.urls import path
from .views import WebHookView,SendMessageView

urlpatterns = [
    path('setwebhook/', WebHookView.as_view(), name='telegram_webhook'),
    path('getpost/',SendMessageView.as_view(), name='send_message'),
    
]
