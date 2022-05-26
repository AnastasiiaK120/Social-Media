from django.urls import path
from .views import ShowNotifications, DeleteNotification

app_name = 'notifications'

urlpatterns = [
	path('', ShowNotifications, name='show-notifications'),
	path('<id>/delete', DeleteNotification, name='delete-notification'),
]