from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from notifications.models import Notification
from profiles.models import Profile


@login_required
def ShowNotifications(request):
    user = request.user
    try:
        request_user = Profile.objects.get(user=user)
        notifications = Notification.objects.filter(
            user=request_user).order_by(
            '-date')
        Notification.objects.filter(user=request_user, is_seen=False).update(
            is_seen=True)
        context = {
            'notifications': notifications,
            }
    except Profile.DoesNotExist:
        context = {
            'notifications': None,
            }
    return render(request, 'notifications/notifications.html', context)


def CountNotifications(request):
    user = None
    count_notifications = 0
    if request.user.is_authenticated:
        user = request.user
        try:
            request_user = Profile.objects.get(user=user)
            count_notifications = Notification.objects.filter(
                user=request_user, is_seen=False).count()
        except Profile.DoesNotExist:
            count_notifications = 0
    return {'count_notifications': count_notifications}


def DeleteNotification(request, id):
    user = None
    if request.user.is_authenticated:
        user = request.user
        try:
            request_user = Profile.objects.get(user=user)
            Notification.objects.filter(id=id, user=request_user).delete()
        except Profile.DoesNotExist:
            count_notifications = 0
        return redirect('notifications:show-notifications')