from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from config import settings
from .models import Movie
from django.contrib.auth import get_user_model



User = get_user_model()
recipient_list = list(User.objects.filter(is_active=True).values_list('email', flat=True))


@receiver(post_save, sender=Movie)
def send_email_on_new_film(sender, instance, created, **kwargs):
    if created:
        subject = 'Yangi film qo\'shildi!'
        message = f'Yangi film: {instance.name} qo\'shildi.'
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient_list],
        )

print("Passed")